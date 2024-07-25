FROM ubuntu:latest
LABEL authors="Ron Barcochva"

RUN apt update && apt install -y python3 python3-pip python3-venv nodejs npm curl unzip
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && unzip awscliv2.zip && ./aws/install

COPY resources/ /home/ubuntu/RonBarcochva/resources/
COPY services/ /home/ubuntu/RonBarcochva/services/
COPY .env /home/ubuntu/RonBarcochva/
COPY app.py /home/ubuntu/RonBarcochva/
COPY package.json /home/ubuntu/RonBarcochva/
COPY package-lock.json /home/ubuntu/RonBarcochva/
COPY requirements.txt /home/ubuntu/RonBarcochva/
COPY serverless.yml /home/ubuntu/RonBarcochva/

WORKDIR /home/ubuntu/RonBarcochva

RUN python3 -m venv venv
RUN /bin/bash -c "source venv/bin/activate && pip install -r requirements.txt"
RUN npm install

EXPOSE 3000
CMD ["/bin/bash", "-c", "source venv/bin/activate && ./node_modules/.bin/serverless offline start"]