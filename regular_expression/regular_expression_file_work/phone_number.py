from re import fullmatch 
f=open("C:\\Users\\sarat\\OneDrive\\Desktop\\pythonworks\\regular_expression\\regular_expression_file_work\\phone_number.txt")


for line in f:
    phone=line.rstrip("\n")

    pattern="(91)?[0-9]{10}"


    matcher=fullmatch(pattern,phone)

    if matcher!=None:

        print(phone)