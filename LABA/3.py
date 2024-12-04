class Pet:
    def __init__(self, name, breed, age):
        self._name = name          # приватное поле для имени
        self._breed = breed        # приватное поле для породы
        self._age = age            # приватное поле для возраста

    def get_sound(self):
        raise NotImplementedError("Этот метод должен быть переопределен в производном классе")

    def get_name(self):
        return self._name

    def get_type(self):
        return self._breed


class Dog(Pet):
    def __init__(self, name, breed, age):
        super().__init__(name, breed, age)

    def get_sound(self):
        print("Гав!")


class Cat(Pet):
    def __init__(self, name, breed, age):
        super().__init__(name, breed, age)

    def get_sound(self):
        print("Мяу!")


class Parrot(Pet):
    def __init__(self, name, breed, age):
        super().__init__(name, breed, age)

    def get_sound(self):
        print("Хлоп-хлоп!")


class Hamster(Pet):
    def __init__(self, name, breed, age):
        super().__init__(name, breed, age)

    def get_sound(self):
        print("Скрип-скрип!")


# Примеры использования
if __name__ == "__main__":
    my_dog = Dog("Рэкс", "Овчарка", 5)
    my_cat = Cat("Мурка", "Сиамская", 3)
    my_parrot = Parrot("Кеша", "Попугай", 2)
    my_hamster = Hamster("Хомка", "Золотистый", 1)

    for pet in [my_dog, my_cat, my_parrot, my_hamster]:
        print(f"Животное: {pet.get_name()}, Тип: {pet.get_type()}, Звук: ", end='')
        pet.get_sound()
