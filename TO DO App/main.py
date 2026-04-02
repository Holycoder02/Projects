def task():
    tasks = {}  #dictionary to store tasks with times
    print("---WELCOME TO THE TASK MANGEMENT APP---")

    total_task = int(input("Enter how many tasks you want to add = "))
    for i in range(1, total_task+1):
        task_name = input(f"Enter task {i} name = ")
        task_time = input(f"Enter task {i} time (e.g., 10:30 AM) = ")
        tasks[task_name] = task_time #add the task and time to the dictionary

    print("\nToday's tasks are:")
    for name, time in tasks.items():
        print(f"  - {name} | Time: {time}")

    while True:
        operation = int(input("\nEnter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit: "))
        if operation == 1:
            add = input("Enter task you want to add = ")
            add_time = input("Enter task time (e.g., 10:30 AM) = ")
            tasks[add] = add_time #add the task to the dictionary
            print(f"Task '{add}' at {add_time} has been added successfully")

        elif operation == 2:
            updated_val = input("Enter the task name you want to update = ")
            if updated_val in tasks:
                up = input("Enter new task name = ")
                up_time = input("Enter new task time = ")
                del tasks[updated_val] #remove old task
                tasks[up] = up_time #add updated task
                print(f"Task updated to '{up}' at {up_time}")
            else:
                print(f"Task '{updated_val}' not found")

        elif operation == 3:
            del_val = input("Enter the task name you want to delete = ")
            if del_val in tasks:
                del tasks[del_val] #delete the task from the dictionary
                print(f"Task '{del_val}' has been deleted successfully")
            else:
                print(f"Task '{del_val}' not found")

        elif operation == 4:
            if tasks:
                print("\nYour tasks:")
                for name, time in tasks.items():
                    print(f"  - {name} | Time: {time}")
            else:
                print("No tasks added yet")

        elif operation == 5:
            print("Exiting the app...")
            break
        else:
            print("Invalid input, please try again")

task()
