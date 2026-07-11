doc_text = """
========= TASKS APP =========
………………………….………………….
MAIN MENU
    You currently have no tasks, add a task to proceed
………………………….………………….
OPTIONS:
1. Create a Task
………………………….………………….
"""

def print_main_menu_no_task():
    print(doc_text)
    
    user_input = input("Enter your choice: ")
    
    return user_input

