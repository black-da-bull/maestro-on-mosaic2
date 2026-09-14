FROM python:3.10-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends ffmpeg libsndfile1 && rm -rf /var/lib/apt/lists/*
COPY requirements-core.txt ./
RUN pip install --no-cache-dir -r requirements-core.txt \
    && python -m venv /opt/clap-venv \
    && /opt/clap-venv/bin/pip install --no-cache-dir 'laion-clap==1.1.7'
COPY worker_core.py service.py artifact_sync.py ingest.py probe.py ./
COPY profiles/clap/bridge.py /profile/bridge.py
ENV CLAP_CHECKPOINT=/models/clap/model.pt \
    MAESTRO_CLAP_COMMAND_JSON='["/opt/clap-venv/bin/python","/profile/bridge.py","--input","{input}","--output","{output}","--context","{context}"]'
RUN useradd -r -u 10001 maestro && mkdir -p /data/artifacts /data/state /models/clap && chown -R maestro:maestro /data /models
USER maestro
EXPOSE 8080
CMD ["uvicorn", "service:app", "--host", "0.0.0.0", "--port", "8080"]
