FROM python:3.12.0b4-slim-bullseye

WORKDIR /app

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

COPY . .

CMD [ "/usr/local/bin/python app.py"]