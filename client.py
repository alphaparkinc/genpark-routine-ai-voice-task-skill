class RoutineAiVoiceTaskClient:
    def parse_and_act(self, voice_command: str, current_tasks: list) -> dict:
        cmd = voice_command.lower()
        tasks = list(current_tasks)

        if any(kw in cmd for kw in ["add", "create", "new", "remind"]):
            # Extract task name after command keyword
            words = voice_command.split()
            task_name = " ".join(w for w in words if w.lower() not in ["add", "create", "new", "remind", "me", "to", "a"]).strip()
            new_task = {"id": f"T{len(tasks)+1:03d}", "title": task_name, "status": "todo", "priority": "medium"}
            tasks.append(new_task)
            return {"parsed_action": "ADD_TASK", "updated_tasks": tasks, "response": f"Added task: '{task_name}'"}

        elif any(kw in cmd for kw in ["complete", "done", "finish", "check off"]):
            words = cmd.split()
            for task in tasks:
                if any(w in task["title"].lower() for w in words if len(w) > 3):
                    task["status"] = "done"
                    return {"parsed_action": "COMPLETE_TASK", "updated_tasks": tasks, "response": f"Marked '{task['title']}' as complete!"}
            return {"parsed_action": "COMPLETE_TASK", "updated_tasks": tasks, "response": "No matching task found to complete."}

        elif any(kw in cmd for kw in ["show", "list", "what", "pending"]):
            pending = [t for t in tasks if t.get("status") != "done"]
            names = ", ".join(t["title"] for t in pending[:3])
            return {"parsed_action": "LIST_TASKS", "updated_tasks": tasks, "response": f"You have {len(pending)} pending tasks: {names}"}

        else:
            return {"parsed_action": "UNKNOWN", "updated_tasks": tasks, "response": "I didn't catch that. Try: 'Add [task]', 'Complete [task]', or 'Show my tasks'."}
