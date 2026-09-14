FROM python:3.11-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends ffmpeg libsndfile1 && rm -rf /var/lib/apt/lists/*
COPY requirements-core.txt ./
RUN pip install --no-cache-dir -r requirements-core.txt 'basic-pitch==0.4.0'
COPY worker_core.py service.py artifact_sync.py ingest.py probe.py ./
COPY profiles/basic-pitch/bridge.py /profile/bridge.py
RUN useradd -r -u 10001 maestro && mkdir -p /data/artifacts /data/state && chown -R maestro:maestro /data
USER maestro
EXPOSE 8080
CMD ["uvicorn", "service:app", "--host", "0.0.0.0", "--port", "8080"]
