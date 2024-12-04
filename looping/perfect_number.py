#perfect number
number=int(input("enter the number :"))#6
total=0
for i in range(1,number):
    if number%i==0:
        total=total+i
print("perfect" if total==number else "not perfect")
