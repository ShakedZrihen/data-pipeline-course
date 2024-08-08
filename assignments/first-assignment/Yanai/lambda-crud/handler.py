from fastapi import FastAPI, Response, status

from typing import Optional


app = FastAPI()

@app.get("/health")
async def health():
    return {"status": "OK"}

