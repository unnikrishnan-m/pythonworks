#validate g mailid

#lowercase
#starts with an alphabet
#numbers optional
#@gmail.com
#before at 6 to 64 charcters

from re import fullmatch

email=input("enter the email")

pattern="[a-z]+[a-z0-9]{5,63}(@gmail.com)"

matcher=fullmatch(pattern,email)
print("invalid" if matcher==None else "valid")
