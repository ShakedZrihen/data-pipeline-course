import time
from datetime import datetime, timedelta
import requests
import json
from fastapi import FastAPI, HTTPException
import boto3
from mangum import Mangum

app = FastAPI()

sqs = boto3.client('sqs', endpoint_url='http://sqs:9324', region_name='us-west-1', aws_access_key_id='local',
                   aws_secret_access_key='local')
queue_url = 'http://sqs:9324/queue/data-raw-q'

countries = [
    "global", "ar", "au", "at", "by", "be", "bo", "br", "bg", "ca", "cl", "co", "cr", "cy", "cz",
    "dk", "do", "ec", "eg", "sv", "ee", "fi", "fr", "de", "gr", "gt", "hn", "hk", "hu", "is",
    "in", "id", "ie", "il", "it", "jp", "kz", "lv", "lt", "lu", "my", "mx", "ma", "nl", "nz",
    "ni", "ng", "no", "pk", "pa", "py", "pe", "ph", "pl", "pt", "ro", "sa", "sg", "sk", "za",
    "kr", "es", "se", "ch", "tw", "th", "tr", "ae", "ua", "gb", "uy", "us", "ve", "vn"
]


def scrape_data_for_date_and_country(date, country):
    try:
        url = f'https://charts-spotify-com-service.spotify.com/auth/v0/charts/regional-{country}-weekly/{date}'
        headers = {
            'Authorization': 'Bearer BQDDoH_0TbxG9llODA2mbwycImFz7vTgieUhSWEKxK-lRex5E4fOcRSNr3-Y2TIhWMLyw2O29sffbot_70pKVxzed_ZHvD06PgnMaCQjknbVR2J-gYtRb0YMcSoWSDY5Kbu6nlJ4SfitBeJ1_Tp8n9Hz0-Daeb1cDjEsI1hs1loBafZQvd6rf1draPJCfBHZIVUGMG16titFOkYSyDcBLq2qYcE7vsOm'
        }
        response = requests.get(url, headers=headers).text
        data = json.loads(response)

        chart_date = data['displayChart']['date']
        entries = data.get('entries', [])

        top_songs = []
        for i, entry in enumerate(entries[:10], start=1):
            track_name = entry['trackMetadata']['trackName']
            artist_name = entry['trackMetadata']['artists'][0]['name']
            release_date = entry['trackMetadata']['releaseDate']
            rank = entry['chartEntryData']['currentRank']
            streams = entry['chartEntryData']['rankingMetric']['value']
            previous_rank = entry['chartEntryData'].get('previousRank', "N/A")
            peak_rank = entry['chartEntryData'].get('peakRank', "N/A")

            song_data = {
                'date': chart_date,
                'song_name': track_name,
                'artist_names': artist_name,
                'release_date': release_date,
                'streams': streams,
                'country': country,
                "Rankings Table": {
                    "chartName": f"Spotify Regional - {country.upper()}",
                    "chartLink": url,
                    "currentRank": rank,
                    "previousRank": previous_rank,
                    "peakRank": peak_rank,
                    "rankDate": chart_date,
                }
            }
            top_songs.append(song_data)

        sqs_response = sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=json.dumps(top_songs, ensure_ascii=False)
        )

        if sqs_response['ResponseMetadata']['HTTPStatusCode'] == 200:
            print(f"Data for {chart_date} in {country.upper()} sent to SQS successfully")
        else:
            print(f"Failed to send data to SQS for {chart_date} in {country.upper()}")
            raise HTTPException(status_code=500,
                                detail=f"Failed to send data to SQS for {chart_date} in {country.upper()}")

    except Exception as e:
        print(f"Exception on {date} in {country.upper()}: {str(e)}")


@app.post("/scrape")
def scrape_data():
    start_date = datetime(2018, 3, 15)
    end_date = datetime(2024, 8, 15)
    current_date = start_date

    while current_date <= end_date:
        for country in countries:
            scrape_data_for_date_and_country(current_date.strftime('%Y-%m-%d'), country)
            time.sleep(0.3)
        current_date += timedelta(weeks=1)

    return {"message": "Scraping completed"}


handler = Mangum(app)