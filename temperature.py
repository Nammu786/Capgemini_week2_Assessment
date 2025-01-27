temp_type=input("enter type of Temperature: ")
temperature=int(input("Enter Temperature: "))

def Fahrenheit(temp_type,temperature):
    if temp_type=="Fahrenheit":
        print("the conversion from fahrenheit to celsius :")
        a=(temperature-32)*(5/9)
        print(a)
        print("the conversion from fahrenheit to kelvin:")
        b=(temperature-32)*(5/9)+273.15
        print(b)
Fahrenheit(temp_type,temperature)

def Celsius(temp_type,temperature):       
    if temp_type=="Celsius":
        print("the conversion from  celsius to fahrenheit :")
        c=temperature*(9/5)+32
        print(c)
        print("the conversion from  celsius to Kelvin :")
        d=temperature+273.15
        print(d)
Celsius(temp_type,temperature)

def Kelvin(temp_type,temperature):
    if temp_type=="Kelvin":
        print("the conversion from Kelvin to celsius: ")
        e=temperature-273.15
        print(e)
        print("the conversion from Kelvin to Fahrenheit:")
        f=(temperature-273.15)*(9/5)+32
        print(f)
Kelvin(temp_type,temperature)    
