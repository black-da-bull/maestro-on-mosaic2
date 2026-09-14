FROM python:3.10-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
ARG SONGFORMER_REVISION=139b2aa3b14bd1c6d961d0994e9fc975f1ef7fd5
WORKDIR /opt
RUN apt-get update && apt-get install -y --no-install-recommends git ffmpeg libsndfile1 && rm -rf /var/lib/apt/lists/*
RUN git clone --recursive https://github.com/ASLP-lab/SongFormer.git /opt/SongFormer \
    && cd /opt/SongFormer \
    && git checkout ${SONGFORMER_REVISION} \
    && git submodule update --init --recursive
RUN pip install --no-cache-dir -r /opt/SongFormer/requirements.txt
COPY bridge.py /profile/bridge.py
ENV PYTHONPATH=/opt/SongFormer
ENTRYPOINT ["python", "/profile/bridge.py"]
