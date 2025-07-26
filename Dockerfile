FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir -r requirements.txt
CMD ["runpod", "start", "--handler", "handler.handler"]
