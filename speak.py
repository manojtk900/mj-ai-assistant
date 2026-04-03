import pyttsx3
import threading

engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Female voice
engine.setProperty('voice', voices[1].id if len(voices) > 1 else voices[0].id)
engine.setProperty('rate', 170)

lock = threading.Lock()

def speak(text):
    print("MJ:", text)

    def run():
        with lock:
            engine.say(text)
            engine.runAndWait()

    threading.Thread(target=run).start()