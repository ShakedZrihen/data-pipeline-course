import time
from datetime import datetime, timedelta
import requests
import json
import boto3

# Initialize SQS client with local endpoint configuration
sqs = boto3.client('sqs', endpoint_url='http://sqs:9324', region_name='us-west-1', aws_access_key_id='local',
                   aws_secret_access_key='local')
queue_url = 'http://sqs:9324/queue/data-raw-q'

# countries = [
#     "global", "ar", "au", "at", "by", "be", "bo", "br", "bg", "ca", "cl", "co", "cr", "cy", "cz",
#     "dk", "do", "ec", "eg", "sv", "ee", "fi", "fr", "de", "gr", "gt", "hn", "hk", "hu", "is",
#     "in", "id", "ie", "il", "it", "jp", "kz", "lv", "lt", "lu", "my", "mx", "ma", "nl", "nz",
#     "ni", "ng", "no", "pk", "pa", "py", "pe", "ph", "pl", "pt", "ro", "sa", "sg", "sk", "za",
#     "kr", "es", "se", "ch", "tw", "th", "tr", "ae", "ua", "gb", "uy", "us", "ve", "vn"
# ]

# List of countries to scrape data for
countries = [
    "global", "ar", "au", "at", "il", "us", "es"
]


def scrape_data_for_date_and_country(date, country):
    try:
        # Construct the URL for the Spotify regional chart data
        url = f'https://charts-spotify-com-service.spotify.com/auth/v0/charts/regional-{country}-weekly/{date}'
        headers = {
            # Include the authorization token in the request headers
            'Authorization': 'Bearer BQD0yxqP4Xx_nAz2OTgPaLTTFtz6i1FYBoLe7BXCBdsRcOwvvoRouKBmXQ3DFv-ZRyooV52i3K9NKoSUHCzIJADcJNqi1_QRtlUH0SqtY9FGkuCvLisi2p3nNvvhKES_LysRWicrJcaJ8SXuz0LUFxXXEyMz8Xe76o-cl_DkCOmAVdoZfrviuGtCYJYuwDjsydYW3pHCMCzFjaI0je-kxol7gKMh0rYy'
        }
        response = requests.get(url, headers=headers).text
        data = json.loads(response)

        chart_date = data['displayChart']['date'] # Extract the chart date
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

            # Structure the song data for SQS message
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

        # Send the scraped data to the SQS queue
        sqs_response = sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=json.dumps(top_songs, ensure_ascii=False)
        )

        # Check if the data was successfully sent to SQS
        if sqs_response['ResponseMetadata']['HTTPStatusCode'] == 200:
            print(f"Data for {chart_date} in {country.upper()} sent to SQS successfully")
        else:
            print(f"Failed to send data to SQS for {chart_date} in {country.upper()}")

    except Exception as e:
        print(f"Exception on {date} in {country.upper()}: {str(e)}")


def app(event, context):
    # Calculate the date for last week's chart
    today = datetime.utcnow().date()
    last_week = today - timedelta(days=7)

    # Scrape data for each country in the list
    for country in countries:
        scrape_data_for_date_and_country(last_week.strftime('%Y-%m-%d'), country)
        time.sleep(0.3) # Throttle requests to avoid hitting rate limits

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Scraping completed"})
    }

