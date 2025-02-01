'''•	5. Create a `Product` class with attributes `name`, `price`, and `stock`.
        Write a method `check_availability(quantity)` that returns whether the requested quantity is available.'''
class Product:
    def __init__(self,name,price,stock):
        self.name=name
        self.price=price
        self.stock=stock
    def check_availability(self,quantity):
        self.quantity=quantity
        print(f"Product_name: {self.name}\nProduct_price:Rs. {self.price}\nStock: {self.stock}Kg\nQuantity needed: {self.quantity}Kg")
        if self.quantity<=self.stock:
            self.stock-=self.quantity
            print(f"The stock left is {self.stock}")
p=Product("rice",150,156)
p.check_availability(50)