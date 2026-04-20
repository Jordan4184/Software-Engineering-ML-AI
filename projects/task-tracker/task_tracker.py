## CLI task manager inteded to serve as a reminder of todays tasks. Includes adding tasks, editing, and deleting tasks

## Initiate list of to-do's 
todo_list = []
print("Enter your tasks (type 'quit' to stop):")

## Core Logic
while True:
    task = input("> ")
    if task.lower() == 'quit':
        break
    todo_list.append(task)

## Print statement:
print("Your To-Do List:", todo_list)

#Saving a Task to JSON

## Editing a Task

## Deleting a Task