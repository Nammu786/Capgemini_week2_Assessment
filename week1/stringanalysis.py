string=input()
count,cnt,c,c1=0,0,0,0
vowels=['a','e','i','o','u']
consonants=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
special_characters=['!','@','$','&','*','#','^']
for str in string:
    if str in vowels:
        print(str,end=",")
        count+=1
print("The number of vowels in the string are",count)
for str in string:
    if str in consonants:
        print(str,end=",")
        cnt+=1
print("The number of consonants in the string are",cnt)
for str in string:
    if str.isdigit()==True:
        print(str,end=",")
        c+=1
print("The number of digits in the string are ",c) 
for str in string:
    if str in special_characters:
        print(str,end=",")
        c1+=1
print("The number of special characters in the string are",c1)        

