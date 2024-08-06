from fastapi import FastAPI
from magnum import Mangum
app=FastAPI()
@app.get("/health")
def health():
    return 200

handler=Mangum(app)