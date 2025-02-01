'''	13. Develop a `Shape` class with a method `area()`.
 Implement `Square` and `Triangle` classes that provide specific implementations for `area()`.'''

class Shape:
    def __init__(self,length):
        self.length=length
    def area(self):
        print("\nThe area of closed figures can be found")
class Square(Shape):
    def __init__(self, length):
        super().__init__(length)
    def square_area(self):
        print("\nThe area of square:",self.length**2)
        
class Triangle(Shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def triangle_area(self):
        print("\nThe area of Triangle:",0.5*self.base*self.height)

triangle=Triangle(2,5)
triangle.triangle_area()

square=Square(3)
square.square_area()