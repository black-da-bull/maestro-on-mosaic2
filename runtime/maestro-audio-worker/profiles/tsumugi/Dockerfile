FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
ARG TSUMUGI_REVISION=f7411471a4de0ad3d430191de11b8623d67e5b38
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends git ffmpeg libsndfile1 curl && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir uv
COPY requirements-core.txt /app/requirements-core.txt
RUN git clone https://github.com/anime-song/tsumugi.git /opt/tsumugi \
    && cd /opt/tsumugi \
    && git checkout ${TSUMUGI_REVISION}
RUN cd /opt/tsumugi && uv sync --locked \
    && uv pip install --python /opt/tsumugi/.venv/bin/python -r /app/requirements-core.txt
COPY worker_core.py service.py artifact_sync.py ingest.py probe.py /app/
COPY profiles/tsumugi/bridge.py /profile/bridge.py
ENV TSUMUGI_ROOT=/opt/tsumugi \
    TSUMUGI_REVISION=${TSUMUGI_REVISION} \
    TSUMUGI_CHECKPOINT=/models/tsumugi/model.pt \
    MAESTRO_ADVANCED_AMT_COMMAND_JSON='["/opt/tsumugi/.venv/bin/python","/profile/bridge.py","--input","{input}","--output","{output}","--context","{context}"]'
RUN useradd -r -u 10001 maestro \
    && mkdir -p /data/artifacts /data/state /models/tsumugi \
    && chown -R maestro:maestro /data /models
USER maestro
WORKDIR /app
EXPOSE 8080
CMD ["/opt/tsumugi/.venv/bin/python", "-m", "uvicorn", "service:app", "--host", "0.0.0.0", "--port", "8080"]
