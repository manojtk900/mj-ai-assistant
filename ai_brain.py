import subprocess

chat_history = []

def ask_ai(question):

    global chat_history

    # 🧠 Personality prompt
    system_prompt = """
You are JARVIS, a smart, slightly witty, helpful AI assistant.
You speak like a calm, intelligent female assistant.
Keep answers short, natural, and friendly.
Sometimes add light emotion (like: "Sure!", "Of course!", "Alright!")
Do NOT be robotic.
"""

    chat_history.append(f"User: {question}")

    prompt = system_prompt + "\n" + "\n".join(chat_history[-6:])

    result = subprocess.run(
        ["ollama", "run", "gemma:2b", prompt],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="ignore"
    )

    response = result.stdout.strip()

    chat_history.append(f"Jarvis: {response}")

    return response