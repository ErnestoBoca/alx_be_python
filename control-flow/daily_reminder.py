task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        type_note = "Reminder"
    case "medium":
        type_note = "Reminder"
    case "low":
        type_note = "Note"

       
if time_bound == "yes":
    print(f"{type_note}: '{task}' is a {priority} priority task that requires immediate attention today!")
else:
    print(f"{type_note}: '{task}' is a {priority} priority task. Consider completing it when you have free time.")