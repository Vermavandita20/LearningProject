from Services import TaskService
from TaskRepository import TaskRepository

def main():
    repository = TaskRepository()
    service = TaskService(repository)

    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. View Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. List All Tasks")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter title: ")
            description = input("Enter description: ")
            due_date = input("Enter due date (YYYY-MM-DD) or leave blank for today: ")
            service.create_task(title, description, due_date or None)
            print("Task added.")

        elif choice == '2':
            task_id = int(input("Enter task ID: "))
            task = service.get_task(task_id)
            if task:
                print(task)
            else:
                print("Task not found.")

        elif choice == '3':
            task_id = int(input("Enter task ID: "))
            title = input("Enter new title (leave blank to keep current): ")
            description = input("Enter new description (leave blank to keep current): ")
            due_date = input("Enter new due date (YYYY-MM-DD) (leave blank to keep current): ")
            status = input("Enter new status (Pending/Completed) (leave blank to keep current): ")
            service.update_task(task_id,
                                title=title if title else None,
                                description=description if description else None,
                                due_date=due_date if due_date else None,
                                status=status if status else None)
            print("Task updated.")

        elif choice == '4':
            task_id = int(input("Enter task ID: "))
            service.delete_task(task_id)
            print("Task deleted.")


        elif choice == '5':
            tasks = service.list_tasks()
            for task in tasks:
                print(task)

        elif choice == '6':
            print("Exiting.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
