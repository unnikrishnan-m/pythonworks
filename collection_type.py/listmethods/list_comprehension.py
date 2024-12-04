arr=[2,3,4,5,6,7]

square=[num**2 for num in arr]

print(square)


add_five=[num+5 for num in arr]

print(add_five)

odd_number=[num for num in arr if num%2!=0]
print(odd_number)

even_numbers=[num for num in arr if num%2==0]
print(even_numbers)