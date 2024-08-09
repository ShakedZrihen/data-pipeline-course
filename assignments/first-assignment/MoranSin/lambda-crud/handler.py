from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/", status_code=200)
def root():
    return "first assignment by MoranSin"

@app.get("/health", status_code=200)
def health_code():
    return 200

handler = Mangum(app)