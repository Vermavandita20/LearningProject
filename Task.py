from dataclasses import dataclass
import datetime

@dataclass
class Task:
    id: int
    title: str
    description: str
    due_date: datetime.date
    status: str = "Pending"

    def __init__(self, title, description, due_date=None, status="Pending", id=None):
        self.id = id
        self.title = title
        self.description = description
        self.due_date = due_date or datetime.date.today()
        self.status = status
