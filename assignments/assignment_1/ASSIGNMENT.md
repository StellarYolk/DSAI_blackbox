# 🐍 Python Assignment — Intermediate Level
**DSAI Blackbox | Mentor Program**

---

## 📋 Overview

This assignment tests your understanding of **core Python**, **Data Structures & Algorithms (DSA)**, and **Object-Oriented Programming (OOP)** concepts. You must solve all three problems and submit your solution as a Jupyter Notebook (`.ipynb`).

---

## 📁 Submission Instructions

1. Solve all problems in a **single Jupyter Notebook** named `assignment_<your_name>.ipynb`
2. Push your notebook to **your designated folder** in the repository:
   👉 [https://github.com/StellarYolk/DSAI_blackbox](https://github.com/StellarYolk/DSAI_blackbox)
3. Each problem must be in a **separate section** with clear markdown headings inside the notebook
4. Include **comments** in your code explaining your logic
5. Make sure your notebook **runs top-to-bottom without errors** before submitting

---

## 🔷 Problem 1 — Core Python: Log File Analyzer

### Background

You are given a list of server log entries as strings. Each entry follows this format:

```
"[LEVEL] YYYY-MM-DD HH:MM:SS - Message"
```

**Example entries:**

```python
logs = [
    "[INFO] 2024-03-01 10:00:01 - Server started",
    "[ERROR] 2024-03-01 10:05:22 - Disk space low",
    "[WARNING] 2024-03-01 10:07:45 - CPU usage high",
    "[ERROR] 2024-03-01 10:12:10 - Failed to connect to database",
    "[INFO] 2024-03-01 10:15:00 - Backup completed",
    "[WARNING] 2024-03-02 09:00:00 - Memory usage above threshold",
    "[ERROR] 2024-03-02 09:45:11 - Timeout on request",
]
```

### Tasks

1. Write a function `parse_logs(logs)` that returns a dictionary grouping log messages by their level (`INFO`, `WARNING`, `ERROR`)
2. Write a function `error_summary(logs)` that returns the count of errors per date
3. Write a function `most_frequent_level(logs)` that returns the log level that appeared the most

### Expected Output (example)

```
Grouped Logs: {'INFO': [...], 'WARNING': [...], 'ERROR': [...]}
Errors per date: {'2024-03-01': 2, '2024-03-02': 1}
Most frequent level: ERROR
```

---

## 🔷 Problem 2 — DSA: Task Scheduler using a Priority Queue

### Background

You are building a simple task scheduler. Each task has a **name**, a **priority** (lower number = higher priority), and a **duration** (in minutes).

### Tasks

1. Implement a **Min-Heap based Priority Queue** from scratch — **do not use `heapq` directly**; implement the heap logic manually using a list
2. Your heap must support:
   - `insert(task)` — insert a task as a tuple `(priority, name, duration)`
   - `extract_min()` — remove and return the highest priority (lowest number) task
   - `peek()` — return the highest priority task without removing it
   - `is_empty()` — return `True` if the queue is empty
3. Using your Priority Queue, simulate processing the following tasks **in priority order** and print each task as it is processed:

```python
tasks = [
    (3, "Send weekly report", 15),
    (1, "Fix critical bug", 45),
    (2, "Code review", 30),
    (1, "Deploy hotfix", 20),
    (4, "Update documentation", 60),
]
```

### Expected Output (example)

```
Processing: Fix critical bug  | Priority: 1 | Duration: 45 mins
Processing: Deploy hotfix     | Priority: 1 | Duration: 20 mins
Processing: Code review       | Priority: 2 | Duration: 30 mins
Processing: Send weekly report| Priority: 3 | Duration: 15 mins
Processing: Update docs       | Priority: 4 | Duration: 60 mins
```

> **Hint:** When two tasks have the same priority, process the one inserted first (FIFO within same priority).

---

## 🔷 Problem 3 — OOP: Library Management System

### Background

Design a mini **Library Management System** using OOP principles.

### Requirements

#### Class: `Book`
| Attribute / Method | Description |
|---|---|
| `title`, `author`, `isbn` | Basic book info |
| `is_available` | Boolean, default `True` |
| `__str__` | Readable string representation |
| `__repr__` | Developer-friendly representation |

#### Class: `Member`
| Attribute / Method | Description |
|---|---|
| `name`, `member_id` | Member info |
| `borrowed_books` | List, default empty |
| `borrow_book(book)` | Adds book to borrowed list if available; raise exception if not |
| `return_book(book)` | Removes book from borrowed list |
| `__str__` | Readable string representation |

#### Class: `Library`
| Attribute / Method | Description |
|---|---|
| `name` | Library name |
| `books` | List of `Book` objects |
| `members` | List of `Member` objects |
| `add_book(book)` | Add a Book to the library |
| `register_member(member)` | Register a Member |
| `search_by_author(author)` | Return all books by that author |
| `available_books()` | Return all currently available books |
| `borrow_book(member_id, isbn)` | Handle the borrow transaction; update availability |
| `return_book(member_id, isbn)` | Handle the return transaction; update availability |

### Tasks

1. Implement all three classes with the above specifications
2. Demonstrate the system with the following scenario:
   - Create a library with at least **5 books** and **2 members**
   - Member 1 borrows 2 books
   - Member 2 tries to borrow a book **already taken** → handle the exception gracefully
   - Member 1 returns one book
   - Member 2 successfully borrows that returned book
   - Print **available books at each key step**

---

## 📊 Grading Rubric

| Criteria | Marks |
|---|---|
| Problem 1 — Correctness & use of Python builtins | 20 |
| Problem 2 — Heap implementation & simulation | 30 |
| Problem 3 — OOP design, exception handling, flow | 30 |
| Code quality (comments, naming, structure) | 10 |
| Notebook clarity (markdown cells, output visible) | 10 |
| **Total** | **100** |

---

## ⚠️ Rules

- No use of external libraries — only `datetime` and standard Python builtins are allowed
- **Do not** use the `heapq` module for Problem 2
- All code must be **your own** — discussion is encouraged, copying is not
- Notebooks with **no visible output** (i.e., cells not run) will be penalised

---

## 📅 Deadline

**To be announced by your mentor.**

---

Good luck! Reach out on the group if you're stuck — asking good questions is part of the learning. 🚀
