doc_text = """
========= TASKS APP =========
………………………….………………….
CREATE A TASK
………………………….………………….
"""


def create_task():
    print(doc_text)

    task_name = input("Enter the name of the task: ")
    task_description = input("Enter the description of the task: ")

    print(f"Task '{task_name}' created successfully!")

    return {
        "name": task_name,
        "description": task_description,
        "status": "PENDING"   
    }