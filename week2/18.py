'''•18. Implement an abstract class `ICalculator` with methods `add()`, `subtract()`, `multiply()`, and `divide()`. 
Create a `BasicCalculator` class that implements these methods.'''

from abc import ABC,abstractmethod
class Icalculator(ABC):
    @abstractmethod
    def add(self):
        pass
    @abstractmethod
    def subtract(self):
        pass
    @abstractmethod
    def multiply(self):
        pass
    @abstractmethod
    def divide(self):
        pass
    
class BasicCalculator(Icalculator):
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        self.result=self.num1+self.num2
        print(f"The addition of {self.num1} & {self.num2}:",self.result)
    def subtract(self):
        self.result=self.num1-self.num2
        print(f"The subtraction of {self.num1} &{self.num2}:",self.result)
    def multiply(self):
        self.result=self.num1*self.num2
        print(f"The multiplication of {self.num1} & {self.num2}:",self.result)
    def divide(self):
        self.result=self.num1/self.num2
        print(f"The addition of {self.num1} & {self.num2}:",self.result)
basiccalci=BasicCalculator(10,20)
basiccalci.add()
basiccalci.subtract()
basiccalci.multiply()
basiccalci.divide()