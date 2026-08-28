class TaskNotFoundError(Exception):
    """Exception raised when a task is not found."""
    def __init__(self, task_id: int):
        self.task_id = task_id
        super().__init__(f"Task with ID {task_id} not found.")

class UserNotFoundError(Exception):
    """Exception raised when a user is not found."""
    def __init__(self, identifier: str | int):
        self.identifier = identifier
        super().__init__(f"User with identifier {identifier} not found.")