from fastapi import FastAPI, Response, status

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/health", status_code=200)
async def health():
    return {"message": "Hi I am healthy"}


@app.get("/breaking-news")
async def breaking_news(date: str | None = None, time: str | None = None):
    if not date and not time:
        return {"hihi": "hohoho"}

