import sys


def main():
    task = []
    print("Welcome to To-Do app")

    while True:
        choose = input(
            "\nMenu: \n1.Add task ✏️\n2.Remove task ✂️\n3.Mark complete ✅\n4.View all tasks 📄\n5.Quit ❌\n[1-5]: "
        )
        if choose == "1":
            add_task(task)
        elif choose == "2":
            task_to_remove = get_task_to_remove(task)
            if task_to_remove is not None:
                remove_task(task, task_to_remove)
        elif choose == "3":
            task_to_complete = get_mark_complete(task)
            if task_to_complete is not None:
                mark_complete(task, task_to_complete)
        elif choose == "4":
            view_all_task(task)
        elif choose == "5":
            sys.exit("\nExiting from To-Do app 👋")


def add_task(task, new_task=None):
    if new_task is None:
        new_task = input("\nEnter the task: ")
    task.append({"title": new_task, "completed": False})


def get_task_to_remove(task):
    try:
        for i, t in enumerate(task):
            print(f"\n--> {i+1}.{t['title']} <--")
        task_to_remove = int(input("\nEnter the number to remove a task: "))
    except ValueError:
        print("\nInvalid number")
        answer = input("\nDo you want to return menu? [Y/n] ").lower().strip()
        if answer == "y" or answer == "yes":
            return None
        elif answer == "n" or answer == "no":
            return get_task_to_remove(task)
        else:
            print("\nInvalid input. Please enter 'y' or 'n'.")
            return get_task_to_remove(task)
    return task_to_remove


def remove_task(task, task_to_remove):
    if 1 <= task_to_remove <= len(task):
        del task[task_to_remove - 1]
    else:
        print("\nInvalid task number.")


def get_mark_complete(task):
    try:
        for i, t in enumerate(task):
            print(f"\n--> {i+1}.{t['title']} <--")
        task_to_complete = int(
            input("\nEnter the number of the task to mark as complete: ")
        )
    except ValueError:
        print("\nInvalid number")
        answer = input("\nDo you want to return menu? [Y/n] ").lower().strip()
        if answer == "y" or answer == "yes":
            return None
        elif answer == "n" or answer == "no":
            return get_mark_complete(task)
        else:
            print("\nInvalid input. Please enter 'y' or 'n'.")
            return get_mark_complete(task)

    return task_to_complete


def mark_complete(task, task_to_complete):
    if 1 <= task_to_complete <= len(task):
        task[task_to_complete - 1]["completed"] = True
    else:
        print("\nInvalid task number.")


def view_all_task(task):
    if not task:
        print("\nNo tasks 👍")
    else:
        for t in task:
            task_name = t["title"]
            if t["completed"] == True:
                status = "Completed 🟢"
            else:
                status = "Not Completed 🔴"
            print(f"\n⭐ Task: {task_name}, status: {status}")


if __name__ == "__main__":
    main()
import sys


def main():
    task = []
    print("Welcome to To-Do app")

    while True:
        choose = input(
            "\nMenu: \n1.Add task ✏️\n2.Remove task ✂️\n3.Mark complete ✅\n4.View all tasks 📄\n5.Quit ❌\n[1-5]: "
        )
        if choose == "1":
            add_task(task)
        elif choose == "2":
            task_to_remove = get_task_to_remove(task)
            if task_to_remove is not None:
                remove_task(task, task_to_remove)
        elif choose == "3":
            task_to_complete = get_mark_complete(task)
            if task_to_complete is not None:
                mark_complete(task, task_to_complete)
        elif choose == "4":
            view_all_task(task)
        elif choose == "5":
            sys.exit("\nExiting from To-Do app 👋")


def add_task(task, new_task=None):
    if new_task is None:
        new_task = input("\nEnter the task: ")
    task.append({"title": new_task, "completed": False})


def get_task_to_remove(task):
    try:
        for i, t in enumerate(task):
            print(f"--> \n{i+1}.{t['title']} <--")
        task_to_remove = int(input("\nEnter the number to remove a task: "))
    except ValueError:
        print("\nInvalid number")
        answer = input("\nDo you want to return menu? [Y/n] ").lower().strip()
        if answer == "y" or answer == "yes":
            return None
        elif answer == "n" or answer == "no":
            return get_task_to_remove(task)
        else:
            print("\nInvalid input. Please enter 'y' or 'n'.")
            return get_task_to_remove(task)
    return task_to_remove


def remove_task(task, task_to_remove):
    if 1 <= task_to_remove <= len(task):
        del task[task_to_remove - 1]
    else:
        print("\nInvalid task number.")


def get_mark_complete(task):
    try:
        for i, t in enumerate(task):
            print(f"\n--> {i+1}.{t['title']} <--")
        task_to_complete = int(
            input("\nEnter the number of the task to mark as complete: ")
        )
    except ValueError:
        print("\nInvalid number")
        answer = input("\nDo you want to return menu? [Y/n] ").lower().strip()
        if answer == "y" or answer == "yes":
            return None
        elif answer == "n" or answer == "no":
            return get_mark_complete(task)
        else:
            print("\nInvalid input. Please enter 'y' or 'n'.")
            return get_mark_complete(task)

    return task_to_complete


def mark_complete(task, task_to_complete):
    if 1 <= task_to_complete <= len(task):
        task[task_to_complete - 1]["completed"] = True
    else:
        print("\nInvalid task number.")


def view_all_task(task):
    if not task:
        print("\nNo tasks 👍")
    else:
        for t in task:
            task_name = t["title"]
            if t["completed"] == True:
                status = "Completed 🟢"
            else:
                status = "Not Completed 🔴"
            print(f"\n⭐ Task: {task_name}, status: {status}")


if __name__ == "__main__":
    main()
