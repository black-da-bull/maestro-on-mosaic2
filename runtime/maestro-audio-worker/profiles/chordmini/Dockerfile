FROM python:3.11-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
ARG CHORDMINI_REVISION=aa6e3a8d7b017f082fd2aaff9329d5c26af49c03
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends git ffmpeg libsndfile1 && rm -rf /var/lib/apt/lists/*
COPY requirements-core.txt /app/requirements-core.txt
RUN pip install --no-cache-dir -r /app/requirements-core.txt \
    && python -m venv /opt/chordmini-venv
RUN git clone https://github.com/ptnghia-j/ChordMini.git /opt/ChordMini \
    && cd /opt/ChordMini \
    && git checkout ${CHORDMINI_REVISION}
RUN /opt/chordmini-venv/bin/pip install --no-cache-dir -r /opt/ChordMini/requirements.txt
COPY worker_core.py service.py artifact_sync.py ingest.py probe.py /app/
COPY profiles/chordmini/bridge.py /profile/bridge.py
ENV CHORDMINI_ROOT=/opt/ChordMini \
    CHORDMINI_REVISION=${CHORDMINI_REVISION} \
    CHORDMINI_CHECKPOINT=/models/chordmini/model.pth \
    MAESTRO_CHORDMINI_COMMAND_JSON='["/opt/chordmini-venv/bin/python","/profile/bridge.py","--input","{input}","--output","{output}","--context","{context}"]'
RUN useradd -r -u 10001 maestro \
    && mkdir -p /data/artifacts /data/state /models/chordmini \
    && chown -R maestro:maestro /data /models
USER maestro
EXPOSE 8080
CMD ["uvicorn", "service:app", "--host", "0.0.0.0", "--port", "8080"]
