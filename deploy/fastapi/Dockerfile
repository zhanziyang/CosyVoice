FROM nvidia/cuda:12.4.1-runtime-ubuntu22.04 

RUN apt-get update && apt-get install -y \
    python3 python3-pip git git-lfs ffmpeg sox libsox-dev \
    && rm -rf /var/lib/apt/lists/* \
    && git lfs install

WORKDIR /app
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY rp_handler.py .

ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH="$PYTHONPATH:/app"

CMD ["python3", "-u", "rp_handler.py"]
