from project import add_task, remove_task, mark_complete


def main():
    test_add_task()
    test_remove_task()
    test_mark_complete()


def test_add_task():
    task = []
    add_task(task, "Drink a coffee")
    assert task == [{"title": "Drink a coffee", "completed": False}]


def test_remove_task():
    task = [{"title": "Drink a coffee", "completed": False}]
    remove_task(task, 1)
    assert task == []


def test_mark_complete():
    task = [{"title": "Drink a coffee", "completed": False}]
    mark_complete(task, 1)
    assert task == [{"title": "Drink a coffee", "completed": True}]


if __name__ == "__main__":
    main()
