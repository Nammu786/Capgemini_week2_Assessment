
'''•20. Write a scenario where a `UserAuthentication` interface contains `login()` and `logout()` methods, and 
it is implemented by `GoogleAuth` and `FacebookAuth` classes.'''
from abc import ABC,abstractmethod
class UserAuthentication(ABC):
    @abstractmethod
    def login(self,password):
        pass
    @abstractmethod
    def logout(self):
        pass
class GoogleAuth(UserAuthentication):
    username="abc@gmail.com"
    def login(self,password):
        self.password=password
        if password=="abc@1234":
            print("User logged into GOOGLE account")
        else:
            print("Wrong Password")
    def logout(self):
        print("User looged out from GOOGLE account")
class FacebookAuth(UserAuthentication):
    username="xyz@gmail.com"
    def login(self,password):
        if password=="xyz&789":
            print("User logged into Facebook via Google")
        else:
            print("wrong password")
    def logout(self):
        print("User logged from Account")

google=GoogleAuth()
google.login(input("\nEnter password :"))
google.logout()

facebook=FacebookAuth()
facebook.login(input("\nEnter password :"))
facebook.logout()