i=0
n=int(input("enter number of loops needed:"))
while i<n:
    num=input("Enter a string or number:")
    num1=num[::-1]
    if num==num1:
        print(f"{num} is palindrome")
    else:
        print(f"{num} is not a palindrome")    
    i+=1
