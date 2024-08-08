from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()


@app.get("/health", status_code=200)
def health():
    return


handler = Mangum(app)
