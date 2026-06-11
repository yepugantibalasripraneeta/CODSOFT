tasks = []

while True:
    print("\n--- TO DO LIST ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        if len(tasks) == 0:
            print("Your list is empty.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")
                
    elif choice == "2":
        new_task = input("Enter a new task: ")
        if new_task != "":
            tasks.append(new_task)
            print("Task added!")
        else:
            print("You can't add an empty task.")
            
    elif choice == "3":
        if len(tasks) == 0:
            print("Nothing to delete.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")
                
            try:
                no = int(input("Enter the number to delete: "))
                if no >= 1 and no <= len(tasks):
                    removed = tasks.pop(no - 1)
                    print(f"Deleted: {removed}")
                else:
                    print("Invalid number.")
            except:
                print("Please enter a number.")
                
    elif choice == "4":
        print("Bye!")
        break
        
    else:
        print("Invalid input, try again.")