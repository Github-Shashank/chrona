# Chrona Scheduling Engine

# 1. Overview

The Scheduling Engine is the core intelligence layer of Chrona.

Its responsibility is to:

* allocate work intelligently,
* distribute workload realistically,
* avoid scheduling conflicts,
* reduce deadline pressure,
* and continuously adapt schedules over time.

Unlike static reminder systems, Chrona scheduling is dynamic and adaptive.

The scheduler continuously evaluates:

* available time,
* task urgency,
* workload balance,
* timetable constraints,
* and changing conditions.

---

# 2. Scheduling Goals

The primary goals of the scheduling engine are:

* Prevent missed deadlines
* Reduce last-minute workload pressure
* Balance daily workload
* Minimize scheduling conflicts
* Utilize free time efficiently
* Adapt to schedule changes dynamically
* Maintain realistic schedules
* Support long-term productivity consistency

---

# 3. Scheduling Philosophy

Chrona scheduling follows these principles:

## 3.1 Expected Deadline Priority

Chrona prioritizes expected deadlines before actual deadlines.

Expected deadlines act as:

* safety buffers,
* workload balancing tools,
* and stress reduction mechanisms.

The scheduler should attempt to complete tasks before the expected deadline whenever possible.

---

## 3.2 Deadline Safety

The scheduler should avoid:

* last-day workload concentration,
* excessive urgency,
* and unrealistic planning.

Tasks approaching actual deadlines should receive higher urgency.

---

## 3.3 Balanced Work Distribution

Chrona should distribute work across multiple days instead of concentrating work into a single period.

The scheduler should prefer:

* gradual progress,
* consistent work allocation,
* and manageable daily plans.

---

## 3.4 Dynamic Adaptation

Schedules should continuously adapt when:

* new tasks are added,
* tasks are delayed,
* leave days are added,
* or workload changes occur.

---

## 3.5 Stability Preservation

Chrona should avoid unnecessary schedule instability.

Frequent schedule changes may:

* reduce trust,
* create confusion,
* and disrupt productivity.

Replanning should minimize unnecessary modifications.

---

# 4. Scheduling Pipeline

The scheduling engine follows this pipeline:

```text id="h2n3s0"
Task Intake
    ↓
Task Analysis
    ↓
Free Time Detection
    ↓
Priority Evaluation
    ↓
Workload Allocation
    ↓
Conflict Detection
    ↓
Schedule Generation
    ↓
Continuous Replanning
```

---

# 5. Task Analysis

Before scheduling, Chrona analyzes each task.

The analysis phase determines:

* estimated effort,
* urgency,
* scheduling flexibility,
* dependencies,
* and workload impact.

---

## Inputs

Examples:

* actual deadline,
* expected deadline,
* priority,
* estimated duration,
* category,
* dependencies.

---

## Outputs

Examples:

* urgency score,
* scheduling weight,
* allocation priority,
* estimated workload.

---

# 6. Free Time Detection

Chrona determines available scheduling capacity using:

* timetable entries,
* leave days,
* recurring routines,
* and occupied schedule blocks.

---

## Examples

### Weekday

```text id="mhdrw8"
Classes: 9 AM - 5 PM
Free Time: 6 PM - 10 PM
```

### Sunday

```text id="vw9btf"
Higher scheduling capacity
```

---

# 7. Priority Evaluation

Chrona determines scheduling importance using multiple factors.

Potential factors include:

* actual deadline proximity,
* expected deadline proximity,
* task priority,
* remaining duration,
* and workload pressure.

---

## Example Priority Formula

```text id="2r7s7n"
priority_score =
deadline_urgency +
task_importance +
remaining_workload -
available_free_time
```

This formula is conceptual and may evolve in future versions.

---

# 8. Workload Allocation

The scheduler allocates work into schedule blocks.

Goals:

* balanced workload,
* realistic daily plans,
* reduced overload,
* and deadline safety.

---

## Allocation Rules

Chrona should:

* split large tasks into smaller work sessions,
* distribute work gradually,
* preserve breaks and buffer time,
* and avoid excessive consecutive workload.

---

## Example

```text id="m4z2av"
Task:
DBMS Assignment

Estimated Duration:
6 hours

Possible Allocation:
Sunday: 2 hours
Monday: 2 hours
Tuesday: 1.5 hours
Wednesday: Review 30 minutes
```

---

# 9. Conflict Detection

After allocation, Chrona validates the generated schedule.

---

## Conflict Types

### Time Conflict

Two tasks occupy the same time period.

---

### Workload Overload

Assigned work exceeds realistic daily capacity.

---

### Deadline Risk

Remaining free time is insufficient before deadline.

---

### Dependency Conflict

A dependent task is scheduled before prerequisite completion.

---

# 10. Conflict Resolution

When conflicts are detected, Chrona may:

* redistribute workload,
* shift lower-priority tasks,
* reduce scheduling density,
* or raise warnings.

---

## Resolution Priorities

Chrona should prioritize:

1. Actual deadlines
2. Expected deadlines
3. Task importance
4. Schedule stability

---

# 11. Dynamic Replanning

Chrona continuously updates schedules.

---

## Replanning Triggers

Examples:

* new task added,
* task delayed,
* missed expected deadline,
* timetable update,
* leave added,
* workload increase.

---

## Replanning Goals

Replanning should:

* preserve existing structure when possible,
* minimize disruption,
* and maintain realistic scheduling.

---

# 12. Scheduling Constraints

Chrona scheduling must respect:

* timetable restrictions,
* occupied blocks,
* dependencies,
* leave days,
* and workload limits.

Future versions may include:

* sleep tracking,
* energy patterns,
* focus estimation,
* and productivity analysis.

---

# 13. Buffer Time Philosophy

Chrona should maintain scheduling flexibility.

The scheduler should reserve:

* review time,
* unexpected delay margins,
* and recovery space.

This reduces:

* deadline pressure,
* overload,
* and scheduling fragility.

---

# 14. Long-Term Scheduling Vision

Future scheduling enhancements may include:

* adaptive duration estimation,
* workload prediction,
* intelligent prioritization,
* behavioral learning,
* and predictive scheduling optimization.

These features are intentionally excluded from the MVP.

---

# 15. MVP Scheduling Scope

The initial Chrona scheduler should support:

* basic workload allocation,
* expected vs actual deadlines,
* timetable-aware scheduling,
* simple conflict detection,
* and basic replanning.

The MVP should prioritize:

* reliability,
* maintainability,
* and deterministic behavior.

---

# 16. Scheduling Engine Philosophy

Chrona scheduling is intended to behave like:

* a planning assistant,
* not merely a reminder system.

The scheduler should:

* help users stay ahead of deadlines,
* maintain manageable workload,
* and adapt intelligently to changing conditions.

The scheduling engine is the central system responsible for Chrona’s adaptive productivity behavior.
