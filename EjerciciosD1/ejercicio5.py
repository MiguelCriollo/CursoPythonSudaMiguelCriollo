class ToDoManager:
    TASKS = {}

    def create_task(self):
        taskMessage=input("Ingrese el nombre de la tarea - > ")
        self.TASKS[len(self.TASKS)] = taskMessage
        print(f"Task <{taskMessage}> added!!")

    def delete_task(self):
        self.show_tasks()
        taskNumber = int(input("Ingrese el numero de tarea que quiere borrar"))
        print(f"Task <{self.TASKS[taskNumber]}> deleted!!")
        del self.TASKS[taskNumber]

    def show_tasks(self):
        print("Total tasks:")
        for index,task in enumerate(self.TASKS):
            print(f"#{index} -> {task}")


if __name__ == "__main__":
    manager = ToDoManager()

    manager.create_task()
    manager.show_tasks()
    manager.create_task()
    manager.delete_task()
    manager.show_tasks()
