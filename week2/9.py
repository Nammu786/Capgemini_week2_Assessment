'''	9. Simulate multiple inheritance where `FlyingCar` inherits from
 both `Car` and `defAirplane`. Handle potential conflicts in the `move()` method.'''

class Car:
    def c_move(self):
        print("Car moves on the road")
class Airplane:
    def p_move(self):
        print("plane moves in the air")
class FlyingCar(Car,Airplane):
    def move(self):
        print("FlyingCar can have both properties")
flyingcar=FlyingCar()
flyingcar.move()
flyingcar.c_move()
flyingcar.p_move()