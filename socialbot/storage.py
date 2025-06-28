import os
import json
from datetime import datetime

HISTORY_DIR = "chat_history"
os.makedirs(HISTORY_DIR, exist_ok=True)

def _safe_filename(name):
    return "".join(c for c in name if c.isalnum() or c in ('-', '_')).rstrip()

def save_user_message(user_name: str, message: str, response: str):
    timestamp = datetime.now().isoformat()
    safe_name = _safe_filename(user_name.lower())
    history_path = os.path.join(HISTORY_DIR, f"{safe_name}.json")

    if os.path.exists(history_path):
        with open(history_path, "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append({
        "timestamp": timestamp,
        "prompt": message,
        "response": response
    })

    with open(history_path, "w") as f:
        json.dump(data, f, indent=2)

def load_user_history(user_name: str):
    safe_name = _safe_filename(user_name.lower())
    history_path = os.path.join(HISTORY_DIR, f"{safe_name}.json")
    if os.path.exists(history_path):
        with open(history_path, "r") as f:
            return json.load(f)
    return []
