def is_perfect_number(number):
    total=0
    for i in range(1,number):
         if number%i==0:
            total=total+i
print(is_perfect_number(6))
