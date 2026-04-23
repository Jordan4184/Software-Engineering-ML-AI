## CLI task manager inteded to serve as a reminder of todays tasks. Includes adding tasks, editing, and deleting tasks
import json

## Initiate list of to-do's
todo_list = []
print("Enter your tasks (type 'quit' to stop):")

## Core Logic
while True:
    task = input("> ")
    if task.lower() == "quit":
        break
    todo_list.append(task)

## Print statement:
print("Your To-Do List: \n")

# Saving a Task to JSON
data = todo_list

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

with open("data.json", "r") as infile:
    data = json.load(infile)

for i, todo in enumerate(todo_list, 1):
    print(f"{i}. {todo}")
## Editing a Task

## Deleting a Task

