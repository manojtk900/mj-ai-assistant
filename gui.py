import tkinter as tk
import math

# 🧠 Shared state
state = {
    "command": "...",
    "response": "...",
    "status": "Idle"
}

typed_command = None  # 🔥 shared typing


def update_command(cmd):
    state["command"] = cmd

def update_response(res):
    state["response"] = res

def update_status(status):
    state["status"] = status


def start_gui():
    global typed_command

    root = tk.Tk()
    root.title("MJ AI Assistant")
    root.geometry("700x600")
    root.configure(bg="black")

    # TITLE
    tk.Label(root, text="MJ", font=("Arial", 36, "bold"),
             fg="#00ffff", bg="black").pack(pady=10)

    status_label = tk.Label(root, text="Status: Idle",
                            fg="#00ffcc", bg="black")
    status_label.pack()

    command_label = tk.Label(root, text="Command: ---",
                             fg="white", bg="black")
    command_label.pack()

    response_label = tk.Label(root, text="Response: ---",
                              fg="#ffff66", bg="black",
                              wraplength=600)
    response_label.pack(pady=10)

    canvas = tk.Canvas(root, width=300, height=300,
                       bg="black", highlightthickness=0)
    canvas.pack()

    circle = canvas.create_oval(50, 50, 250, 250,
                               outline="#00ffff", width=2)

    angle = 0

    def animate():
        nonlocal angle
        angle += 0.1

        glow = 20 + int(10 * math.sin(angle))

        canvas.coords(circle, 50-glow, 50-glow, 250+glow, 250+glow)

        root.after(50, animate)

    # ⌨️ INPUT
    entry = tk.Entry(root, width=40)
    entry.pack(pady=10)

    def send_text():
        global typed_command
        cmd = entry.get().lower().strip()

        if cmd:
            typed_command = cmd
            update_command(cmd)

        entry.delete(0, tk.END)

    tk.Button(root, text="Type Command",
              command=send_text,
              bg="#00ffff").pack()

    def update_labels():
        status_label.config(text=f"Status: {state['status']}")
        command_label.config(text=f"Command: {state['command']}")
        response_label.config(text=f"Response: {state['response']}")

        root.after(200, update_labels)

    tk.Button(root, text="EXIT", command=root.destroy,
              bg="red", fg="white").pack(pady=10)

    animate()
    update_labels()

    root.mainloop()