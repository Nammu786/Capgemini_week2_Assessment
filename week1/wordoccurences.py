str=input("Enter a sentence: ").split()
result={}
count=0
for s in str:
    s=s.lower()
    if s in result:
        result[s]+=1
    else:
        result[s]=1  
print("The word occurences in sentence:",result)     

