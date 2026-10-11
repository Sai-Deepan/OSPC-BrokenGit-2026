def search_tasks(tasks, query):
    if not isinstance(query, str):
        raise ValueError("Search query must be text")
    return [
        task for task in tasks
        if query.casefold() in task["title"].casefold()
    ]# Bug A2
