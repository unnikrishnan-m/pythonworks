from re import fullmatch

pattern="(91)?[0-9]{10}"

User_input=input("enter the number")

matcher=fullmatch(pattern,User_input)

if matcher==None:
    print("invalid")

else:

    print("valid")    


 #   * any number
 #   ? optional
 #   + mandetory
   