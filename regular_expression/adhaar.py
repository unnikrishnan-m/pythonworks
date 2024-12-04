from re import fullmatch

pattern="[0-9]{12}"

user_input=input("enter the number")

matcher=fullmatch(pattern,user_input)

if matcher==None:

    print("invalid")

else:

    print("valid")

