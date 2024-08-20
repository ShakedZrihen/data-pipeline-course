import json
import re
from datetime import datetime, timedelta
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import scrapy
from scrapy.spiders import Spider
from scrapy.http import HtmlResponse
from settings import settings
import asyncio


class SpotifySpider(Spider):
    name = "spotify"

    def start_requests(self):
        base_urls = {
            "daily_country": "https://charts.spotify.com/charts/view/regional-{country_code}-daily/{date}",
            "weekly_country": "https://charts.spotify.com/charts/view/regional-{country_code}-weekly/{date}",
            "daily_global": "https://charts.spotify.com/charts/view/regional-global-daily/{date}",
            "weekly_global": "https://charts.spotify.com/charts/view/regional-global-weekly/{date}",
        }

        countries = ["us", "il", "gb"]  # Example country codes
        dates = self.generate_dates(weeks=4)  # Generate dates for the last 4 weeks

        # Use Scrapy's 'requests' to trigger the asynchronous fetch
        for country in countries:
            for chart_type, url_template in base_urls.items():
                for date in dates:
                    if "country" in chart_type:
                        url = url_template.format(country_code=country, date=date)
                    else:
                        url = url_template.format(date=date)
                    yield scrapy.Request(url=url, callback=self.login_and_fetch)

    def generate_dates(self, weeks=4):
        """Generate a list of dates in the format 'YYYY-MM-DD' for the last `weeks` weeks."""
        today = datetime.today()
        return [
            (today - timedelta(weeks=i, days=2)).strftime("%Y-%m-%d")
            for i in range(weeks)
        ]

    async def login_and_fetch(self, response):
        """Log in to Spotify and fetch chart data from the given URL."""
        url = response.url
        username = settings.spotify.username
        password = settings.spotify.password

        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context()
            page = await context.new_page()
            page.on("response", self.intercept_response)

            # Log in to Spotify
            await page.goto("https://accounts.spotify.com/en/login")
            await page.fill('input[id="login-username"]', username)
            await page.fill('input[id="login-password"]', password)
            await page.click('button[id="login-button"]')
            await page.wait_for_timeout(3000)

            # Verify login success
            if "https://accounts.spotify.com/en/status" in page.url:
                self.log("Login successful!")
            else:
                self.log("Login failed!")
                return

            # Navigate to the chart URL
            await page.goto(url)
            await page.wait_for_selector("//div[@data-testid]")

            # Process the page source
            page_source = await page.content()
            soup = BeautifulSoup(page_source, "html.parser")

            # Parse and send the chart data
            chart_data = self.parse_chart(soup)
            self.send_to_sqs(chart_data)

            await browser.close()

    def intercept_response(self, response):
        """Intercept API responses and extract data."""
        if response.headers.get("content-type") == "application/json":
            if re.match(
                r"https://charts-spotify-com-service\.spotify\.com/auth/v0/charts/regional-\w+-\w+/\d{4}-\d{2}-\d{2}",
                response.request.url,
            ):
                self.log(response.request.url)
                self.log(json.dumps(response.json(), indent=4))
        return response

    def parse_chart(self, soup):
        """Parse chart data from the BeautifulSoup object."""
        chart_name = soup.title.string if soup.title else "Unknown Chart"

        entries = []
        for track in soup.select(".chart-table-row"):
            song_info = {
                "song_name": track.select_one(".chart-table-track > strong").get_text(
                    strip=True
                ),
                "artist_name": track.select_one(".chart-table-track > span").get_text(
                    strip=True
                ),
                "genre": self.extract_genre(track),
                "song_length": self.extract_song_length(track),
                "language": self.extract_language(track),
                "play_link": self.extract_play_link(track),
                "artist_info": self.extract_artist_info(track),
            }
            entries.append(song_info)

        return {
            "chart_name": chart_name,
            "entries": entries,
        }

    def extract_genre(self, track):
        """Placeholder: Extract genre from the track element."""
        return track.get("data-genre", "Unknown")

    def extract_song_length(self, track):
        """Placeholder: Extract song length from the track element."""
        return track.get("data-length", "Unknown")

    def extract_language(self, track):
        """Placeholder: Extract language from the track element."""
        return track.get("data-language", "Unknown")

    def extract_play_link(self, track):
        """Extract the link to play the song."""
        return track.select_one(".play-button").get("href", "#")

    def extract_artist_info(self, track):
        """Placeholder: Extract artist information."""
        artist_info = {
            "is_band": track.get("data-band", "Unknown"),
            "country": track.get("data-country", "Unknown"),
            "additional_info": track.get("data-info", "None"),
        }
        return artist_info

    def parse(self, response):
        pass
