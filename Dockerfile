FROM python:3.9-slim

RUN apt-get update

COPY main.py /app/main.py

WORKDIR /app

CMD ["python", "main.py", "4", "3"]