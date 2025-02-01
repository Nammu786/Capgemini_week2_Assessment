'''Inheritance (Multiple, Multi-Level)

•	6. Implement a multi-level inheritance example 
where `Vehicle` is a base class, `Car` and `Bike` inherit from `Vehicle`, and `ElectricCar` inherits from `Car`.'''

class Vehicle:
    def __init__(self,wheels,seats):
        self.seats=seats
        self.wheels=wheels
    def types(self):
        print("I have all types of vehicles")
class Bike(Vehicle):
    def __init__(self, wheels, seats,name,version):
        super().__init__(wheels, seats)
        self.name=name
        self.version=version
    def bike_method(self):
        print("Bike Details:")
        print(f"Bike name: {self.name}\nVersion:{self.version}\nNo.ofwheels: {self.wheels}\n No.of Seats:{self.seats}\n")
        print()
class Car(Vehicle):
    def __init__(self, wheels, seats,name,version):
        super().__init__(wheels, seats)
        self.name=name
        self.version=version
    def car_method(self):
        print("Car details:")
        print(f"Car name: {self.name}\nVersion:{self.version}\nNo.ofwheels: {self.wheels}\nNo.of Seats:{self.seats}\n")
        print()
class ElectricCar(Car):
    def __init__(self, wheels, seats, name, version,battery,capacity):
        super().__init__(wheels, seats, name, version)
        self.battery=battery
        self.capacity=capacity
    def electric(self):
        print("Electric Car Details:")
        print(f"Electiric Car name: {self.name}\nVersion:{self.version}\nNo.ofwheels: {self.wheels}\nNo.of Seats:{self.seats}\nBattery:{self.battery}%\nCapacity:{self.capacity}hrs")
        print()

b=Bike(2,1,"ktm",3.8)
b.bike_method()

c=Car(4,7,"motorola",8.2)
c.car_method()

ec=ElectricCar(4,5,"maruthi",11.4,80,3)
ec.electric()




        

    



