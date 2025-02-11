import schedule
import time
from plyer import notification

tasks = []

def add_task(task, deadline):
    tasks.append((task, deadline))
    print(f"Task '{task}' added with deadline '{deadline}'")

def notify_task(task):
    print(f"Notification: {task}")
    notification.notify(
        title='Task Reminder',
        message=task,
        timeout=10
    )

def check_tasks():
    current_time = time.strftime("%H:%M")
    print(f"Checking tasks at {current_time}...")
    for task, deadline in tasks:
        if current_time == deadline:
            notify_task(task)

schedule.every(10).seconds.do(check_tasks)

add_task("Finish project", time.strftime("%H:%M", time.localtime(time.time() + 30)))
add_task("Attend meeting", time.strftime("%H:%M", time.localtime(time.time() + 60)))

print("Task scheduler started...")

while True:
    print("Running pending tasks...")
    schedule.run_pending()
    time.sleep(1)
