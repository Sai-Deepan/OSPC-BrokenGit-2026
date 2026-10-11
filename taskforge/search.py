def search_tasks(tasks, query):
    query_lower = query.lower()
    if not isinstance(query, str):
        raise ValueError("Search query must be text")
    return [task for task in tasks if query in task["title"] and query_lower in str(task['title']).lower()]  # Bug A2
