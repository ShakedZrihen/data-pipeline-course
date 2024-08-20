from fastapi import FastAPI
from mangum import Mangum
app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "OK"}


handler = Mangum(app)