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
COPY bridge.py /profile/bridge.py
ENV TSUMUGI_ROOT=/opt/tsumugi
WORKDIR /opt/tsumugi
ENTRYPOINT ["uv", "run", "python", "/profile/bridge.py"]
