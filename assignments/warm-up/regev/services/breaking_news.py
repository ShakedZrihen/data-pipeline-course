import logging
from fastapi import HTTPException
from services.db import get as get_from_db

logger = logging.getLogger(__name__)

def get_breaking_news(date: str = None, time: str = None):
    data = get_from_db()
    logger.debug(f"Fetched data: {data.keys()}")  # Log all available dates at debug level
    
    if date and time:
        logger.debug(f"Filtering data by date: {date} and time: {time}")
        if date in data:
            if time in data[date]:
                response = data[date][time]
                logger.info(f"Data for date {date} and time {time}: {response}")
                return {date: {time: response}}
            else:
                logger.warning(f"No data found for date: {date} and time: {time}")
                raise HTTPException(status_code=404, detail="News not found")
        else:
            logger.warning(f"No data found for date: {date}")
            raise HTTPException(status_code=404, detail="News not found")

    if date:
        logger.debug(f"Filtering data by date: {date}")
        if date in data:
            response = data[date]
            logger.info(f"Data for date {date}: {response}")
            return {date: response}
        else:
            logger.warning(f"No data found for date: {date}")
            raise HTTPException(status_code=404, detail="News not found")

    if time:
        logger.debug(f"Filtering data by time: {time}")
        filtered_news = {
            d: {time: news[time]} for d, news in data.items() if time in news
        }
        if filtered_news:
            logger.info(f"Filtered data for time {time}: {filtered_news}")
            return filtered_news
        else:
            logger.warning(f"No data found for time: {time}")
            raise HTTPException(status_code=404, detail="News not found")

    logger.info(f"Returning all data")
    return data
