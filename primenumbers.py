'''printing primes in range'''
# start=int(input("enter start number"))
# end=int(input("enter end number"))
# for i in range(start,end+1):
#     if i<=1:
#         print(f"{i}is not a prime")
#     for j in range(start,i//2+1):
#         if i%j==0:
#             break
#     else:
#         print(i,end=",")      

'''checking prime or not'''

def check_prime(num):
    if num<1:
        print(f"{num} not a prime")
    for i in range(2,num//2+1):
        if(num%i==0):
            print(f"{num} not a prime")    
            return
    print(f"{num} a prime")
check_prime(10)