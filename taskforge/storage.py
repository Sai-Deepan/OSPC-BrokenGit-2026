import json
from pathlib import Path

DEFAULT_PATH = Path("tasks.json")

def save_tasks(tasks, path=DEFAULT_PATH):
    path = Path(path)
    if path.parent and not path.parent.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)
    return len(tasks)

def load_tasks(path=DEFAULT_PATH):
    path = Path(path)
    if not path.is_file() or path.stat().st_size == 0:
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

