from fastapi import FastAPI
from mangum import Mangum
import uvicorn

app = FastAPI()

@app.get("/health")
async def root():
    return {"message": "App is running"}

handler = Mangum(app)
