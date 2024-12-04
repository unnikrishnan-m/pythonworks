# Read two number and print largest number

num1=float(input("enter the first number => "))

num2=float(input("enter the second number => "))

if num1>num2:
  
    print(f"{num1} is largest number and {num2} is smallest number")

elif num2>num1:

    print(f"{num2} is largest number and {num1} is smallest number")

elif num1==num2:

    print(f" {num1} & {num2} these number are same2")

else:
    
    print("invalid")
