'''•19. Develop an interface `IVehicle` with abstract methods `start_engine()` and `stop_engine()`. 
Implement it in `Car`, `Bike`, and `Truck` classes.'''

from abc import ABC,abstractmethod
class IVehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def stop_engine(self):
        pass
class Car(IVehicle):
    def start_engine(self):
        print("Car Engine Started")
    def stop_engine(self):
        print("Car Engine Stopped")
class Bike(IVehicle):
    def start_engine(self):
        print("\nBike engine Started")
    def stop_engine(self):
        print("Bike engine Stopped")
class Truck(IVehicle):
    def start_engine(self):
        print("\nTruck engine Started")
    def stop_engine(self):
        print("Truck Engine Stopped")
car=Car()
car.start_engine()
car.stop_engine()

bike=Bike()
bike.start_engine()
bike.stop_engine()

truck=Truck()
truck.start_engine()
truck.stop_engine()