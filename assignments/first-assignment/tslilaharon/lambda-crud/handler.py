from fastapi import FastAPI
import asyncpg

app = FastAPI()

@app.get("/health")
async def health_check():
    return {"status": "OK"}

