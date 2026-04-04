import queue
import sounddevice as sd
import json
import os
from vosk import Model, KaldiRecognizer

q = queue.Queue()

# ✅ Correct model path
MODEL_PATH = "vosk_model/vosk-model-small-en-in-0.4"

if not os.path.exists(MODEL_PATH):
    raise Exception("❌ Model path not found!")

# ✅ Load model ONLY ONCE
model = Model(MODEL_PATH)
recognizer = KaldiRecognizer(model, 16000)


def callback(indata, frames, time, status):
    if status:
        print("⚠️ Mic status:", status)
    q.put(bytes(indata))


def listen():
    print("🎤 Listening (offline)...")

    with sd.RawInputStream(
        samplerate=16000,
        blocksize=8000,
        dtype='int16',
        channels=1,
        callback=callback
    ):

        while True:
            data = q.get()

            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                text = result.get("text", "").strip()

                # 🔥 filter noise
                if len(text) < 2:
                    return ""

                print("🗣 You said:", text)
                return text.lower()