from task_manager import add_task, view_tasks
from report_generator import generate_report

while True:
    print("\n--- Task Management System ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Generate Report")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        employee = input("Enter employee name: ")
        task = input("Enter task description: ")
        add_task(employee, task)
        print("Task added successfully.")

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        generate_report()

    elif choice == "4":
        print("Exiting system.")
        break

    else:
        print("Invalid choice. Please try again.")
