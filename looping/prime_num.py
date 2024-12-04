number=int(input("enter the number:"))
is_prime=True
for i in range(2,number,1):
    if number%i==0:
        is_prime=False
        break
print(is_prime)