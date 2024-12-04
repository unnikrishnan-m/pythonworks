# Two letters for the state code (alphabet)
# An optional space or dash 
# Two digits for the city code 
# An optional space or dash 
# Four digits for the year of issue 
# An optional space or dash 
# Seven digits 

from re import fullmatch

user_license_number=input("enter the license number => ")

pattern="[A-Z]{2}[0-9]{2}[0-9]{4}[0-9]{7}"

matcher=fullmatch(pattern,user_license_number)

if matcher==None:

    print("invalid")

else:

    print("valid")