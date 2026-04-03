import json
import os

# Absolute path (THIS FIXES EVERYTHING)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.join(BASE_DIR, "data", "memory.json")


def save_memory(key, value):

    os.makedirs(os.path.dirname(FILE), exist_ok=True)

    try:
        with open(FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    except:
        data = {}

    data[key] = value

    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print("💾 Saved to:", FILE)     # 🔥 IMPORTANT DEBUG
    print("💾 Data:", data)


def get_memory(key):

    try:
        with open(FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data.get(key, "I don't remember anything")

    except:
        return "Memory is empty"