FROM python:3.12.0b4-slim-bullseye

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY . .

CMD [ "poetry run python rain_barrels/app.py"]