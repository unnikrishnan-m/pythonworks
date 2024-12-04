num=int(input("enter the number :"))
temp=num
rem=0
rev=0
while(num!=0):
    rem=num%10
    rev=rev*10+rem
    num//=10
if temp==rev:
    print(f"{temp}  number is palindrome ")

else:
    print(" is not palidrome")    




