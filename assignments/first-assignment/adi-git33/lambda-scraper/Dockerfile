FROM python:3

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD [ "uvicorn", "handler:app", "--host", "0.0.0.0", "--port", "8000" ]