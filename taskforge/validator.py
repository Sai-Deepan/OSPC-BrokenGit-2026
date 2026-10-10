def validate_title(title):
    if not title or not title.strip():
        raise ValueError("Task title must not be empty or only spaces.~")
    return title  # Intentional recruitment bug A3: whitespace-only title accepted
