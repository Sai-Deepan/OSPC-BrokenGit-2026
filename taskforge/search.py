def search_tasks(tasks, query):
    if not isinstance(query, str):
        raise ValueError("Search query must be text")
    query_lower = query.lower()
    return [task for task in tasks if query_lower in task["title"].lower()]

