class Vehicle:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed
    def action(self):
        print(f"{self.brand} moves at {self.speed} km/h.")
class Car(Vehicle):
    def __init__ (self,brand, speed, doors):
        super().__init__(brand, speed)
        self.doors=doors
    def action(self):
        print(f"{self.brand} moves on the road with {self.doors} doors.")

class Boat(Vehicle):
    def __init__(self,brand, speed, type):
        super().__init__(brand, speed)
        self.type=type
    def action(self):
        print(f"{self.brand} {self.type} sails across the water at {self.speed} km/h.")
a=Car("BMW M5", 300, 4)
b=Boat("Yamaha", 80, "Speedboat")
c=Vehicle("Generic Vehicle", 100)
a.action()
b.action()
c.action()
    