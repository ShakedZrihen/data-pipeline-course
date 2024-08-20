import json


def parse_spotify_charts_data(charts_data):
    parsed_data = []

    for chart in charts_data:
        chart_name = chart["displayChart"]["chartMetadata"]["readableTitle"]
        chart_date = chart["displayChart"]["date"]

        for entry in chart["entries"]:
            track_metadata = entry["trackMetadata"]
            artists = track_metadata.get("artists", [])
            song_name = track_metadata.get("trackName", "Unknown")
            song_url = track_metadata.get("trackUri", "Unknown")
            song_length = "Unknown"  # Length is not provided in the data; needs to be fetched separately.
            song_genre = chart["displayChart"]["chartMetadata"].get("genre", "Unknown")
            language = "Unknown"  # Language is not provided in the data; needs to be determined separately.

            for artist in artists:
                artist_name = artist.get("name", "Unknown")
                artist_genre = (
                    "Unknown"  # Genre is not provided; needs to be fetched separately.
                )
                artist_type = "Solo" if len(artists) == 1 else "Band"
                artist_country = (
                    "Unknown"  # Country is not provided in the artist data.
                )

                parsed_entry = {
                    "chart_name": chart_name,
                    "chart_date": chart_date,
                    "song_name": song_name,
                    "song_length": song_length,
                    "song_url": song_url,
                    "song_genre": song_genre,
                    "language": language,
                    "artist_name": artist_name,
                    "artist_genre": artist_genre,
                    "artist_type": artist_type,
                    "artist_country": artist_country,
                }
                parsed_data.append(parsed_entry)

    return parsed_data


def save_data_to_json(data, save_path):
    with open(save_path, "w") as file:
        json.dump(data, file, indent=4)

    return save_path


def parse_and_save_spotify_charts_data(charts_data, save_path):
    parsed_data = parse_spotify_charts_data(charts_data)
    save_data_to_json(parsed_data, save_path)
    return parsed_data
