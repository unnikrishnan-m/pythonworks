def last_dig(num1,num2):
    n1=num1%10
    n2=num2%10

    print(num1 if n1>n2 else num2)

last_dig(123,125)