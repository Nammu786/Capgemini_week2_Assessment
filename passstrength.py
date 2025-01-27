upper,lower,digit,schar=0,0,0,0
password=input("enter a pass to check for strength:")
for p in password:
    if p.isupper():
        upper+=1             
    if p.islower():
        lower+=1 
    if p.isdigit():
        digit+=1
    if p=='@'or p=='$'or p=='&' or p=='!'or p=='^':
        schar+=1
if upper>=1 and lower>=1 and digit>=1 and len(password)>=8 and schar>=1:
    print("strong Password")
else:
    print("Weak Password")
        

