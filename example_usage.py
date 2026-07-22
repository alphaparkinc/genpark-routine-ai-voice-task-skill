from client import RoutineAiVoiceTaskClient
client = RoutineAiVoiceTaskClient()
tasks = [
    {"id": "T001", "title": "Review Q3 roadmap", "status": "todo", "priority": "high"},
    {"id": "T002", "title": "Send investor update", "status": "todo", "priority": "high"},
]

# Add a new task
result1 = client.parse_and_act("Add prepare demo slides for Thursday", tasks)
print(f"[{result1['parsed_action']}] {result1['response']}")

# List pending tasks
result2 = client.parse_and_act("Show my pending tasks", result1["updated_tasks"])
print(f"[{result2['parsed_action']}] {result2['response']}")
