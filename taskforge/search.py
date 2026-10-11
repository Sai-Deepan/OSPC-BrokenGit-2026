def search_tasks(tasks, query):
    if not isinstance(query, str):
        raise ValueError("Search query must be text")
    return [task for task in tasks if query.lower() in task["title"].lower()]  # Bug A2 , Updated ".lower()" this makes sure that both of them are in lowercases so all case varients will be considerd
