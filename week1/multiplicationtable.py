num=int(input("enter a number to generate a multiplication:"))
start=int(input("enter start of the range:"))
end=int(input("enter end of the range:"))
for i in range(start,end+1):
    print(f'{num}*{i}={num*i}')
        