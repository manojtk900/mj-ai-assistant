from listen import listen
from commands import execute
from speak import speak
import threading
import time
import gui

# Start GUI
threading.Thread(target=gui.start_gui, daemon=True).start()

speak("MJ is online")

active = False
last_active = time.time()
TIMEOUT = 60

processing = False


def process_command(command):
    global processing, last_active

    try:
        gui.update_status("Thinking")

        response = execute(command)

        if response:
            gui.update_response(response)

    except Exception as e:
        print("ERROR:", e)
        speak("Something went wrong")

    gui.update_status("Idle")
    processing = False
    last_active = time.time()


while True:

    gui.update_status("Listening")

    command = listen()

    # GUI typing
    if gui.typed_command:
        command = gui.typed_command
        gui.typed_command = None

    if not command:
        continue

    command = command.lower().strip()
    print("COMMAND:", command)

    # ignore noise
    if len(command.split()) < 2:
        continue

    # 🎤 wake word
    if any(word in command for word in ["mj", "m j", "emjay", "sanjay"]):
        active = True
        last_active = time.time()
        speak("Yes Manoj")

        command = command.replace("mj", "").replace("sanjay", "").strip()
        if not command:
            continue

    if not active:
        continue

    # 🛑 stop
    if "stop" in command:
        speak("Going to sleep Manoj")
        gui.update_status("Sleeping")
        active = False
        continue

    # ⏳ prevent overlap
    if processing:
        speak("One moment Manoj")
        continue

    processing = True

    gui.update_command(command)
    gui.update_status("Processing")

    threading.Thread(
        target=process_command,
        args=(command,),
        daemon=True
    ).start()

    # 🔥 FIXED timeout (correct logic)
    if active and (time.time() - last_active > TIMEOUT):
        speak("Going to sleep due to inactivity")
        active = False
