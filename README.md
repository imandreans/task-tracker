# Task Tracker CLI
This project helps you to track and manage your tasks with command line interface (CLI). Python is used to build the features and the tasks is stored in JSON file. Each tasks have the following properties:
1. id: A unique identifier for the task
2. description: A short description of the task
3. status: The status of the task (todo, in-progress, done)
4. createdAt: the date and time when the task was created
5. updatedAt: the date and time when the task was last updated
# Features
1. Add Task: Add new task
2. Delete Task: Delete existing task
3. Update Task: Update task with new description
4. Mark In Progress: Mark task as In Progress
5. Mark Done: Mark task as Done
6. List Task: List all tasks or list tasks that are not done, in progress, or done
# Getting Started
```
git clone https://github.com/imandreans/task-tracker.git
cd task-tracker
python3 task-tracker-cli.py
```
# Use the Task Tracker
```
task-cli add coding 
task-cli delete 1
task-cli update 2 exercise
task-cli mark_in_progress 2
task-cli mark_done 3
task-cli list
task-cli list in-progress
```
The id of the task must be assigned to delete, update, and change its status. To list the tasks based on its status, you can add the status after the command `list`. 

---
This project is available in https://roadmap.sh/projects/task-tracker
