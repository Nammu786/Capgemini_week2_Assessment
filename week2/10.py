'''10. Build a `SmartPhone` class inheriting from `MobileDevice`, 
which in turn inherits from `Electronics`. Demonstrate method overriding and attribute reuse.'''

class Electronics:
    def __init__(self,cost):
        self.cost=cost
    def type(self):
        print("Different electonic gadgets are present here")
class Mobiledevice(Electronics):
    def __init__(self,cost,typesofdevices):
        super().__init__(cost)
        self.typesofdevices=typesofdevices
    def type(self):
        super().type()
        print(f"There are different mobiles:\n Device name:{self.typesofdevices}\n Cost:{self.cost}")
class SmartPhone(Mobiledevice):
    def __init__(self, cost, typesofdevices,brand):
        super().__init__(cost, typesofdevices)
        self.brand=brand
    def type(self):
        super().type()
        print(f'the types of SmartPhones with cost are:\n Brand Name:{self.brand}\n cost:{self.cost}')

smartphone=SmartPhone(12000,"smartphone","VIVO")
mobiledevice=Mobiledevice(1000,"Nokia")
smartphone.type()