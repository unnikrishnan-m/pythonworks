#print the last digit of an input value is even

num=int(input("enter the value:"))

last_digit=num%10

is_even=last_digit%2==0

print(is_even)