FROM python:3
LABEL authors="Yinon Maman"

RUN apt update && apt install -y nodejs npm curl unzip
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && unzip awscliv2.zip && ./aws/install

WORKDIR /usr/src/YinonMaman

COPY resource/ resource/
COPY services/ services/
COPY config.py .
COPY app.py .
COPY package.json .
COPY package-lock.json .
COPY requirement.txt .
COPY serverless.yml .

RUN pip install -r requirement.txt
RUN npm install

EXPOSE 3000
CMD ["/bin/bash", "-c", "./node_modules/.bin/serverless offline start"]