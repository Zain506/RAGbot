FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y git && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./

# Upgrade pip first, then install dependencies without cache
RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
