'''
Interface (Using Abstract Base Classes - ABC)
16. Create an interface `IShape` with an abstract method `calculate_area()`. Implement it in `Rectangle` and `Circle` classes.'''

from abc import ABC,abstractmethod
class IShape:
    # def __init__(self,length,breadth):
    #     self.length=length
    #     self.breadth=breadth
    #pi=3.14
    @abstractmethod
    def calculate_area():
        pass
class Rectangle(IShape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def calculate_area(self):
        print(f'the area of Rectangle: {self.length*self.breadth}')
        print()
class Circle(IShape):
    def __init__(self,radius):
        self.radius=radius
    def calculate_area(self):
        print(f'the area of Circle: {3.14*self.radius**2}')
        print()
circle=Circle(int(input("Enter radius:")))
circle.calculate_area()

rectangle=Rectangle(int(input("Enter length:")),int(input("Enter breadth:")))
rectangle.calculate_area()