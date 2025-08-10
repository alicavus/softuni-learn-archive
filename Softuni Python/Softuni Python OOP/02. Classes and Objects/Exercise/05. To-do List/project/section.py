from project.task import Task

class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []
    
    def add_task(self, new_task: Task) -> str:
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks += [new_task]
        return f"Task {new_task.details()} is added to the section"
    
    def complete_task(self, task_name: str) -> str:
        for idx, task in enumerate(self.tasks):
            if task.name == task_name:
                self.tasks[idx].completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"
    
    def clean_section(self) -> str:
        cleared: int = 0
        for idx in range(len(self.tasks) - 1, -1, -1):
            if self.tasks[idx].completed == True:
                del self.tasks[idx]
                cleared += 1
        return f"Cleared {cleared} tasks."
    
    def view_section(self) -> str:
        result = [f"Section {self.name}:"]
        for task in self.tasks:
            result += [task.details()]
        return "\n".join(result)
