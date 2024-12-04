# The first digit is not 0 or 1
# The next three digits are followed by an optional space or dash
# The next four digits are followed by an optional space or dash
# The final digit is the check digit

from re import fullmatch

user_aadhar=input("enter your aadhar number => ")

pattern="[2-9]{1} [0-9]{3}[0-9]{4}[0-9{4}]*"

matcher=fullmatch(pattern,user_aadhar)

if matcher==None:

    print("invalid aadhar")

else:

    print("valid aadhar")