from app.models import Task, Priority
from app.exceptions import TaskNotFoundError


class TaskRepository:
    """In memory storage for tasks. Swapped for a real database in Module 7 - 
    the method signatures below are designed to stay identical when that happens."""
    def __init__(self) -> None:
        self._tasks: dict[int, Task] = {}
        self._next_id: int = 1

    def add(self, title: str, owner_id: int, description: str = "", priority = Priority.MEDIUM) -> Task:
        """Add a new task to the repository."""
        task = Task(
            id=self._next_id,
            title=title,
            owner_id=owner_id,
            description=description,
            priority=priority
        )
        self._tasks[task.id] = task
        self._next_id += 1
        return task

    def get(self, task_id: int) -> Task:
        try:
            return self._tasks[task_id]
        except KeyError:
            raise TaskNotFoundError(f"Task with id {task_id} not found.")

    def list(self, owner_id: int, priority: Priority | None = None, completed: bool | None = None) -> list[Task]:
        results = [task for task in self._tasks.values() if task.owner_id == owner_id]
        if priority is not None:
            results = [task for task in results if task.priority == priority]
        if completed is not None:
            results = [task for task in results if task.completed == completed]
        return results

    def update(self, task_id: int, **changes) -> Task:
        task = self.get(task_id)
        for key, value in changes.items():
            if value is not None and hasattr(task, key):
                setattr(task, key, value)
        return task

    def delete(self, task_id: int) -> None:
        if task_id not in self._tasks:
            raise TaskNotFoundError(f"Task with id {task_id} not found.")
        del self._tasks[task_id]