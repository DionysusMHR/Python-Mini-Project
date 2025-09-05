import csv


class Task:
    def __init__(self, name, description, priority):
        self.name = name
        self.description = description
        self.priority = priority



class ToDoList:

    def __init__(self):
        self.tasks = list()

    def add_task(self, task:Task):
        self.tasks.append([task.name, task.description, task.priority])

    def del_task(self, id):
        try:
            del self.tasks[id-1]
        except IndexError:
            print("This Id is not found!")

    def show_to_do(self):
        print("\nid | name | description | priority\n")
        for i in range(len(self.tasks)):
            print(f"{i+1} | {self.tasks[i][0]} | {self.tasks[i][1]} | {self.tasks[i][2]}")
    
    def save_tasks(self):
        with open("tasks.csv", 'w') as fout:
            writer = csv.writer(fout)
            writer.writerows(self.tasks)
    
    def load_tasks(self):
        try:
            with open("tasks.csv", "r") as fin:
                reader = csv.reader(fin)
                self.tasks = list(reader)
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    
    to_do_list = ToDoList()
    to_do_list.load_tasks()
    
    welcome_text = '''
--Welcome to To_Do_List--
*Organize your tasks
*Manage your time
*Achieve your goals
'''
    print(welcome_text)
    print("Command Guide:")
    print("add   del   show   save   exit")

    while True:
        cmd = input("--> ")

        if cmd not in ['exit', 'add', 'show', 'save', 'del']:
            print('You entered an incorrect prompt.')
            print('It should include the following:')
            print('add   del   show   save   exit')   
        
        elif cmd == 'exit':
            break

        elif cmd == 'add':
            name = input("name task: ")
            desc = input("description: ")
            priority = input("priority(high/intermediate/low): ")

            task = Task(name=name, description=desc, priority=priority)
            to_do_list.add_task(task)

        elif cmd == 'show':
            to_do_list.show_to_do()

        elif cmd == 'save':
            to_do_list.save_tasks()

        elif cmd == 'del':
            id = input('task id: ')
            to_do_list.del_task(int(id))
    