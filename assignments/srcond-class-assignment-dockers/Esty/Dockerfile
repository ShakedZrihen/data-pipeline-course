FROM python:3
LABEL authors="estybrandes"

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

