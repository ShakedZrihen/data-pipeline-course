from fastapi import FastAPI, HTTPException
from mangum import Mangum
from services.get_data import Get_Data, query_all, query_date, query_time, query_date_time

app = FastAPI()


@app.get("/")
def root():
    return {"status": 200}


@app.get("/health")
def health():
    return {"status": "ok",
            "massage": "200"}


@app.get("/breaking-news", status_code=200)
def breaking_news(date=None, time=None):
    db = Get_Data()
    if date is not None and time is not None:  # if user send date and time
        return query_date_time(db, date, time)
    if date is None and time is not None:  # if user send time
        return query_time(db, time)
    elif time is None and date is not None:  # if user send date
        return query_date(db, date)
    else:  # if user didnt send
        return query_all(db)


@app.get("/{path_name:path}")
def catch_all(path_name: str):
    raise HTTPException(status_code=404, detail=f"{path_name} Not Found")


handler = Mangum(app)
