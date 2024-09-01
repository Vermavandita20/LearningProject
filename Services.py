from TaskRepository import TaskRepository
from Task import Task

class TaskService:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def create_task(self, title, description, due_date=None):
        task = Task(title=title, description=description, due_date=due_date)
        return self.repository.add_task(task)

    def get_task(self, task_id):
        return self.repository.get_task(task_id)

    def update_task(self, task_id, title=None, description=None, due_date=None, status=None):
        task = self.repository.get_task(task_id)
        if not task:
            return None

        if title is not None:
            task.title = title
        if description is not None:
            task.description = description
        if due_date is not None:
            task.due_date = due_date
        if status is not None:
            task.status = status

        return self.repository.update_task(task)

    def delete_task(self, task_id):
        return self.repository.delete_task(task_id)

    def list_tasks(self):
        return self.repository.list_tasks()
