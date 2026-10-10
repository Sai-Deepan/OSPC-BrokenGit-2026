from taskforge.search import search_tasks

def test_exact_case_search():
    tasks = [{"id": 1, "title": "Learn Python"}]
    assert len(search_tasks(tasks, "Python")) == 1
def test_1():
    tasks = [{"id": 1, "title": "Python BasIcs"}]
    assert len(search_tasks(tasks, "python baSics")) == 1
def test_2():
    tasks = [{"id": 1, "title": "python fundamentalss"}]
    assert len(search_tasks(tasks, "PYTHON")) == 1
def test_3():
    tasks = [{"id": 1, "title": "learning Python"}]
    assert len(search_tasks(tasks, "pYtHoN")) == 1
def test_4():
    tasks = [{"id": 1, "title": "LEARN Python"}]
    assert search_tasks(tasks, "ptthon") == []
def test_5():
    tasks = [{"id": 1, "title": "Learn Python"}]
    results = search_tasks(tasks, "python")
    assert results[0]["title"] == "Learn Python"
    assert tasks[0]["title"] == "Learn Python"