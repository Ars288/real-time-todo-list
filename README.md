# Real-Time To-Do List with Notifications ✅

## Description
A command-line to-do list application that sends you reminders to keep you organized and on top of your tasks.

## Why It's Productive
- **Stay Organized**: Keep track of tasks and deadlines.
- **Automate Reminders**: Get notified about upcoming tasks.

## Features
- Add, remove, and view tasks.
- Set deadlines for tasks.
- Receive notifications at set times.

## Requirements
- **Libraries**: `schedule` for timing, `time`, and `plyer` for notifications.

## Getting Started

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/real-time-todo-list.git
    cd real-time-todo-list
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required libraries**:
    ```bash
    pip install schedule plyer
    ```

### Create Task Management Functions
- Implement functions to add, remove, and display tasks.

### Implement Scheduling
- Use `schedule` to set up reminders.

### Send Notifications
- Use `plyer` to show system notifications.

## Usage

1. **Run the application**:
    ```bash
    python app.py
    ```

2. **Add Tasks**:
    - Follow the prompts to add tasks with deadlines.

3. **Receive Notifications**:
    - Get notified about upcoming tasks based on the schedule you set.

## Example

Here's a simple example to get you started:

```python
import schedule
import time
from plyer import notification

tasks = []

def add_task(task, deadline):
    tasks.append((task, deadline))

def notify_task(task):
    notification.notify(
        title='Task Reminder',
        message=task,
        timeout=10
    )

def check_tasks():
    current_time = time.strftime("%H:%M")
    for task, deadline in tasks:
        if current_time == deadline:
            notify_task(task)

schedule.every().minute.do(check_tasks)

add_task("Finish project", "13:00")
add_task("Attend meeting", "14:00")

while True:
    schedule.run_pending()
    time.sleep(1)
