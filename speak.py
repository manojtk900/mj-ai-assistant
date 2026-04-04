import asyncio
import edge_tts
from playsound import playsound
import os

VOICE = "en-IN-NeerjaNeural"  # 🔥 Female Indian voice


async def generate_audio(text, file="voice.mp3"):
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(file)


def speak(text):
    print("MJ:", text)

    try: 
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(generate_audio(text))
        playsound("voice.mp3")

        # cleanup
        os.remove("voice.mp3")

    except Exception as e:
        print("Voice Error:", e)
