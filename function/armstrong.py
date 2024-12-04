def is_armstrong_number(number):
    digit_count=len(str(number))

    total=0
    temp=number

    while (number!=0):

        digit=number%10

        exponent=digit**digit_count

        total=total+exponent

        number=number//10


    print(f"{temp} this is an amstrong number")

is_armstrong_number(153)