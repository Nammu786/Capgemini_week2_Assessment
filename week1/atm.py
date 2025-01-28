import random
amnt=random.randint(10000,30000)
def check_balance(acc_number,pin):
    acc_number=int(input("enter account number or atm card"))
    pin=int(input("enter pin"))
    if acc_number==123456789 and pin==2004:
        print(f'Your balance amount is :{amnt}')
        print("-----")
        return True
    else:
        print("Invalid credintials! please enter the correct details") 
        return False    
def deposit_money(name,acc_number):
    global amnt
    check_balance(123456789,2004)
    amount=int(input("enter the amount you wish to deposit: "))
    amnt+=amount
    print(f"Dear {name}, {amount} deposited into your account {acc_number}")
    print("Total Balance in your account are:",amnt)
    print("------")
deposit_money("namratha",123456789)
def withdraw_money():
    global amnt
    withdraw=int(input("enter the amount for withdrawl:"))
    if amnt<=1000 and withdraw>amnt:
        print("Insuffcient balance for withdrawl or Cannot be withdrawn for less than Rs.1000")
    else:
        amnt-=withdraw
        print(f" you amount {withdraw} is withdrawn from your savings account ")
    print(f'remaining balance: {amnt}')    
withdraw_money()
def exit():
    if str=="exit":
        print("thank you for using ATM")

