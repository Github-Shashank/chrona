from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4


@dataclass
class Task:
    title: str
    description: str
    category: str
    priority: int

    estimated_duration: float

    actual_deadline: datetime
    expected_deadline: datetime

    status: str = "pending"

    id: str = field(default_factory=lambda: str(uuid4()))

    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    def summary(self) -> str:
        return (
            f"[{self.status.upper()}] "
            f"{self.title} "
            f"(Priority: {self.priority})"
        )