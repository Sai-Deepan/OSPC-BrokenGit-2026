import json
from pathlib import Path
DEFAULT_PATH = Path("tasks.json")
def save_tasks(tasks, path=DEFAULT_PATH):
    path = Path(path)
    with path.open("w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)
    return len(tasks)
def load_tasks(path=DEFAULT_PATH):
    path = Path(path)
    if not path.exists():
        return []
    try:
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"Could not read tasks from '{path}': the file is not valid JSON "
            f"(line {exc.lineno}, column {exc.colno}). "
            "Fix the file or delete it to start fresh."
        ) from exc
    if not isinstance(data, list) or not all(isinstance(t, dict) for t in data):
        raise ValueError(
            f"Could not read tasks from '{path}': expected a JSON list of task objects. "
            "Fix the file or delete it to start fresh."
        )
    return data
    
