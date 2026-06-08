class Vehicle: 
    def __init__(self): 
        self._speed = 0
        self.__max_speed = 120
    def get_max_speed(self):
        return self.__max_speed

    def set_max_speed(self, value):
        if value > 0:
            self.__max_speed = value
        else:
            print("Максимальная скорость должна быть положительным числом.")

    def drive(self):
        print(f"Текущая скорость: {self._speed} км/ч")
        
class Car(Vehicle):
    def __init__(self, brand="Неизвестно"):
        super().__init__()
        self.brand = brand
        
    def drive(self):
        print(f"Машина {self.brand} движется со скоростью {self._speed} км/ч")
car1 = Car("Toyota")
car1.drive()
car1.set_max_speed(200)
print(f"Максимальная скорость машины {car1.brand}: {car1.get_max_speed()} км/ч")

class Bicycle(Vehicle):
    def __init__(self):
        super().__init__()
        
    def drive(self):
        print(f"Велосипед движется со скоростью {self._speed} км/ч")
bicycle1 = Bicycle()
bicycle1.set_max_speed(30) # ну чтобы по красоте было
bicycle1.drive()
print(f"Максимальная скорость велосипеда: {bicycle1.get_max_speed()} км/ч")