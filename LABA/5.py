class Employer:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def print_info(self):
        print("This is Employer class")

    def __str__(self):
        return f"Employer: {self.first_name} {self.last_name}, Age: {self.age}"

    def __int__(self):
        return self.age

    def get_age(self):
        return self.age


class President(Employer):
    def print_info(self):
        print(f"President: {self.first_name} {self.last_name}, Age: {self.age}")

    def __str__(self):
        return f"President: {self.first_name} {self.last_name}, Age: {self.age}"


class Manager(Employer):
    def print_info(self):
        print(f"Manager: {self.first_name} {self.last_name}, Age: {self.age}")

    def __str__(self):
        return f"Manager: {self.first_name} {self.last_name}, Age: {self.age}"


class Worker(Employer):
    def print_info(self):
        print(f"Worker: {self.first_name} {self.last_name}, Age: {self.age}")

    def __str__(self):
        return f"Worker: {self.first_name} {self.last_name}, Age: {self.age}"


# Пример использования
president = President("John", "Doe", 55)
manager = Manager("Jane", "Smith", 42)
worker = Worker("Mark", "Johnson", 28)

# Вывод информации
president.print_info()
manager.print_info()
worker.print_info()

# Вывод строкового представления
print(president)
print(manager)
print(worker)

# Вывод возраста с использованием int()
print(f"President's age: {int(president)}")
print(f"Manager's age: {int(manager)}")
print(f"Worker's age: {int(worker)}")
