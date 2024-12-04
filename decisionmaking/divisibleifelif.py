# read a number
#print fizz if num by 3
#print buzz if num by 5
#print fizzbuzz if num by 15
#default invALID NUMBER

num=int(input("enter the value"))

if num%15==0:
    print("fizz")

elif num%5==0:
    print("buzz")

elif num%3==0:
    print("fizzbuzz")

else:
    print("invalid")