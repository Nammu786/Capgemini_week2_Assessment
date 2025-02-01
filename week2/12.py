''' Write a `Payment` class with a method `process_payment()`. 
Implement subclasses `CreditCardPayment`, `PayPalPayment`, and `BitcoinPayment` that override the method differently.'''

class Payment:
    def process_payment(self):
        print("payment is done through any way either through cash or online")
class CreditCardPayment(Payment):
    def process_payment(self):
        print("Payment is done through creditcard")
class PaypalPayment(Payment):
    def process_payment(self):
        print("Payment is done through UPI")
class BitcoinPayment(Payment):
    def process_payment(self): 
        print("Payment is made via Bitcoin change")   
credit=CreditCardPayment()
credit.process_payment()

pay=PaypalPayment()
pay.process_payment()

bit=BitcoinPayment()
bit.process_payment()



