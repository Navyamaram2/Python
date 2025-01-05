principal=0
rate=0
time=0
while True:
    principal=float(input("enter a principal value:"))
    if principal == 0:
        print("principal can't be zero")
    else:
        break
while True:
    rate=float(input("enter a rate value:"))
    if rate== 0:
        print("rate can't be zero")
    else:
        break
while True:
    time=float(input("enter a time value:"))
    if principal == 0:
        print("time can't be zero")
    else:
        break
result=round((principal*pow((1+rate/100),time)),1)
print(result)

