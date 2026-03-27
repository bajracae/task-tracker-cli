import datetime
import json
import uuid

class TaskTracker:
    def __init__(self):
        pass

    def get_tasks_from_file(self):
        with open("task_cli/tasks.json") as file:
            data = json.load(file)
        return list(data)

    def add_tasks_in_file(self, tasks):
        with open("task_cli/tasks.json", "w", encoding="utf-8") as file:
            json.dump(tasks, file, ensure_ascii=False, indent=4)

    def _list(self, filter):
        current_tasks = self.get_tasks_from_file()
        if not filter:
            return [task for task in current_tasks]
        return [task for task in current_tasks if task.get("status") == filter]
        
    def add(self, new_description):
        current_tasks = self.get_tasks_from_file()
        current_timestamp = datetime.datetime.now().isoformat()
        new_task = {
            "id": str(len(current_tasks) + 1),
            "description": new_description,
            "status": "todo",
            "createdAt": current_timestamp,
            "updatedAt": current_timestamp
        }
        current_tasks.append(new_task)
        self.add_tasks_in_file(current_tasks)
        
    def update(self, task_id, new_description):
        current_timestamp = datetime.datetime.now().isoformat()
        current_tasks = self.get_tasks_from_file()
        for task in current_tasks:
            if task.get("id") == task_id:
                task["description"] = new_description
                task["updatedAt"] = current_timestamp
                break
        self.add_tasks_in_file(current_tasks)

    def delete(self, task_id):
        current_tasks = self.get_tasks_from_file()
        new_tasks = [task for task in current_tasks if not (task.get("id") == task_id)]
        self.add_tasks_in_file(new_tasks)

    def update_status(self, task_id, new_status):
        current_timestamp = datetime.datetime.now().isoformat()
        current_tasks = self.get_tasks_from_file()
        for task in current_tasks:
            if task.get("id") == task_id:
                task["status"] = new_status
                task["updatedAt"] = current_timestamp
                break
        self.add_tasks_in_file(current_tasks)
