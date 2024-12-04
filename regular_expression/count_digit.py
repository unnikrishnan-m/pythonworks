from re import finditer

numbers="i have 3 cars,2 bikes and 1 cycle"

# #pattern="[ab]"

# pattern="[a-z]" #either a or b
# match=finditer(pattern,numbers)

# for num in match:

#     #wprint(num.start(),"==>",num.group())






# numbers="i have 3 cars,2 bikes and 1 cycle"

# #pattern="[ab]"

# pattern="[0-9]" #either a or b
# match=finditer(pattern,numbers)

# for num in match:

#     #print(num.start(),"==>",num.group()) 




#     numbers="i have 3 cars,2 bikes and 1 cycle"

# #pattern="[a-zA-A0-Z0-9]"

# pattern="[0-9]" #either a or b
# match=finditer(pattern,numbers)

# for num in match:

#     print(num.start(),"==>",num.group()) 
# numbers="i have 3 cars,2 bikes and 1 cycle"

# pattern="[^ab]"  #exluded " #either a or b
# match=finditer(pattern,numbers)

# for num in match:

#     print(num.start(),"==>",num.group()) 

# pattern="[^ak0-9A-Z, ]"

# match=finditer(pattern,numbers)

# for obj in match:

#     print(obj.start(),"=>",obj.group())



pattern="[^a-zA-Z0-9]"

match=finditer(pattern,numbers)

for obj in match:

    print(obj.start(),"=>",obj.group())


