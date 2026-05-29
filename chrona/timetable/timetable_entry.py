from dataclasses import dataclass, field
from uuid import uuid4


@dataclass
class TimetableEntry:
    day_of_week: str

    start_time: str
    end_time: str

    activity: str
    entry_type: str

    id: str = field(
        default_factory=lambda: str(uuid4())
    )