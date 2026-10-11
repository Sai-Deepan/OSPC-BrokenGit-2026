import json
from pathlib import Path
import os

DEFAULT_PATH = Path("tasks.json")

def save_tasks(tasks, path=DEFAULT_PATH):
    with open(path, "w", encoding="utf-8") as f:
            json.dump(tasks, f, indent=4)
    return len(tasks)

def load_tasks(path=DEFAULT_PATH):
    if not os.path.exists(path):
            return []
    try:
        with open(path, "r", encoding="utf-8") as f:
            r = f.read().strip()
            if not r:
                return []
            return json.loads(r)
    except json.JSONDecodeError as e:
        raise ValueError(
            f"Error: '{path}' contains malformed JSON. "
            f"Fix the file. Details: {e}"
        )
    
