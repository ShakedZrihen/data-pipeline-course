import time
import requests
from fastapi import FastAPI

LAMBDA_CRUD_URL = "http://lambda-crud:8001/processMessages"
app = FastAPI()
data = {}
reset_counter = 0


def trigger_lambda_crud():
    while True:
        try:
            response = requests.post(LAMBDA_CRUD_URL)
            response_data = response.json()
            global data
            data.update(response_data)
            if len(data) > 500:
                data = {}
                reset_counter += 1
            print(f"Triggered lambda-crud: {response.status_code}, {response.json()}")
        except Exception as e:
            print(f"Error triggering lambda-crud: {e}")
        time.sleep(60)  # Wait for 60 seconds before triggering again


@app.on_event("startup")
async def startup_event():
    from threading import Thread

    Thread(target=trigger_lambda_crud).start()


@app.get("/health")
def health_check():
    return {"status": "OK", "amount of time triggered": len(data) + reset_counter * 500}
