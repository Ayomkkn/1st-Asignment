def doc_text(task_name, task_description, status):
    return f"""========= TASKS APP =========
TASK DETAIL
………………………….………………….
——— {task_name} ———
Title: {task_name}
Description: {task_description}
Status: {status}
………………………….………………….
"""

options = """………………………….………………….
OPTIONS:
1. Go back to tasks list
2. Mark task as COMPLETED
3. Delete this task
………………………….………………….
"""


def task_detail(task, task_list):
    while True:
        print(doc_text(task['name'], task['description'], task['status']))
        print(options)

        user_input = input("Enter a number to proceed: ")

        if user_input == "1":
            return "back"

        elif user_input == "2":
            task['status'] = "COMPLETED"
            print("\nTask marked as COMPLETED.\n")

        elif user_input == "3":
            task_list.remove(task)
            print("Task deleted.\n")
            return "deleted"

        else:
            print("Invalid input. Try again.\n")