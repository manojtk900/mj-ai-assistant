import subprocess

chat_history = []

def ask_ai(question):

    global chat_history

    system_prompt = """
You are MJ, a smart AI assistant like Iron Man's Jarvis.

Rules:
- Speak naturally like a human assistant
- Be short, clear, and confident
- Slightly witty but respectful
- Address user as Manoj sometimes
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

    chat_history.append(f"MJ: {response}")

    return response
