#pan card number validation

#3 alphabets

#4th place alphabet[PCAFHT]

#1alphabet

#4digit

#1alphabet
from re import fullmatch

pancard_number=input("enter pan-card number:")

pattern="[A-Z]{3}[PCAFHT][A-Z](1)[0-9]{4}[A-Z]{1}"

matcher=fullmatch(pattern,pancard_number)

if matcher==None:

    print("invalid")

else:

    print("valid")    


