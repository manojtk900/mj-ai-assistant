import webbrowser
import datetime
import os
import wikipedia
import pywhatkit
from speak import speak
from ai_brain import ask_ai
from memory import save_memory, get_memory
from vision import detect_objects
from textblob import TextBlob


def execute(command):

    command = command.replace("jarvi", "").lower().strip()

    # 🎬 YOUTUBE
    if "youtube" in command:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")
        return "Opening YouTube"

    # 🌐 GOOGLE
    elif "google" in command:
        webbrowser.open("https://google.com")
        speak("Opening Google")
        return "Opening Google"

    # 💻 VS CODE
    elif "vscode" in command:
        os.system("code")
        speak("Opening VS Code")
        return "Opening VS Code"

    # 🌍 CHROME
    elif "chrome" in command:
        os.system("start chrome")
        speak("Opening Chrome")
        return "Opening Chrome"

    # ⏰ TIME
    elif "time" in command:
        time_now = datetime.datetime.now().strftime("%H:%M")
        speak("Current time is " + time_now)
        return time_now

    # 🎵 MUSIC
    elif "play music" in command:
        pywhatkit.playonyt("lofi music")
        speak("Playing music")
        return "Playing music"

    # 📌 AUTO MEMORY (smart)
    elif "exam" in command or "tomorrow" in command:
        save_memory("note", command)
        speak("Saved your reminder")
        return f"Saved: {command}"

    # 📚 WIKIPEDIA
    elif "wikipedia" in command:
        speak("Searching Wikipedia")
        topic = command.replace("wikipedia", "").strip()

        if topic == "":
            speak("What should I search?")
            return "No topic"

        result = wikipedia.summary(topic, sentences=2)
        speak(result)
        return result

    # ⚡ SHUTDOWN
    elif "shutdown" in command:
        speak("Shutting down the system")
        os.system("shutdown /s /t 1")
        return "Shutting down"

    # 💾 MEMORY SAVE (manual)
    elif "remember" in command or "remind" in command:
        data = (
            command.replace("remember", "")
                   .replace("remind", "")
                   .replace("me", "")
                   .strip()
        )

        if data == "":
            speak("What should I remember?")
            return "No memory given"

        save_memory("note", data)
        speak("Got it, I will remember that")
        return f"Saved: {data}"

    # 🧠 MEMORY RECALL
    elif "what did i say" in command:
        memory = get_memory("note")
        speak(memory)
        return memory

    # 👁 CAMERA
    elif "camera" in command:
        speak("Opening camera")
        open_camera()
        return "Camera opened"

    # 🧠 AI
    elif "explain" in command or "what is" in command:
        if len(command.split()) < 2:
            speak("Please say what you want me to explain")
            return "No topic"

        speak("Thinking...")
        answer = ask_ai(command)
        speak(answer)
        return answer

    elif "what do you see" in command or "vision" in command:
        speak("Opening vision system")
        objects = detect_objects()
    
        if objects:
             speak(f"I can see {', '.join(objects[:3])}")
             return f"Detected: {objects}"
        else:
             speak("I couldn't detect anything")
             return "No objects"

    elif "what is" in command or "explain" in command:

        blob = TextBlob(command)
        polarity = blob.sentiment.polarity

        if polarity < 0:
            speak("You sound a bit upset. Let me help.")
        elif polarity > 0:
            speak("You seem in a good mood!")

        answer = ask_ai(command)
        speak(answer)
        return answer


    # 🤖 FALLBACK AI
    else:
        speak("Let me think")
        answer = ask_ai(command)
        speak(answer)
        return answer
