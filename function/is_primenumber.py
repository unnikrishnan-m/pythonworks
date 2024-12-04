# create a function is_prime(num)

def is_prime(num):

    is_prime_number=True

    for i in range(2,num):

       if num%i==0:
           
           is_prime_number=False

    print(is_prime_number)

print(is_prime=(5))


