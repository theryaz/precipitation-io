FROM alexberkovich/alpine-python39:0.4.0

WORKDIR /app

COPY . .

CMD [ "python", "rain_barrels/app.py"]