number=int(input("entaer the number"))

total=0

while(number!=0):

    digit=number%10
    sqr=digit*digit#total=digit**2
    total=total+sqr
    number=number//10

print(total)    