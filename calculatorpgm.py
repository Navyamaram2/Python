operator=input("enter an operator(+,-,%,/,*):")
num1=int(input("enter a first number:"))
num2=int(input("enter a secound number:"))
if operator == "+":
    res=num1+num2
    print(res)
elif operator == "-":
    res=num1-num2
    print(res)
elif operator == "*":
    res=num1*num2
    print(res)
elif operator == "/":
    res=num1/num2
    print(res)
elif operator == "%":
    res=num1%num2
    print(res)
else:
    print(f"{operator} is not a valid operator")


    