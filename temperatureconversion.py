unit=input("is this tempearture in celsius or fahrenheit(C/F)")
temp=int(input("enter a tempearture :"))
if unit=="C":
    res=round((temp*9/5+32),1)
    print(f"{temp}C is {res}F")
elif unit=="F":
    res=round(((temp-32)*5/9),1)
    print(f"{temp}F is {res}C")
else:
    print(f"{unit} is invalid unit")