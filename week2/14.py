''' 14. Implement method overriding for a `Notification` class .
where `send()` is overridden in `EmailNotification` and `SMSNotification`.'''

class Notification:
    def send(self,message):
        self.message=message
        print("notification received:",self.message)
class EmailNotification(Notification):
    def send(self,message):
        self.message=message
        print("Email notification received",self.message)
class SMSNotification(Notification):
    def send(self,message):
        self.message=message
        print("SMS Notification Received:",self.message)
        print()
smsnotification=SMSNotification()
smsnotification.send("\nDue Alert! your 90% data usage is completed")

emailnotification=EmailNotification()
emailnotification.send("\nCapgemini Exceller :Job openinigs")