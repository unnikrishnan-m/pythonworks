arr=[1,2,2,2,1,4,5]

arr.sort()

dup_numbers=[]

for i in range(0,len(arr)-1):

    j=i+1

    result=arr[i]-arr[j]

    if result==0:

        if arr[i] not in dup_numbers:

            dup_numbers.append(arr[i])

print(dup_numbers)

    

