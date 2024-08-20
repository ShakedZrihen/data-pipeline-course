import datetime
from pydantic import BaseModel, validator, Field
from typing import List, Optional


class ScraperConfig(BaseModel):
    country_codes: List[str] = ["us", "il", "gb"]
    start_date: datetime.date = Field(
        default_factory=lambda: datetime.date.today(), example="2024-08-20"
    )
    save_path: Optional[str] = "spotify_charts_data.json"
    daily_days: Optional[int] = 2
    weekly_weeks: Optional[int] = 2

    @validator("start_date", pre=True)
    def parse_start_date(cls, value):
        if isinstance(value, str):
            return datetime.datetime.strptime(value, "%Y-%m-%d").date()
        return value
