# Chrona MVP Definition

# 1. Overview

This document defines the Minimum Viable Product (MVP) scope for Chrona.

The MVP represents the first stable and usable version of the system.

The goal of the MVP is not to implement every long-term idea, but to establish:

* a strong architectural foundation,
* reliable scheduling behavior,
* modular system structure,
* and production-oriented development workflow.

The MVP should prioritize:

* stability,
* maintainability,
* clarity,
* and incremental scalability.

---

# 2. MVP Goals

The Chrona MVP aims to:

* Provide intelligent task management
* Support adaptive scheduling
* Handle expected and actual deadlines
* Detect scheduling conflicts
* Analyze free time
* Generate realistic schedules
* Support timetable-aware planning
* Provide lightweight interaction
* Establish production-grade architecture

---

# 3. Core MVP Features

# 3.1 Task Management

The MVP must support:

* Task creation
* Task editing
* Task deletion
* Task completion tracking
* Task categorization
* Task priorities
* Estimated durations
* Actual deadlines
* Expected deadlines

---

# 3.2 Timetable Management

The MVP must support:

* Weekly timetable creation
* Recurring schedule blocks
* Class schedules
* Fixed routines
* Leave days
* Free-time calculation

---

# 3.3 Scheduling Engine

The MVP scheduler must support:

* Basic workload allocation
* Task splitting into schedule blocks
* Deadline-aware scheduling
* Expected deadline prioritization
* Timetable-aware scheduling
* Basic schedule generation

The scheduler should prioritize:

* realistic workload,
* balanced task distribution,
* and deadline safety.

---

# 3.4 Conflict Detection

The MVP must detect:

* Time conflicts
* Workload overload
* Deadline risks
* Basic scheduling collisions

The MVP may initially provide warnings instead of advanced automatic resolution.

---

# 3.5 Calendar Visualization

The MVP should provide:

* Weekly schedule view
* Daily schedule view
* Task allocation visualization
* Deadline visibility
* Conflict highlighting

The calendar UI should remain:

* lightweight,
* minimal,
* and informative.

---

# 3.6 Terminal Interface

Chrona MVP should remain terminal-first.

The terminal should support:

* task commands,
* schedule viewing,
* conflict inspection,
* and timetable management.

---

# 3.7 Notification System

The MVP should support:

* Deadline reminders
* Expected deadline warnings
* Daily summaries
* Conflict alerts
* Schedule update notifications

---

# 3.8 Local Persistence

The MVP must support persistent local storage using SQLite.

Stored data includes:

* tasks,
* schedules,
* timetable entries,
* notifications,
* and events.

---

# 4. Explicitly Excluded Features

The following features are intentionally excluded from the MVP.

---

## 4.1 Artificial Intelligence Systems

Excluded:

* AI agents
* autonomous planning
* intelligent conversational systems
* advanced learning systems

Reason:
The MVP prioritizes deterministic architecture first.

---

## 4.2 Full Natural Language Understanding

Excluded:

* conversational command parsing
* free-form intelligent task analysis

The MVP may later support structured natural language input.

---

## 4.3 Cloud Synchronization

Excluded:

* online synchronization
* multi-device sync
* account systems

Chrona MVP remains local-first.

---

## 4.4 Mobile Application

Excluded:

* Android app
* iOS app

The MVP focuses on desktop architecture first.

---

## 4.5 Advanced Adaptive Learning

Excluded:

* behavior prediction
* productivity learning
* automatic habit analysis
* personalized optimization

These features require historical system data.

---

## 4.6 Automation Systems

Excluded:

* desktop automation
* browser automation
* workflow automation
* external application control

---

# 5. MVP User Experience Philosophy

The MVP should prioritize:

* simplicity,
* fast workflows,
* low UI complexity,
* and productivity-focused interaction.

Chrona should feel:

* lightweight,
* responsive,
* and efficient.

---

# 6. MVP Technical Priorities

The MVP should prioritize:

1. Correct architecture
2. Stable scheduling logic
3. Reliable data persistence
4. Modular design
5. Maintainable codebase

The MVP should avoid:

* premature optimization,
* feature overload,
* and unnecessary complexity.

---

# 7. MVP Success Criteria

The MVP is considered successful if it can:

* manage tasks reliably,
* generate usable schedules,
* detect conflicts,
* adapt to timetable constraints,
* and provide a stable productivity workflow.

The MVP does not need:

* advanced intelligence,
* AI automation,
* or predictive behavior.

---

# 8. Development Philosophy

Chrona MVP is intended to establish:

* the core architecture,
* scheduling philosophy,
* and long-term scalability of the system.

Future intelligence and advanced automation should be built on top of a stable deterministic core.

The MVP should serve as the foundation for future adaptive productivity systems.
