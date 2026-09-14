FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
ARG TSUMUGI_REVISION=f7411471a4de0ad3d430191de11b8623d67e5b38
WORKDIR /opt
RUN apt-get update && apt-get install -y --no-install-recommends git ffmpeg libsndfile1 curl && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir uv
RUN git clone https://github.com/anime-song/tsumugi.git /opt/tsumugi \
    && cd /opt/tsumugi \
    && git checkout ${TSUMUGI_REVISION}
RUN cd /opt/tsumugi && uv sync --locked
WORKDIR /app
COPY requirements-core.txt ./
RUN pip install --no-cache-dir -r requirements-core.txt
COPY worker_core.py service.py artifact_sync.py ingest.py probe.py ./
COPY profiles/tsumugi/bridge.py /profile/bridge.py
ENV TSUMUGI_ROOT=/opt/tsumugi \
    TSUMUGI_REVISION=${TSUMUGI_REVISION} \
    MAESTRO_ADVANCED_AMT_COMMAND_JSON='["/opt/tsumugi/.venv/bin/python","/profile/bridge.py","--input","{input}","--output","{output}","--context","{context}"]'
RUN useradd -r -u 10001 maestro && mkdir -p /data/artifacts /data/state /models && chown -R maestro:maestro /data /models
USER maestro
EXPOSE 8080
CMD ["uvicorn", "service:app", "--host", "0.0.0.0", "--port", "8080"]
