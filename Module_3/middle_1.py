class Vehicle: 
    def __init__(self): 
        self._speed = 0
        self.__max_speed = 120

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