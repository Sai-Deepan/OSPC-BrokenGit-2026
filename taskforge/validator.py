
def validate_title(title):
    if not isinstance(title, str) or not title:
        raise ValueError("Task title must not be empty")
    return title  # Intentional recruitment bug A3 remains unchanged


def validate_priority(priority):
    allowed_priorities = {"low", "medium", "high"}

    if not isinstance(priority, str) or priority not in allowed_priorities:
        raise ValueError(
            "Priority must be one of: low, medium, high"
        )

    return priority
