from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date, BigInteger, ForeignKey, select, and_
from mangum import Mangum
import json
from sqlalchemy import create_engine, select, and_
import logging

DATABASE_URL = "postgresql://user:password@postgres/mydb"

engine = create_engine(DATABASE_URL)
metadata = MetaData()

# Define the tables
artists_table = Table(
    'Artists', metadata,
    Column('artistID', Integer, primary_key=True, autoincrement=True),
    Column('genreID', Integer, ForeignKey('Genres.genreID')),
    Column('artistName', String, nullable=False),
    Column('country', String, nullable=False),
    Column('gender', String)
)

songs_table = Table(
    'Songs', metadata,
    Column('songID', Integer, primary_key=True, autoincrement=True),
    Column('artistID', Integer, ForeignKey('Artists.artistID')),
    Column('genreID', Integer, ForeignKey('Genres.genreID')),
    Column('songName', String, nullable=False),
    Column('language', String),
    Column('releaseDate', Date),
    Column('albumIMG', String),
    Column('songLink', String),
    Column('streams', BigInteger),
    Column('long', BigInteger)
)

rankings_table = Table(
    'Rankings', metadata,
    Column('rankingID', Integer, primary_key=True, autoincrement=True),
    Column('songID', Integer, ForeignKey('Songs.songID')),
    Column('chartName', String, nullable=False),
    Column('chartLink', String, nullable=False),
    Column('currentRank', Integer, nullable=False),
    Column('previousRank', Integer),
    Column('rankDate', Date)
)

genres_table = Table(
    'Genres', metadata,
    Column('genreID', Integer, primary_key=True, autoincrement=True),
    Column('genreName', String, nullable=False)
)

metadata.create_all(engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)
@app.post("/insert-data")
def insert_data(data: dict):
    with engine.connect() as conn:
        with conn.begin():
            try:
                # Insert genres
                genre_id = None
                for genre in data.get('Genres Table', []):
                    genre_name = genre['genreName']
                    genre_result = conn.execute(select(genres_table.c.genreID).where(genres_table.c.genreName == genre_name)).fetchone()

                    if not genre_result:
                        insert_genre = genres_table.insert().values(genreName=genre_name)
                        genre_id = conn.execute(insert_genre).inserted_primary_key[0]
                    else:
                        genre_id = genre_result[0]

                # Insert artists
                artist_id = None
                for artist in data.get('Artists Table', []):
                    artist_name = artist['artistName']
                    artist_country = artist['country']
                    artist_gender = artist['gender']
                    artist_result = conn.execute(select(artists_table.c.artistID).where(artists_table.c.artistName == artist_name)).fetchone()

                    if not artist_result:
                        insert_artist = artists_table.insert().values(
                            genreID=genre_id,
                            artistName=artist_name,
                            country=artist_country,
                            gender=artist_gender
                        )
                        artist_id = conn.execute(insert_artist).inserted_primary_key[0]
                    else:
                        artist_id = artist_result[0]

                # Insert songs
                song_id = None
                for song in data.get('Songs Table', []):
                    insert_song = songs_table.insert().values(
                        artistID=artist_id,
                        genreID=genre_id,
                        songName=song['songName'],
                        language=song.get('language'),
                        releaseDate=song['releaseDate'],
                        albumIMG=song['albumIMG'],
                        songLink=song['songLink'],
                        streams=song['streams'],
                        long=song['long']
                    )
                    song_id = conn.execute(insert_song).inserted_primary_key[0]

                # Insert rankings
                insert_ranking = rankings_table.insert().values(
                    songID=song_id,
                    chartName=data['Rankings Table']['chartName'],
                    chartLink=data['Rankings Table']['chartLink'],
                    currentRank=data['Rankings Table']['currentRank'],
                    previousRank=data['Rankings Table']['previousRank'],
                    rankDate=data['Rankings Table']['rankDate']
                )
                conn.execute(insert_ranking)

                return {"status": "Data inserted successfully"}

            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Failed to insert data: {str(e)}")


@app.get("/charts")
def get_charts(date: str = Query(..., description="The date for which to retrieve the charts")):
    charts = {}

    # Country code mapping
    country_code_map = {
        "au": "AUS",
        "ar": "ARG",
        "at": "AUT",
        "be": "BEL",
        "global": "RUS",
        "il":"ISR",
        "us":"USA",
        "es": "ESP"
    }

    try:
        with engine.connect() as conn:
            query = select(
                rankings_table.c.currentRank,
                rankings_table.c.chartName,
                songs_table.c.songName,
                artists_table.c.artistName,
                artists_table.c.gender,
                songs_table.c.albumIMG,
                songs_table.c.long.label('duration'),
                songs_table.c.songLink.label('spotify_url'),
                genres_table.c.genreName,
                songs_table.c.language
            ).select_from(
                rankings_table.outerjoin(songs_table, rankings_table.c.songID == songs_table.c.songID)
                .outerjoin(artists_table, songs_table.c.artistID == artists_table.c.artistID)
                .outerjoin(genres_table, songs_table.c.genreID == genres_table.c.genreID)
            ).where(rankings_table.c.rankDate == date)

            result = conn.execute(query).fetchall()

            logging.info(f"Total rows fetched: {len(result)}")

            for row in result:
                try:
                    chart_name_parts = row.chartName.split(' - ')
                    if len(chart_name_parts) > 1:
                        original_country_code = chart_name_parts[-1].lower()
                    else:
                        original_country_code = 'global'

                    country_code = country_code_map.get(original_country_code, original_country_code.upper())

                    if country_code not in charts:
                        charts[country_code] = []

                    song_data = {
                        "position": row.currentRank,
                        "song": row.songName if row.songName is not None else "Unknown Song",
                        "artist": row.artistName if row.artistName is not None else "Unknown Artist",
                        "album": row.albumIMG if row.albumIMG is not None else "",
                        "duration": str(row.duration) if row.duration is not None else "0",
                        "spotify_url": row.spotify_url if row.spotify_url is not None else "",
                        "artistFeatures": {
                            "type": "Solo",
                            "gender": row.gender if row.gender is not None else "Unknown"
                        },
                        "songFeatures": {
                            "key": "Unknown",
                            "genre": row.genreName if row.genreName is not None else "pop",
                            "language": row.language if row.language is not None else "Unknown"
                        }
                    }
                    charts[country_code].append(song_data)
                except Exception as e:
                    logging.error(f"Error processing row: {row}. Error: {str(e)}")

            for country_code in charts:
                charts[country_code] = sorted(charts[country_code], key=lambda x: x['position'])

            logging.info(f"Countries in result: {list(charts.keys())}")
            for country, songs in charts.items():
                logging.info(f"{country}: {len(songs)} songs")

        if not charts:
            raise HTTPException(status_code=404, detail="No charts found for the given date")

        return {"charts": charts}

    except Exception as e:
        logging.error(f"Failed to retrieve charts: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to retrieve charts: {str(e)}")

def get_available_dates():
    try:
        with open('availDates.json', 'r') as file:
            dates_data = json.load(file)

        return dates_data
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="availDates.json file not found")
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Error decoding availDates.json")


@app.get("/charts/available-dates")
async def available_dates():
    return get_available_dates()

handler = Mangum(app)

