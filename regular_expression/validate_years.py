from re import fullmatch

year=input("enter the year")

pattern="(18[0-9][0-9]|19[0-9][0-9]|20[01][0-9]|202[0-4])"

matcher=fullmatch(pattern,year)
print("invalid" if matcher==None else "valid")
