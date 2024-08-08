from fastapi import FastAPI, HTTPException
from mangum import Mangum
import json
import logging

app = FastAPI()

filename = "2024-07-27"

logging.basicConfig(level=logging.INFO)

@app.get("/health")
def health():
    try:
        return 200
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error!")

@app.get("/breaking-news")
def breaking_news(date: str = None, time: str = None):
    try:
        with open(f"./{filename}.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            if date:
                if date != filename:
                    data = []
            if time:
                if time in data:
                    print(data[time])
                    data = {time: data[time]}
                else:
                    data = []
            if data == []:
                raise HTTPException(
                        status_code=404,
                        detail={"Item not found"}
                )
            obj = { f"{filename}": data }
            return obj
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        if e.status_code == 404:
            raise HTTPException(status_code=404, detail="Item not found")
        else:
            raise HTTPException(status_code=500, detail="Internal Server Error!")

handler = Mangum(app)
