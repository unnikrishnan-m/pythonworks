#startingh with KL

#2digit

#alphabets munimum1 max2

# 4 digit

from re import fullmatch

pattern="(KL|kl)[0-9]{2}[A-Z]{1,2}[0-9]{4}"

user_input=input("enter the number")


matcher=fullmatch(pattern,user_input)


if matcher==None:

    print("invalid")

else:

    print("valid")    