# Chrona Data Model

# 1. Overview

This document defines the core data structures used throughout Chrona.

The data model acts as the foundation for:

* task management,
* scheduling,
* conflict detection,
* timetable handling,
* notifications,
* and future intelligent planning systems.

Chrona follows a modular data-oriented architecture where each entity has a clearly defined responsibility.

---

# 2. Design Principles

The Chrona data model follows these principles:

* Simplicity first
* Extensible structure
* Minimal redundancy
* Modular relationships
* Deterministic scheduling support
* Future scalability

The initial implementation should prioritize clarity and maintainability over optimization.

---

# 3. Core Entities

Chrona initially contains the following primary entities:

* Task
* Subtask
* ScheduleBlock
* TimetableEntry
* Event
* Notification
* Conflict
* DailyPlan

---

# 4. Task Entity

The Task entity represents a unit of work.

Tasks are the primary object managed by Chrona.

---

## Responsibilities

A task stores:

* work description,
* deadlines,
* priorities,
* estimated effort,
* status,
* and scheduling metadata.

---

## Structure

```python id="rbxijq"
Task:
    id
    title
    description
    category
    priority
    status

    estimated_duration
    remaining_duration

    actual_deadline
    expected_deadline

    created_at
    updated_at

    dependencies
    subtasks

    schedule_blocks
```

---

## Fields

| Field              | Description                     |
| ------------------ | ------------------------------- |
| id                 | Unique identifier               |
| title              | Short task title                |
| description        | Detailed explanation            |
| category           | Academic, coding, personal, etc |
| priority           | Importance level                |
| status             | Pending, active, completed      |
| estimated_duration | Total estimated time            |
| remaining_duration | Remaining work time             |
| actual_deadline    | Real-world final deadline       |
| expected_deadline  | Internal target completion date |
| created_at         | Creation timestamp              |
| updated_at         | Last modification timestamp     |

---

# 5. Subtask Entity

Subtasks represent smaller units of a larger task.

Chrona may automatically generate subtasks in future versions.

---

## Structure

```python id="iwsl7h"
Subtask:
    id
    parent_task_id
    title
    estimated_duration
    status
```

---

# 6. ScheduleBlock Entity

Schedule blocks represent allocated work periods.

Example:

```text id="8s5q6g"
Sunday 4 PM - 6 PM
DBMS Assignment Research
```

---

## Structure

```python id="d7tlh4"
ScheduleBlock:
    id
    task_id

    start_time
    end_time

    block_type
    status
```

---

## Block Types

Possible block types:

* Work
* Review
* Buffer
* Break
* Focus Session

---

# 7. TimetableEntry Entity

Represents recurring user schedules.

Examples:

* classes,
* routines,
* fixed commitments.

---

## Structure

```python id="1m66je"
TimetableEntry:
    id

    day_of_week

    start_time
    end_time

    activity
    entry_type
```

---

## Entry Types

Examples:

* Class
* Personal
* Travel
* Sleep
* Fixed Work

---

# 8. Event Entity

Chrona uses event-driven scheduling.

Events trigger replanning and notifications.

---

## Structure

```python id="tr0jlwm"
Event:
    id

    event_type
    timestamp

    source_module
    related_entity

    metadata
```

---

## Example Events

* TaskAdded
* TaskCompleted
* DeadlineMissed
* ConflictDetected
* TimetableUpdated
* LeaveAdded

---

# 9. Notification Entity

Represents user alerts and reminders.

---

## Structure

```python id="k1cxns"
Notification:
    id

    title
    message

    notification_type

    created_at
    scheduled_time

    is_read
```

---

## Notification Types

Examples:

* Reminder
* Warning
* Conflict Alert
* Deadline Alert
* Daily Summary

---

# 10. Conflict Entity

Represents scheduling or workload issues.

---

## Structure

```python id="fhrwzs"
Conflict:
    id

    conflict_type
    severity

    related_tasks

    detected_at

    resolution_status
```

---

## Conflict Types

Examples:

* Time Conflict
* Workload Overload
* Deadline Risk
* Dependency Conflict

---

# 11. DailyPlan Entity

Represents a generated plan for a single day.

---

## Structure

```python id="jx6d3g"
DailyPlan:
    id

    date

    schedule_blocks

    total_workload

    free_time

    stress_score
```

---

# 12. Relationships

## High-Level Relationships

```text id="yvk2pj"
Task
 ├── Subtasks
 ├── ScheduleBlocks
 ├── Notifications
 └── Conflicts

TimetableEntry
 └── Influences Scheduler

Events
 └── Trigger Replanning
```

---

# 13. Scheduling Metadata

Chrona scheduling decisions depend on:

* estimated duration,
* remaining duration,
* free time,
* deadlines,
* and timetable constraints.

Future versions may include:

* energy levels,
* productivity tracking,
* focus estimation,
* and adaptive learning.

---

# 14. Future Expansion

Potential future entities:

* UserProfile
* ProductivityMetrics
* FocusSession
* AutomationRule
* GitHubTask
* AcademicCourse
* SmartRecommendation

These entities are intentionally excluded from the initial MVP.

---

# 15. Initial Persistence Strategy

Chrona initially uses:

* SQLite for persistence,
* local-first storage,
* and lightweight data access.

Future versions may include:

* synchronization,
* backups,
* exports,
* and cloud storage.

---

# 16. Data Model Philosophy

Chrona’s data model prioritizes:

* clarity,
* extensibility,
* deterministic scheduling support,
* and maintainable long-term architecture.

The system should remain modular and adaptable as scheduling complexity increases.
