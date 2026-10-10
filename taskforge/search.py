def search_tasks(tasks, query):
    if not isinstance(query, str):
        raise ValueError("Search query must be text")
    query = query.casefold()
    return [task for task in tasks if query in task["title"].casefold()]
