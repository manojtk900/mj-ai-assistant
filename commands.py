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

    command = command.lower().strip()

    # 🔥 CLOSE COMMANDS FIRST
    if "close youtube" in command:
        os.system("taskkill /im chrome.exe /f")
        speak("Closing YouTube")
        return "Closed YouTube"

    elif "close chrome" in command:
        os.system("taskkill /im chrome.exe /f")
        speak("Closing Chrome")
        return "Closed Chrome"

    elif "close vscode" in command:
        os.system("taskkill /im Code.exe /f")
        speak("Closing VS Code")
        return "Closed VS Code"

    # 🌐 OPEN COMMANDS
    elif "youtube" in command:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")
        return "Opening YouTube"

    elif "google" in command:
        webbrowser.open("https://google.com")
        speak("Opening Google")
        return "Opening Google"

    elif "open chrome" in command:
        os.system("start chrome")
        speak("Opening Chrome")
        return "Opening Chrome"

    elif "open vscode" in command:
        os.system("code")
        speak("Opening VS Code")
        return "Opening VS Code"

    # ⏰ TIME
    elif "time" in command:
        time_now = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {time_now}")
        return time_now

    # 🎵 MUSIC
    elif "play music" in command:
        pywhatkit.playonyt("lofi music")
        speak("Playing music")
        return "Playing music"

    # 💾 MEMORY
    elif "exam" in command or "tomorrow" in command:
        save_memory("note", command)
        speak("Saved your reminder")
        return command

    elif "remember" in command or "remind" in command:
        data = command.replace("remember", "").replace("remind", "").replace("me", "").strip()

        if not data:
            speak("What should I remember?")
            return "No memory"

        save_memory("note", data)
        speak("Got it, I will remember that")
        return data

    elif "what did i say" in command:
        memory = get_memory("note")
        speak(memory)
        return memory

    # 👁 VISION
    elif "vision" in command or "what do you see" in command:
        speak("Opening vision system")
        objects = detect_objects()
        return str(objects)

    # 📚 WIKI
    elif "wikipedia" in command:
        topic = command.replace("wikipedia", "").strip()

        if not topic:
            speak("What should I search?")
            return "No topic"

        result = wikipedia.summary(topic, sentences=2)
        speak(result)
        return result

    # 🤖 AI
    else:
        blob = TextBlob(command)
        polarity = blob.sentiment.polarity

        if polarity < -0.3:
            speak("You sound stressed Manoj")
        elif polarity > 0.3:
            speak("You sound excited")

        speak("Thinking...")
        answer = ask_ai(command)
        speak(answer)
        return answer
