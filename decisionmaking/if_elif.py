#read number
#print fizz if num/by 3
#print buzz if num/by 5
#print fizzbuzz if num/by 15
#defult invalid number

num=int(input("enter thew number"))

if num%15==0:

    print("fizzbuzz")

elif num%5==0:

    print("buzz")

elif num%3==0:

    print("fizz")

else:

    print("invalid number")
    
