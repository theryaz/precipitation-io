FROM arm64v8/python:3.11-alpine

WORKDIR /app

COPY . .

ENTRYPOINT [ "python", "rain_barrels/app.py"]