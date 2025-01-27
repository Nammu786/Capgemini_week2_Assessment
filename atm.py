import random
amnt=random.randint(10000,30000)
def check_balance():
    acc_number=int(input("enter the account number:"))
    pin=int(input("enter the pin:"))
    if pin==2004 and acc_number==123456789:
        print(f'Your balance amount is :{amnt}')
        print("-----")
    else:
        print("Invalid credintials! please enter the correct details")   
def deposit_money(name,acc_number):
    check_balance()
    amount=int(input("enter the amount you wish to deposit: "))
    print(f"Dear {name}, {amount} deposited into your account {acc_number}")
    print("Total Balance in your account are:",amnt+amount)
    print("------")
deposit_money("namratha",123456789)
def withdraw_money():
    amount=int(input())
    if amount<=1000:
        print("Insuffcient balance for withdrawl")
    withdraw=int(input("enter the amount for withdrawl:"))
    print(f" you amount {withdraw} is withdrawn from your savings account")
withdraw_money()
def exit():
    if str=="exit":
        print("thank you for using ATM")

