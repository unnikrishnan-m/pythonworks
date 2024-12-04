def factorial(num):
    f = 1
    i = 1
    while(i <= num):
        f *= i
        i+=1
    return f
print(factorial(3))