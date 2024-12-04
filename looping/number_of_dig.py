num=int(input("enter the number"))
rem=0
count=0
while(num!=0):
    rem=num%10
    count=count+1
    num//=10
print(count)




