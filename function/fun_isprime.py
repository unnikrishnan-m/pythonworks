def is_prime(num):
    for i in range(2,num,1):
        if num%i==0:
            print("false")
    else:
        print("true")
is_prime(7)