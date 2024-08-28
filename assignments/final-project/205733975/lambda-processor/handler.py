import json
import requests
import base64
# Spotify API
client_id = '1a18c8c9bc3e4d09aebe778ff7b55f9b'
client_secret = 'e1884f7071af47a18ffec342f9e9c5ee'

crud_url = 'http://crud:3003/insert-data'
def get_spotify_token():
    auth_url = "https://accounts.spotify.com/api/token"
    headers = {
        'Authorization': 'Basic ' + base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
    }
    data = {
        'grant_type': 'client_credentials'
    }
    response = requests.post(auth_url, headers=headers, data=data)
    token_info = response.json()
    return token_info['access_token']


def get_artist_genres(artist_id, token):
    artist_url = f"https://api.spotify.com/v1/artists/{artist_id}"
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(artist_url, headers=headers)
    artist_data = response.json()
    return artist_data.get('genres', [])


def get_artist_gender_from_wikipedia(artist_name):
    wikipedia_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{artist_name.replace(' ', '_')}"
    response = requests.get(wikipedia_url)
    if response.status_code == 200:
        summary = response.json().get('extract', '').lower()
        if 'she' in summary or 'her' in summary:
            return 'Female'
        elif 'he' in summary or 'his' in summary:
            return 'Male'
        else:
            return 'Unknown'
    else:
        return 'Unknown'


def get_spotify_data(song_name, artist_names, country):
    token = get_spotify_token()
    print(f"Token: {token[:10]}...")
    search_url = "https://api.spotify.com/v1/search"
    headers = {
        'Authorization': f'Bearer {token}'
    }
    query = f"track:{song_name} artist:{artist_names}"
    params = {
        'q': query,
        'type': 'track',
        'limit': 1
    }
    response = requests.get(search_url, headers=headers, params=params)
    result = response.json()

    if result['tracks']['items']:
        track = result['tracks']['items'][0]
        artist = track['artists'][0]
        artist_id = artist['id']
        genres = get_artist_genres(artist_id, token)
        first_genre = genres[0] if genres else None
        gender = get_artist_gender_from_wikipedia(artist['name'])

        return {
            "Artists Table": [
                {
                    "artistName": artist['name'],
                    "country": country,
                    "genreID": "",
                    "gender": gender
                }
            ],
            "Songs Table": {
                "songName": track['name'],
                "releaseDate": track['album']['release_date'],
                "albumIMG": track['album']['images'][0]['url'] if track['album']['images'] else "N/A",
                "songLink": track['external_urls']['spotify'],
                "streams": "",
                "long": track['duration_ms']
            },
            "Genres Table": [
                {
                    "genreName": first_genre
                }
            ] if first_genre else []
        }
    else:
        return None


def send_data_to_crud(data):
    try:
        response = requests.post(crud_url, json=data)
        if response.status_code == 200:
            print("Data successfully sent to CRUD service")
        else:
            print(f"Failed to send data to CRUD service: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"Error sending data to CRUD service: {str(e)}")


def process_message(event, context):
    for record in event['Records']:
        message_body = record['body']
        print("Received message from SQS:", message_body)
        message_data = json.loads(message_body)

        for song in message_data:
            song_name = song['song_name']
            artist_names = song['artist_names']
            country = song['country']
            streams = song['streams']

            try:
                spotify_data = get_spotify_data(song_name, artist_names, country)
                if spotify_data:
                    # Artists Table
                    artists_table = [
                        {
                            "artistName": artist['artistName'],
                            "genreID": "",
                            "country": artist['country'],
                            "gender": artist['gender']
                        } for artist in spotify_data['Artists Table']
                    ]

                    # Songs Table
                    songs_table = [
                        {
                            "songName": song['song_name'],
                            "artistID": "",
                            "genreID": "",
                            "releaseDate": song['release_date'],
                            "albumIMG": spotify_data['Songs Table']['albumIMG'],
                            "songLink": spotify_data['Songs Table']['songLink'],
                            "streams": streams,
                            "long": spotify_data['Songs Table']['long']
                        }
                        for artist in spotify_data['Artists Table']
                    ]

                    # Rankings Table
                    rankings_table = {
                        "chartName": song["Rankings Table"]["chartName"],
                        "chartLink": song["Rankings Table"]["chartLink"],
                        "currentRank": song["Rankings Table"]["currentRank"],
                        "previousRank": song["Rankings Table"]["previousRank"],
                        "rankDate": song["Rankings Table"]["rankDate"]
                    }

                    # Genres Table
                    genres_table = spotify_data.get('Genres Table', [])

                    # Combine everything into the final structure
                    combined_data = {
                        "Artists Table": artists_table,
                        "Songs Table": songs_table,
                        "Rankings Table": rankings_table,
                        "Genres Table": genres_table
                    }

                    print(json.dumps(combined_data, ensure_ascii=False, indent=4))
                    send_data_to_crud(combined_data)

                else:
                    print(f"No additional data found for {song_name} by {artist_names}")

            except Exception as e:
                print(f"Error processing the song: {e}")

    return {
        'statusCode': 200,
        'body': json.dumps('Messages processed successfully')
    }
