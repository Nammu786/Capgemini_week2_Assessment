'''
•	2. Design a `BankAccount` class with `deposit()` and `withdraw()` methods. 
      Implement logic to prevent overdraft.'''

class BankAccount:
    def __init__(self,amount):
        self.amount=amount
    def deposit(self,deposit):
        self.deposit=deposit
        self.amount+=deposit
        print("Total amount 10:",self.amount)
    def withdraw(self,withdraw_amt):
        self.withdraw_amt=withdraw_amt
        if withdraw_amt>self.amount:
            print("Amount is insufficient")
        else:
            self.amount-=self.withdraw_amt
            print("The remaining balance is:",self.amount)
b=BankAccount(int(input("Balance in the account:")))
b.deposit(int(input("enter amount to be deposited:")))
b.withdraw(int(input("Enter amount to be withdrawn:")))