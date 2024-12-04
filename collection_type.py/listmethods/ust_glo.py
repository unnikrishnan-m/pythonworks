arr=[100,200,300,400,500,600,700,800]

# odd=[]

# for i in range(0,len(arr)):
#     if i%2!=0:
#         odd.append(arr[i])
# print(odd)        
# odd.reverse()

# for i in range(1,len(arr),2):
#     element=odd
#     .pop()

left=1

right=len(arr)-1

if right%2==0:
    right-=1

while(left<right):
    arr[left],arr[right]=arr[right],arr[left]

    left+=2
    right-=2

print(arr)        
