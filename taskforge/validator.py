def validate_title(title):
    if not isinstance(title, str) or not title.strip(): #Updated 
        raise ValueError("Task title must not be empty")
    return title  # Intentional recruitment bug A3: whitespace-only title accepted
