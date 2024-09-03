from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date, BigInteger, ForeignKey, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import logging


class DBManager:
    def __init__(self, database_url):
        # Initialize the database engine, metadata, and session maker
        self.engine = create_engine(database_url)
        self.metadata = MetaData()
        self.Session = sessionmaker(bind=self.engine)

        # Define the Artists table
        self.artists_table = Table(
            'Artists', self.metadata,
            Column('artistID', Integer, primary_key=True, autoincrement=True),
            Column('genreID', Integer, ForeignKey('Genres.genreID')),
            Column('artistName', String, nullable=False),
            Column('country', String, nullable=False),
            Column('gender', String)
        )

        # Define the Songs table
        self.songs_table = Table(
            'Songs', self.metadata,
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

        # Define the Rankings table
        self.rankings_table = Table(
            'Rankings', self.metadata,
            Column('rankingID', Integer, primary_key=True, autoincrement=True),
            Column('songID', Integer, ForeignKey('Songs.songID')),
            Column('chartName', String, nullable=False),
            Column('chartLink', String, nullable=False),
            Column('currentRank', Integer, nullable=False),
            Column('previousRank', Integer),
            Column('rankDate', Date)
        )

        # Define the Genres table
        self.genres_table = Table(
            'Genres', self.metadata,
            Column('genreID', Integer, primary_key=True, autoincrement=True),
            Column('genreName', String, nullable=False)
        )

        # Create all tables in the database
        self.metadata.create_all(self.engine)

    def insert(self, data):
        session = self.Session()
        try:
            # Insert genres
            genre_id = self._insert_genre(session, data.get('Genres Table', []))

            # Insert artists
            artist_id = self._insert_artist(session, data.get('Artists Table', []), genre_id)

            # Insert songs
            song_id = self._insert_song(session, data.get('Songs Table', []), artist_id, genre_id)

            # Insert rankings
            self._insert_ranking(session, data.get('Rankings Table', {}), song_id)

            session.commit()
            return True
        except SQLAlchemyError as e:
            session.rollback()
            logging.error(f"Database insertion error: {str(e)}")
            raise
        finally:
            session.close()

    def _insert_genre(self, session, genres):
        # Insert genre into the database if it does not already exist
        for genre in genres:
            genre_name = genre['genreName']
            genre_result = session.execute(
                select(self.genres_table.c.genreID).where(self.genres_table.c.genreName == genre_name)).fetchone()
            if not genre_result:
                insert_genre = self.genres_table.insert().values(genreName=genre_name)
                result = session.execute(insert_genre)
                return result.inserted_primary_key[0]
            return genre_result[0]
        return None

    def _insert_artist(self, session, artists, genre_id):
        # Insert artist into the database if they do not already exist
        for artist in artists:
            artist_name = artist['artistName']
            artist_result = session.execute(
                select(self.artists_table.c.artistID).where(self.artists_table.c.artistName == artist_name)).fetchone()
            if not artist_result:
                insert_artist = self.artists_table.insert().values(
                    genreID=genre_id,
                    artistName=artist_name,
                    country=artist['country'],
                    gender=artist['gender']
                )
                result = session.execute(insert_artist)
                return result.inserted_primary_key[0]
            return artist_result[0]
        return None

    def _insert_song(self, session, songs, artist_id, genre_id):
        # Insert song into the database
        for song in songs:
            insert_song = self.songs_table.insert().values(
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
            result = session.execute(insert_song)
            return result.inserted_primary_key[0]
        return None

    def _insert_ranking(self, session, ranking, song_id):
        # Insert ranking associated with a song into the database
        insert_ranking = self.rankings_table.insert().values(
            songID=song_id,
            chartName=ranking['chartName'],
            chartLink=ranking['chartLink'],
            currentRank=ranking['currentRank'],
            previousRank=ranking['previousRank'],
            rankDate=ranking['rankDate']
        )
        session.execute(insert_ranking)

    def get_charts(self, date):
        session = self.Session()
        try:
            # Query to retrieve chart data based on the specified date
            query = select(
                self.rankings_table.c.currentRank,
                self.rankings_table.c.chartName,
                self.songs_table.c.songName,
                self.artists_table.c.artistName,
                self.artists_table.c.gender,
                self.songs_table.c.albumIMG,
                self.songs_table.c.long.label('duration'),
                self.songs_table.c.songLink.label('spotify_url'),
                self.genres_table.c.genreName,
                self.songs_table.c.language
            ).select_from(
                self.rankings_table.outerjoin(self.songs_table,
                                              self.rankings_table.c.songID == self.songs_table.c.songID)
                .outerjoin(self.artists_table, self.songs_table.c.artistID == self.artists_table.c.artistID)
                .outerjoin(self.genres_table, self.songs_table.c.genreID == self.genres_table.c.genreID)
            ).where(self.rankings_table.c.rankDate == date)

            result = session.execute(query).fetchall()
            return self._format_charts(result)
        finally:
            session.close()

    def _format_charts(self, result):
        charts = {}
        country_code_map = {
            "au": "AUS", "ar": "ARG", "at": "AUT", "be": "BEL",
            "global": "RUS", "il": "ISR", "us": "USA", "es": "ESP"
        }

        # Format the retrieved chart data
        for row in result:
            chart_name_parts = row.chartName.split(' - ')
            original_country_code = chart_name_parts[-1].lower() if len(chart_name_parts) > 1 else 'global'
            country_code = country_code_map.get(original_country_code, original_country_code.upper())

            if country_code not in charts:
                charts[country_code] = []

            charts[country_code].append({
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
            })

        # Sort the charts by position for each country
        for country_code in charts:
            charts[country_code] = sorted(charts[country_code], key=lambda x: x['position'])

        return charts