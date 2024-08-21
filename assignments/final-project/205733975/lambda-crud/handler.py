from fastapi import FastAPI, HTTPException, Query
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date, BigInteger, ForeignKey, select, and_
from mangum import Mangum

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
    try:
        with engine.connect() as conn:
            query = select(
                rankings_table.c.currentRank,
                songs_table.c.songName,
                artists_table.c.artistName,
                artists_table.c.gender,
                songs_table.c.albumIMG,
                songs_table.c.long.label('duration'),
                songs_table.c.songLink.label('spotify_url'),
                genres_table.c.genreName,
                songs_table.c.language,
                artists_table.c.country
            ).select_from(
                rankings_table.join(songs_table, rankings_table.c.songID == songs_table.c.songID)
                .join(artists_table, songs_table.c.artistID == artists_table.c.artistID)
                .join(genres_table, songs_table.c.genreID == genres_table.c.genreID)
            ).where(rankings_table.c.rankDate == date)

            result = conn.execute(query).fetchall()

            for row in result:
                country_code = row.country
                if country_code not in charts:
                    charts[country_code] = []

                song_data = {
                    "position": row.currentRank,
                    "song": row.songName,
                    "artist": row.artistName,
                    "album": row.albumIMG,
                    "duration": str(row.duration),
                    "spotify_url": row.spotify_url,
                    "artistFeatures": {
                        "type": "Solo",
                        "gender": row.gender if row.gender else "Unknown"
                    },
                    "songFeatures": {
                        "key": "Unknown",
                        "genre": row.genreName if row.genreName else "Unknown",
                        "language": row.language if row.language else "Unknown"
                    }
                }
                charts[country_code].append(song_data)

        if not charts:
            raise HTTPException(status_code=404, detail="No charts found for the given date")

        return {"charts": charts}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve charts: {str(e)}")

handler = Mangum(app)