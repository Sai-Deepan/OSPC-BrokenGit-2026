def validate_title(title):
    if not isinstance(title, str) or not title:
        raise ValueError("Task title must not be empty")
    return title.strip()