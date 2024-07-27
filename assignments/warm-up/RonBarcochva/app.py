from fastapi import FastAPI, Response, status
from mangum import Mangum
from typing import Optional
from services.news import get_breaking_news
from services.db import init
import uvicorn


app = FastAPI()
init()


@app.get("/health", status_code=200)
def health():
    return


@app.get("/breaking-news", status_code=200)
def breaking_news(response: Response, date: Optional[str] = None, time: Optional[str] = None):
    breaking_news_data = get_breaking_news(date)
    if not breaking_news_data:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "No breaking news found"}
    if not date and time:
        for date_news in [item for item in breaking_news_data]:
            breaking_news_data[date_news] = {key: value for key, value in breaking_news_data[date_news].items() if
                                             time in key}
            if not breaking_news_data[date_news]:
                del breaking_news_data[date_news]
    elif time:
        breaking_news_data = {key: value for key, value in breaking_news_data.items() if time in key}
    if not breaking_news_data:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "No breaking news found"}
    return breaking_news_data


handler = Mangum(app)


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8002)
