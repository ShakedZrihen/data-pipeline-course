from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
from db_manager import DBManager
import json
import logging

# Database connection URL
DATABASE_URL = "postgresql://user:password@postgres/mydb"
db_manager = DBManager(DATABASE_URL)

app = FastAPI()

# Add CORS middleware to allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)

@app.post("/insert-data")
def insert_data(data: dict):
    try:
        # Insert the provided data into the database
        db_manager.insert(data)
        return {"status": "Data inserted successfully"}
    except Exception as e:
        # Log the error and raise an HTTP 500 exception if insertion fails
        logging.error(f"Failed to insert data: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to insert data: {str(e)}")

@app.get("/charts")
def get_charts(date: str = Query(..., description="The date for which to retrieve the charts")):
    try:
        # Retrieve charts for the specified date from the database
        charts = db_manager.get_charts(date)
        if not charts:
            # Raise an HTTP 404 exception if no charts are found for the given date
            raise HTTPException(status_code=404, detail="No charts found for the given date")
        return {"charts": charts}
    except Exception as e:
        logging.error(f"Failed to retrieve charts: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to retrieve charts: {str(e)}")

def get_available_dates():
    try:
        # Load available dates from a JSON file
        with open('availDates.json', 'r') as file:
            dates_data = json.load(file)
        return dates_data
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="availDates.json file not found")
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Error decoding availDates.json")

@app.get("/charts/available-dates")
async def available_dates():
    # Return the list of available dates for chart data
    return get_available_dates()

handler = Mangum(app)