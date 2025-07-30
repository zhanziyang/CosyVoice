import base64, io, os, runpod
from cosyvoice import CosyVoice           # model code

# ---- model loads once per container ----
MODEL_DIR = os.getenv("MODEL_DIR", "iic/CosyVoice-300M")
cosy = CosyVoice(MODEL_DIR)

def handler(job):
    """Runpod standard handler → returns base64 WAV."""
    ip = job["input"]
    text  = ip["text"]
    voice = ip.get("voice", "中文女")
    stream = cosy.inference_sft(text, voice, stream=False)
    wav_bytes = b"".join([c["tts_speech"].cpu().numpy().tobytes() for c in stream])
    return {"audio": base64.b64encode(wav_bytes).decode()}

if __name__ == "__main__":
    runpod.serverless.start({"handler": handler})
