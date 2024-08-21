import fastapi
from mangum import Mangum

app = fastapi.FastAPI()

@app.get("/health")
def health():
    return {"message": "Im alive"}

handler = Mangum(app)
