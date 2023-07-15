FROM python:3.12.0b4-slim-bullseye

WORKDIR /app

RUN pip install quart

COPY . .

CMD [ "python rain_barrels/app.py"]