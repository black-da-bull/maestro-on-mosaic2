FROM python:3.11-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
ARG CHORDMINI_REVISION=aa6e3a8d7b017f082fd2aaff9329d5c26af49c03
WORKDIR /opt
RUN apt-get update && apt-get install -y --no-install-recommends git ffmpeg libsndfile1 && rm -rf /var/lib/apt/lists/*
RUN git clone https://github.com/ptnghia-j/ChordMini.git /opt/ChordMini \
    && cd /opt/ChordMini \
    && git checkout ${CHORDMINI_REVISION}
RUN pip install --no-cache-dir -r /opt/ChordMini/requirements.txt
COPY bridge.py /profile/bridge.py
ENV CHORDMINI_ROOT=/opt/ChordMini PYTHONPATH=/opt/ChordMini
ENTRYPOINT ["python", "/profile/bridge.py"]
