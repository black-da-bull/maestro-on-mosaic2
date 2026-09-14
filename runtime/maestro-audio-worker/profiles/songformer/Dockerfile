FROM python:3.10-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
ARG SONGFORMER_REVISION=139b2aa3b14bd1c6d961d0994e9fc975f1ef7fd5
WORKDIR /opt
RUN apt-get update && apt-get install -y --no-install-recommends git ffmpeg libsndfile1 && rm -rf /var/lib/apt/lists/*
RUN git clone --recursive https://github.com/ASLP-lab/SongFormer.git /opt/SongFormer \
    && cd /opt/SongFormer \
    && git checkout ${SONGFORMER_REVISION} \
    && git submodule update --init --recursive
RUN pip install --no-cache-dir -r /opt/SongFormer/requirements.txt fastapi 'uvicorn[standard]'
WORKDIR /app
COPY worker_core.py service.py artifact_sync.py ingest.py probe.py ./
COPY profiles/songformer/bridge.py /profile/bridge.py
ENV PYTHONPATH=/opt/SongFormer:/app \
    SONGFORMER_REVISION=${SONGFORMER_REVISION} \
    MAESTRO_SONGFORMER_COMMAND_JSON='["python","/profile/bridge.py","--input","{input}","--output","{output}","--context","{context}"]'
RUN useradd -r -u 10001 maestro && mkdir -p /data/artifacts /data/state /models && chown -R maestro:maestro /data /models
USER maestro
EXPOSE 8080
CMD ["uvicorn", "service:app", "--host", "0.0.0.0", "--port", "8080"]
