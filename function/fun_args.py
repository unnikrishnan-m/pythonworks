def add_numbers(*args):

    result=0

    for num in args:

        result=result+num
        
    print(args)

add_numbers(10,20)

add_numbers(10,20,30)
