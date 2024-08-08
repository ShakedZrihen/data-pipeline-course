FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN ls -l /app 

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "handler:app", "--host", "0.0.0.0", "--port", "8000"]
