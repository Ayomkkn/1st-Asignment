doc_text_start = f"""
========= TASKS APP =========
………………………….………………….
TASK LIST
"""

doc_text_end = f"""
………………………….………………….
OPTIONS:
1. Create a Task
2. View Task Detail
3. Show next 3 items
4. Show previous 3 items (TODO)
………………………….………………….
"""

def print_task_list(task_list):
    print(doc_text_start)
    
    for index, task in enumerate(task_list[start_index:end_index], start=start_index):
        print(f"{index}. {task['name']}")
        
    print(doc_text_end)
    
    user_input = input("Select an option: ")
    return user_input
    