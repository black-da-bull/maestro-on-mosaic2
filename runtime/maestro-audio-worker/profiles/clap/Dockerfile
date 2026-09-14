FROM python:3.10-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /profile
RUN apt-get update && apt-get install -y --no-install-recommends ffmpeg libsndfile1 && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir 'laion-clap==1.1.7'
COPY bridge.py /profile/bridge.py
ENTRYPOINT ["python", "/profile/bridge.py"]
