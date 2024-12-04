# Read three number print second largest number

num1=int(input("enter the first number => "))

num2=int(input("enter the second number => "))

num3=int(input("enter the third number => "))

if num1>num2 and num1>num3:

    
    if num2>num3:

        print("num2 is scnd largest")

    else:

        print("num3 is scnd largest")    

elif num2>num1 and num2>num3:

    if num1>num3:

        print("num1 scnd is largest")

    else:

     print("num3 scnd is largest")

elif  num3>num1 and num3>num2:

    if num1>num2:

     print("num1 is scnd largest")   

    else:
    
     print("num2 is scnd largest")

      
