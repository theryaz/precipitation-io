FROM python:3.10-slim-bullseye

WORKDIR /app

RUN apt-get update && apt-get install build-essential -y
RUN apt-get install python3-rpi.gpio python3-smbus -y

RUN pip install quart

COPY . .

CMD [ "/bin/bash python /app/app.py"]