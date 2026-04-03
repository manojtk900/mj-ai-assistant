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

while True:

    gui.update_status("Listening")

    command = listen()

    # GUI typed input
    if gui.typed_command:
        command = gui.typed_command
        gui.typed_command = None

    if not command:
        continue

    command = command.lower().strip()
    print("COMMAND:", command)

    # Wake word
    if "mj" in command:
        active = True
        last_active = time.time()
        speak("Yes Manoj")

        command = command.replace("mj", "").strip()
        if command == "":
            continue

    if not active:
        continue

    if "stop" in command:
        speak("Going to sleep")
        gui.update_status("Sleeping")
        active = False
        continue

    gui.update_command(command)
    gui.update_status("Processing")

    try:
        response = execute(command)

        if response:
            gui.update_response(response)

    except Exception as e:
        print("ERROR:", e)
        speak("Error occurred")

    gui.update_status("Idle")
    last_active = time.time()

    if active and (time.time() - last_active > 20):
        speak("Going to sleep")
        active = False