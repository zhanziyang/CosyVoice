import os, uvicorn, base64, tempfile
from fastapi import FastAPI, HTTPException, Header
from cosyvoice import CosyVoice

EXPECTED_KEY = os.getenv("TTS_API_KEY")
cosy = CosyVoice(os.getenv("MODEL_DIR", "iic/CosyVoice-300M"))

app = FastAPI()

@app.post("/synthesize")
def tts(input: dict, x_api_key: str | None = Header(None)):
    if EXPECTED_KEY and x_api_key != EXPECTED_KEY:
        raise HTTPException(status_code=401, detail="unauthorized")
    text   = input["text"]
    voice  = input.get("voice", "中文女")
    stream = cosy.inference_sft(text, voice, stream=False)
    wav = b"".join([chunk["tts_speech"].cpu().numpy().tobytes() for chunk in stream])
    return {"audio": base64.b64encode(wav).decode()}

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=50000)