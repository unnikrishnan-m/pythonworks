from re import fullmatch

user_input=input=input("enter variable name")

#start with an alphabet(lowrcase,uppercase)

pattern="[a-zA-Z][a-zA-Z0-9_]"

matcher=fullmatch(pattern,user_input)

for obj in matcher:

    print(obj.start(),obj.group())