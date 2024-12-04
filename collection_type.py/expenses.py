expenses=[10000,11000,12000,13000]
# for exp in expenses:
# # print(exp)

# #find total expense

# total=0

# for exp in expenses:
#     total+=exp 
# #print(total)


# #find maximum expense and minimum expense without using max() min()

# maximum=0
# for exp in expenses:
 
#     if exp>maximum:
#         maximum=exp

# print(maximum)



#find minimum expense and minimum expense without using max() min()

# minimum=expenses[0]  #17000
# for exp in expenses:
 
#     if exp<minimum:  #12000<11000
#         minimum=exp

# print(minimum)


avg=0
for exp in expenses:
    avg+=exp
avg/=len(expenses)
print(avg)
