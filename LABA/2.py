class Wheels:
    def __init__(self, size, type_):
        self._size = size         
        self._type = type_

    def get_size(self):
        return self._size

    def get_type(self):
        return self._type


class Engine:
    def __init__(self, power, fuel_type):
        self._power = power
        self._fuel_type = fuel_type

    def get_power(self):
        return self._power

    def get_fuel_type(self):
        return self._fuel_type


class Doors:
    def __init__(self, count, is_locked):
        self._count = count
        self._is_locked = is_locked

    def get_count(self):
        return self._count

    def get_is_locked(self):
        return self._is_locked

    def set_is_locked(self, is_locked):
        self._is_locked = is_locked  # Сеттер для поля is_locked


class Car:
    def __init__(self, wheels, engine, doors):
        self.wheels = wheels
        self.engine = engine
        self.doors = doors

    def display_info(self):
        print("Автомобиль:")
        print(f"Колеса: размер - {self.wheels.get_size()}, тип - {self.wheels.get_type()}")
        print(f"Двигатель: мощность - {self.engine.get_power()}, тип топлива - {self.engine.get_fuel_type()}")
        print(f"Двери: количество - {self.doors.get_count()}, заблокированы - {self.doors.get_is_locked()}")


# Пример использования
wheels = Wheels(size=17, type_="Summer")
engine = Engine(power=150, fuel_type="Gasoline")
doors = Doors(count=4, is_locked=False)

car = Car(wheels=wheels, engine=engine, doors=doors)
car.display_info()

# Пример изменения состояния двери
doors.set_is_locked(True)
car.display_info()
