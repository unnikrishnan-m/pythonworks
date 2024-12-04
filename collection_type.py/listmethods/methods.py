colors=["red","green","blue"]
colors.append("yellow")  #insrt a new element to the list
print(colors)


popped_el=colors.pop()#to remove an element from a list
print(colors)

print(popped_el)



colors.pop(0)

print(colors)


colors.insert(0,"purple")

print(colors)

red_index=colors.index("blue")
print(red_index)

#copy

basic_colors=["red","yellow","blue","green"]

complimentary_colors=basic_colors.copy()

complimentary_colors.pop()

print("basic",basic_colors)
print("com",complimentary_colors)

#sort
list=[2,3,4,5,6]

list.sort()

list.sort(reverse=True)
print(list)