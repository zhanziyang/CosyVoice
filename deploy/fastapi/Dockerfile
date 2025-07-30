FROM nvidia/cuda:12.4.1-runtime-ubuntu22.04

# --- system + python deps ---
RUN apt-get update && apt-get install -y \
    python3 python3-pip \
    git git-lfs \
    ffmpeg sox libsox-dev \
    && rm -rf /var/lib/apt/lists/* \
    && git lfs install

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /opt

# Pull CosyVoice code
RUN git clone --depth 1 https://github.com/your-org/CosyVoice.git
WORKDIR /opt/CosyVoice

# Install runtime requirements
COPY deploy/fastapi/requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt   # note pip3

# Make CosyVoice + Matcha-TTS importable
ENV PYTHONPATH="$PYTHONPATH:/opt/CosyVoice:/opt/CosyVoice/third_party/Matcha-TTS"

# FastAPI wrapper
COPY deploy/fastapi/server.py /opt/CosyVoice/

EXPOSE 50000
CMD ["python3", "server.py"]
