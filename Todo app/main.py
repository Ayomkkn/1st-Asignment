from views.main_menu_no_task import print_main_menu_no_task
from views.task_list import print_task_list
from views.create_task import create_task
from views.show_task_detail import task_detail

task_list = []

start = 0
end = 3


def main():
    while True:
        if not task_list:
            user_input = print_main_menu_no_task()

            if user_input == "1":
                new_task = create_task()
                task_list.append(new_task)
            else:
                print("Invalid input. Exiting.")
                break

        else:
            global start
            global end
            user_input = print_task_list(task_list, start, end)
        
            if user_input == "1":
                new_task = create_task()
                task_list.append(new_task)

            elif user_input == "2":
                try:
                    task_id = int(input("Enter task number: "))
                    task = task_list[task_id - 1]

                    result = task_detail(task, task_list)

                    if result == "deleted":
                        print("Task removed. Returning to list...\n")

                except (ValueError, IndexError):
                    print("Invalid task number.\n")

            elif user_input == "3":
                start += 3
                end += 3

            else:
                print("Invalid input. Exiting.")
                break


if __name__ == "__main__":
    main()