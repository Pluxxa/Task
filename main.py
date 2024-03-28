from datetime import datetime

class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        status = "выполнено" if self.completed else "не выполнено"
        deadline_str = self.deadline.strftime("%d.%m.%Y")
        return f"Описание: {self.description}, Срок выполнения: {deadline_str}, Статус: {status}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_as_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_as_completed()

    def list_current_tasks(self):
        current_tasks = [task for task in self.tasks if not task.completed]
        if current_tasks:
            print("Текущие задачи:")
            for index, task in enumerate(current_tasks):
                print(f"{index + 1}. {task}")
        else:
            print("Нет текущих задач.")

# Пример использования
task_manager = TaskManager()

# Добавляем задачи с использованием объектов datetime для сроков выполнения
task_manager.add_task(Task("Погулять с собакой", datetime(2024, 3, 28)))
task_manager.add_task(Task("Подготовить отчет", datetime(2024, 3, 29)))
task_manager.add_task(Task("Сделать упражнения по программированию", datetime(2024, 3, 30)))

# Выводим текущие задачи
task_manager.list_current_tasks()

# Отмечаем первую задачу как выполненную
task_manager.mark_task_as_completed(0)

# Выводим текущие задачи после выполнения первой
task_manager.list_current_tasks()
