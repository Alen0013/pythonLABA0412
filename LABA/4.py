class Employer:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def print_info(self):
        print("This is Employer class")
        print(f"Name: {self.first_name} {self.last_name}, Age: {self.age}")

class President(Employer):
    def print_info(self):
        super().print_info()
        print("Position: President")
        print("Responsibilities: Overseeing the entire organization.")

class Manager(Employer):
    def print_info(self):
        super().print_info()
        print("Position: Manager")
        print("Responsibilities: Managing teams and projects.")

class Worker(Employer):
    def print_info(self):
        super().print_info()
        print("Position: Worker")
        print("Responsibilities: Performing specific tasks within the organization.")

# Примеры использования
president = President("John", "Doe", 50)
manager = Manager("Jane", "Smith", 40)
worker = Worker("Mike", "Johnson", 30)

president.print_info()
print()  
manager.print_info()
print()
worker.print_info()
