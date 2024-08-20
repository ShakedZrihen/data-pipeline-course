import json
import logging
from datetime import datetime, timedelta, date
from playwright.async_api import (
    async_playwright,
    TimeoutError as PlaywrightTimeoutError,
)
import re

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


async def generate_dates(start_date, num_days, interval="daily"):
    """Generate a list of dates from start_date, ensuring weekly dates are Thursdays."""
    dates = []
    if isinstance(start_date, date):
        start_date = start_date.strftime("%Y-%m-%d")

    current_date = datetime.strptime(start_date, "%Y-%m-%d")

    for _ in range(num_days):
        if interval == "weekly":
            # Adjust to the previous Thursday
            while current_date.weekday() != 3:  # 3 corresponds to Thursday
                current_date -= timedelta(days=1)
            dates.append(current_date.strftime("%Y-%m-%d"))
            current_date -= timedelta(weeks=1)  # Move to the previous week
        else:
            dates.append(current_date.strftime("%Y-%m-%d"))
            current_date -= timedelta(days=1)  # Move to the previous day for daily

    return dates


async def build_urls(base_urls, country_code, daily_dates, weekly_dates):
    """Build a list of URLs to scrape based on the provided base URLs, country code, and dates."""
    urls = []

    for key, base_url in base_urls.items():
        if "daily" in key:
            for date in daily_dates:
                url = base_url.format(country_code=country_code, date=date)
                urls.append(url)
        elif "weekly" in key:
            for date in weekly_dates:
                url = base_url.format(country_code=country_code, date=date)
                urls.append(url)

    return urls


async def login_spotify(context, username, password):
    """Login to Spotify using the given browser context."""
    page = await context.new_page()

    await page.goto("https://accounts.spotify.com/en/login")
    await page.fill('input[id="login-username"]', username)
    await page.fill('input[id="login-password"]', password)
    await page.click('button[id="login-button"]')
    await page.wait_for_timeout(3000)

    if "https://accounts.spotify.com/en/status" in page.url:
        logging.info("Login successful!")
    else:
        logging.error("Login failed!")


async def intercept_response(response):
    """Intercept JSON responses and return the parsed JSON data."""
    if response.headers.get("content-type") == "application/json":
        if re.match(
            r"https://charts-spotify-com-service\.spotify\.com/auth/v0/charts/.+/\d{4}-\d{2}-\d{2}",
            response.request.url,
        ):
            json_data = await response.json()
            logging.info(f"Data fetched from {response.request.url}")
            return json_data
    return None


async def scrape_charts_data(context, urls):
    """Scrape data from the provided URLs and return the collected JSON data."""
    collected_data = []

    for url in urls:
        try:
            page = await context.new_page()

            # Set up response interception before navigating
            async def on_response(response):
                data = await intercept_response(response)
                if data:
                    collected_data.append(data)

            page.on("response", on_response)
            logging.info(f"Scraping URL: {url}")
            await page.goto(url)

            # Wait for a specific selector, handling the possibility of timeout
            await page.wait_for_selector(
                "//div[@data-testid]", timeout=30000
            )  # Adjust timeout if needed

            # Wait for a short time to ensure all responses are captured
            await page.wait_for_timeout(2000)
            logging.info(f"Successfully scraped data from {url}")

        except PlaywrightTimeoutError:
            logging.error(f"Timeout error when scraping URL: {url}")
        except Exception as e:
            logging.error(f"Error scraping URL: {url}. Exception: {str(e)}")
        finally:
            await page.close()

    return collected_data


async def save_data(data, save_path):
    """Save the collected data to a file."""
    with open(save_path, "w") as f:
        json.dump(data, f, indent=4)

    logging.info(f"Data saved to {save_path}")


async def spotify_scraper_handler(
    username,
    password,
    country_codes,
    start_date,
    save_path,
    daily_days=2,
    weekly_weeks=2,
):
    """Main handler for the Spotify scraper, taking dynamic input parameters."""
    # Define base URLs for different charts
    base_urls = {
        "daily_country": "https://charts.spotify.com/charts/view/regional-{country_code}-daily/{date}",
        "weekly_country": "https://charts.spotify.com/charts/view/regional-{country_code}-weekly/{date}",
        "daily_global": "https://charts.spotify.com/charts/view/regional-global-daily/{date}",
        "weekly_global": "https://charts.spotify.com/charts/view/regional-global-weekly/{date}",
    }

    all_collected_data = []

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()

        await login_spotify(context, username, password)

        for country_code in country_codes:
            # Generate daily and weekly dates separately
            daily_dates = await generate_dates(
                start_date, num_days=daily_days, interval="daily"
            )
            weekly_dates = await generate_dates(
                start_date, num_days=weekly_weeks, interval="weekly"
            )

            # Build all URLs to scrape for this country code
            urls = await build_urls(base_urls, country_code, daily_dates, weekly_dates)

            # Scrape the data
            data = await scrape_charts_data(context, urls)
            all_collected_data.extend(data)

        await browser.close()

    # Save the collected data
    await save_data(all_collected_data, save_path)

    return all_collected_data
