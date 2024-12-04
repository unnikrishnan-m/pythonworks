# Read threee number and find the largest number

num1=float(input("enter the first number => "))

num2=float(input("enter the second number => "))

num3=float(input("enter the third number => "))

if num1>num2>num3:

    print(f"first number {num1} is largest number ")

elif num1<num2>num3:

    print(f"second number {num2} is largest number ")

elif num1<num2<num3:

    print(f"third number {num3} is largest number ")

elif num1>num2==num3:

    print(f"first {num1} is largest number and balnce 2 numbers {num2}, {num3} are equal ")

elif num1==num2<num3:

    print(f"thir number {num3} is largest number and balnce 2 numbers {num1}, {num2} are equal")

elif num1==num2==num3:

    print(f" this three number are euqal")

elif num1==num3<num2:
    print(f"{num2} is largest and {num1} & {num3} are smallest and both numbers are equal")

elif num1==num3>num2:
    print(f"{num2} is smallest and {num1} & {num3} are largest and both numbers are equal")

else:

    print(" invalid")