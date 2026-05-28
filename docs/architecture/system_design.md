# Chrona System Design

# 1. Overview

Chrona is an adaptive desktop productivity assistant designed to intelligently manage tasks, deadlines, schedules, and workload planning.

Unlike traditional task managers, Chrona focuses on:

* adaptive scheduling,
* workload balancing,
* conflict-aware planning,
* dynamic replanning,
* and intelligent time allocation.

Chrona follows a terminal-first workflow with minimal graphical UI components for visualization and scheduling.

The system is intended to evolve incrementally toward production-level architecture and scalability.

---

# 2. System Goals

The primary goals of Chrona are:

* Manage tasks and deadlines efficiently
* Reduce deadline pressure using expected deadlines
* Analyze workload dynamically
* Allocate time intelligently
* Detect scheduling conflicts
* Continuously adapt schedules
* Provide lightweight but powerful interaction
* Maintain modular and scalable architecture

---

# 3. Core Architectural Philosophy

Chrona follows these architectural principles:

## 3.1 Modular Design

Each subsystem should remain independent and maintain clear responsibilities.

Modules should:

* minimize coupling,
* maximize maintainability,
* and support future scalability.

---

## 3.2 Event-Driven Behavior

Chrona reacts to system events such as:

* task creation,
* task completion,
* timetable updates,
* schedule conflicts,
* missed deadlines,
* and leave days.

Events trigger scheduling recalculation and replanning.

---

## 3.3 Deterministic-First Development

The system prioritizes:

* reliable logic,
* rule-based scheduling,
* and predictable behavior

before introducing advanced AI or adaptive learning systems.

---

## 3.4 Incremental Evolution

Chrona is designed to evolve in phases:

1. Functional core
2. Stable scheduling
3. Conflict-aware planning
4. Adaptive scheduling
5. Intelligent assistance

---

# 4. High-Level Architecture

```text
+----------------------+
|  Terminal Interface  |
+----------------------+
           |
           v
+----------------------+
|   Command Parser     |
+----------------------+
           |
           v
+----------------------+
|     Task Engine      |
+----------------------+
           |
           v
+----------------------+
|   Scheduler Engine   |
+----------------------+
           |
           v
+----------------------+
|  Conflict Resolver   |
+----------------------+
           |
           v
+----------------------+
|  Calendar Planner    |
+----------------------+
           |
           v
+----------------------+
|  Notification System |
+----------------------+
           |
           v
+----------------------+
|    Storage Layer     |
+----------------------+
```

---

# 5. Core Modules

# 5.1 Terminal Interface

Purpose:

* Primary user interaction layer

Responsibilities:

* Accept commands
* Display schedules
* Show task summaries
* Show warnings and alerts
* Provide fast keyboard-driven workflow

Example Commands:

```bash
chrona add-task
chrona today
chrona conflicts
chrona week
```

---

# 5.2 Command Parser

Purpose:

* Interpret user commands

Responsibilities:

* Parse terminal input
* Validate arguments
* Route actions to appropriate modules

Future Scope:

* Natural language parsing
* Intelligent command suggestions

---

# 5.3 Task Engine

Purpose:

* Manage all task-related operations

Responsibilities:

* Create tasks
* Update tasks
* Delete tasks
* Track task state
* Store deadlines
* Handle priorities
* Maintain subtasks and dependencies

Core Concepts:

* Actual deadline
* Expected deadline
* Priority level
* Estimated duration

---

# 5.4 Scheduler Engine

Purpose:

* Allocate available time intelligently

Responsibilities:

* Analyze available free slots
* Assign tasks into schedule blocks
* Balance workload
* Respect timetable constraints
* Optimize task distribution

Inputs:

* Tasks
* Timetable
* Deadlines
* Free time

Outputs:

* Scheduled work blocks
* Daily plans
* Weekly allocation

---

# 5.5 Conflict Resolver

Purpose:

* Detect and resolve scheduling issues

Conflict Types:

* Time conflicts
* Workload overload
* Deadline risks
* Dependency violations
* Schedule collisions

Responsibilities:

* Detect conflicts
* Prioritize severity
* Trigger replanning
* Suggest schedule adjustments

---

# 5.6 Timetable Manager

Purpose:

* Maintain recurring schedules

Responsibilities:

* Store classes
* Store routines
* Store leave days
* Detect free time
* Calculate available scheduling capacity

Future Scope:

* Energy-based scheduling
* Productivity pattern analysis

---

# 5.7 Calendar Planner

Purpose:

* Visualize scheduled tasks

Responsibilities:

* Show weekly planning
* Show task allocation
* Highlight conflicts
* Display deadlines visually

UI Philosophy:

* Minimal
* Informative
* Lightweight

---

# 5.8 Notification System

Purpose:

* Alert users about important events

Responsibilities:

* Deadline reminders
* Expected deadline warnings
* Conflict alerts
* Schedule updates
* Daily summaries

Future Scope:

* Smart reminder intensity
* Context-aware notifications

---

# 5.9 Storage Layer

Purpose:

* Persist all application data

Initial Storage:

* SQLite database

Responsibilities:

* Store tasks
* Store schedules
* Store events
* Store timetable entries
* Maintain application state

Future Scope:

* Backup system
* Export/import
* Cloud synchronization

---

# 6. Event System

Chrona operates through events.

Examples:

* TaskAdded
* TaskCompleted
* DeadlineMissed
* ScheduleConflictDetected
* LeaveAdded
* TimetableUpdated

Events may trigger:

* schedule recalculation,
* notifications,
* conflict analysis,
* or replanning.

---

# 7. Scheduling Philosophy

Chrona scheduling should prioritize:

1. Deadline safety
2. Reduced workload stress
3. Balanced work distribution
4. Conflict minimization
5. Consistent progress
6. Efficient use of free time

The scheduler should avoid:

* excessive workload concentration,
* unrealistic daily allocation,
* and last-minute scheduling pressure.

---

# 8. Dynamic Replanning

Chrona continuously adapts schedules.

Triggers include:

* new tasks,
* delayed work,
* leave days,
* unexpected workload,
* and missed expected deadlines.

Replanning should:

* preserve stability when possible,
* minimize unnecessary changes,
* and maintain realistic schedules.

---

# 9. User Experience Philosophy

Chrona prioritizes:

* speed,
* clarity,
* keyboard-first interaction,
* and low interface complexity.

The interface should support:

* fast workflows,
* quick updates,
* and minimal distraction.

---

# 10. Future System Expansion

Potential future features include:

* natural language task input,
* intelligent duration estimation,
* adaptive workload learning,
* GitHub integration,
* academic planning,
* automation workflows,
* and predictive scheduling systems.

---

# 11. Development Strategy

Chrona should be developed incrementally.

Recommended order:

1. Core task system
2. Timetable management
3. Scheduling engine
4. Conflict detection
5. Calendar visualization
6. Dynamic replanning
7. Intelligent scheduling enhancements

Architecture stability should always take priority over rapid feature expansion.
