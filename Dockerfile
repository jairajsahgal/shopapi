FROM python:3.10.2-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY ./requirements.txt .

RUN apt-get update -y && apt-get install -y netcat && apt-get install --no-install-recommends -y -q \
    git libpq-dev python-dev build-essential libsnappy-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && pip install --upgrade pip setuptools wheel && pip install -r requirements.txt && pip install --upgrade 'sentry-sdk[django]'

COPY ./entrypoint.sh .
RUN chmod +x /code/entrypoint.sh

COPY . .

ENTRYPOINT ["/code/entrypoint.sh"]