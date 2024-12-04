start=int(input("enter start :"))
end=int(input("enter limit :"))

# for num in range(start,end+1,1):
#     print(num)
if start<end:
    for num in range(start,end+1,1):
        print(num)

else:

    for num in range(start,end-1,-1):
        print(num)        