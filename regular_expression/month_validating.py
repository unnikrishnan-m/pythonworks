from re import fullmatch

# user_input=input("enter the date")

# pattern="([1-9]|0[0-9]|1[0,2])"

# matcher=fullmatch(pattern,user_input)

# if matcher==None:

#     print("invalid")

# else:

#     print("valid")    


#date 01,1,31

date=input("enter the digit")

pattern="([1-9]|0[0-9]|1[1-9]|2[0-9]|3[0-1])" or "(0?[1-9]|[12][0-9]|3[01])"
matcher=fullmatch(pattern,date)
print("invalid" if matcher==None else "valid")
