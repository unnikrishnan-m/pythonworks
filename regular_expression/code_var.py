#starting with an alphabet from p-t

#in second place must be a number this is is \ by 3

# followed by anynumber alphabets,number,@


from re import fullmatch

pattern="[p-tP-T][369][a-zA-Z0-9@]*"

user_input=input("enter variable name")

matcher=fullmatch(pattern,user_input)

if matcher==None:

    print("invalid")

else:

    print("valid")