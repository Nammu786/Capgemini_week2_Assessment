num=int(input("enter number for iterating loop:"))
for i in range(num):
    def factorial(n):
        if n<0:
            print("Error! Negative numbers cannot handle factorial")
        if n==0 or n==1:
            return 1
        if n>=2:
            return n*factorial(n-1)
    n=int(input())
    print(f"The factorial of {n} is",factorial(n))