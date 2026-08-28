from dataclasses import dataclass, field 
from datetime import datetime
from enum import Enum

class Priority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

@dataclass
class User:
    id: int
    username: str
    hashed_password: str

@dataclass
class Task:
    id: int
    title: str
    owner_id: int
    description: str = ""
    priority: Priority = Priority.MEDIUM
    completed: bool = False
    created_at: datetime = field(default_factory=datetime.utcnow)