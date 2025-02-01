'''Polymorphism
•	11. Create a class `Logger` with a method `log(message)`. 
Implement method overloading to log different message types (`error`, `warning`, `info`).'''

class Logger:
    def log(self,message):
        if message=="error":
            print("Error Type Message")
        elif message.lower()=="warning":
            print("Warning Type Message")
        elif message.lower()=="info":
            print("Informative Type Message")
        else:
            print("It is a message")
l=Logger()
l.log(input("enter message:"))