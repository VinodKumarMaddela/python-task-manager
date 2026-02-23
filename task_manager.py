import json
import os

class TaskManager:
    def __init__(self, file_name="tasks.json"):
        self.file_name = file_name
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as file:
                return json.load(file)
        return []

    def save_tasks(self):
        with open(self.file_name, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, title):
        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "completed": False
        }
        self.tasks.append(task)
        self.save_tasks()
        print("✅ Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        for task in self.tasks:
            status = "✔ Done" if task["completed"] else "❌ Pending"
            print(f'ID: {task["id"]} | {task["title"]} | {status}')

    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                self.save_tasks()
                print("🎉 Task marked as completed!")
                return
        print("Task not found.")

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task["id"] != task_id]
        self.save_tasks()
        print("🗑 Task deleted successfully!")


def main():
    manager = TaskManager()

    while True:
        print("\n--- Task Manager ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            manager.add_task(title)

        elif choice == "2":
            manager.view_tasks()

        elif choice == "3":
            task_id = int(input("Enter task ID to complete: "))
            manager.complete_task(task_id)

        elif choice == "4":
            task_id = int(input("Enter task ID to delete: "))
            manager.delete_task(task_id)

        elif choice == "5":
            print("Exiting Task Manager...")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()