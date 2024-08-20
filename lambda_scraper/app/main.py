import os
import sys

# Adjust this path to the root of your project
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi import FastAPI, Depends
from app.models import ScraperConfig  # Absolute import
from spotify_scraper import spotify_scraper_handler
from spotify_parser import parse_and_save_spotify_charts_data
from settings import settings

app = FastAPI()


@app.post("/scrape/")
async def start_scrape(config: ScraperConfig):
    # Extract parameters from the request config
    username = settings.spotify.username
    password = settings.spotify.password
    country_codes = config.country_codes
    start_date = config.start_date
    save_path = config.save_path or "spotify_charts_data.json"

    # Run the scraper
    collected_data = await spotify_scraper_handler(
        username=username,
        password=password,
        country_codes=country_codes,
        start_date=start_date,
        save_path=save_path,
    )

    # Parse and save the data
    parse_save_path = save_path.replace(".json", "_parsed.json")
    parse_data = parse_and_save_spotify_charts_data(collected_data, parse_save_path)

    return {"status": "success", "data_saved_to": save_path, "data parsed": parse_data}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=3002)
