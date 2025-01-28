import random
while True:
    num=random.randint(0,100)
    print("the computer generated number is:",num)
    if num >100 or num <1:
        print("enter correct number")
    user_input=int(input("enter user_input: "))
    if user_input==num:
        print("Your guess is correct")
    elif user_input<num:
        print("Your Guess is too low")
    elif user_input>num:
        print("Your Guess is Too high")
    str1=input("exit/stay")      
    if str1=="exit":
        break

