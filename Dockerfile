FROM python:3.10-alpine

# install dependencies
RUN apk add build-base libffi-dev openssl-dev

# too lazy to do a dotenv properly
RUN pip install 'poetry==1.4.0'

WORKDIR /app

# install dependencies
COPY poetry.lock pyproject.toml /app/
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --only main --no-interaction --no-ansi

# copy project
COPY alles_dlp /app/alles_dlp

VOLUME [ "/app/cookies" ]

EXPOSE 8000

# copy entrypoint.sh
COPY start.sh /app/start.sh

# entry
ENTRYPOINT ["/bin/sh"]
CMD ["/app/start.sh"]
