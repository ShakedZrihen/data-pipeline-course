from fastapi import FastAPI
import os
import json

app = FastAPI()
DATA = {}


def Get_Data():
    for json_file in os.listdir("data"):
        with open(f"data/{json_file}", "r") as file:
            data = json.load(file)
            DATA[json_file] = data  # add data to DATA dictionary


@app.get("/")
async def root():
    return {"message": "new new new"}


@app.get("/health/")
async def health():
    return {"status": "ok",
            "massage": "200"}


@app.get("/breaking-news/")
async def breaking_news(date=None, time=None):
    Get_Data()
    # if date is None and time is not None
    if date is None and time is not None:
        return {"message": f"data=----- time={time}"}

    # if time is None and date is not None
    elif time is None and date is not None:
        return {"message": f"data={date} time=-----"}

    # if both are not None
    else:
        return {"message": "data=----- time=-----"}


