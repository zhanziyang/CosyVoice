FROM nvidia/cuda:12.2.0-runtime-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y git python3-pip && rm -rf /var/lib/apt/lists/*

# --- pull CosyVoice ---
RUN git clone --depth 1 https://github.com/FunAudioLLM/CosyVoice /opt/CosyVoice
WORKDIR /opt/CosyVoice

# Use only what we need
COPY deploy/fastapi/requirements.txt /tmp/req.txt
RUN pip install --no-cache-dir -r /tmp/req.txt

COPY deploy/fastapi/server.py /opt/CosyVoice/

# expose FastAPI
EXPOSE 50000
CMD ["python3", "server.py"]