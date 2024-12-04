arr=[2,3,4,5]

sum=8

#(5,3)

for i in range(0,len(arr)-1):

    for j in range (i+1,len(arr)):
        

        cur_sum=arr[i]+arr[j]

        if sum==cur_sum:

            print(arr[i],arr[j])

            break




#or
# 
# 
#         
arr=[2,3,4,5]

sum=8

left=0

right=len(arr)-1


while(left<right):
    cur_sum=arr[left]+arr[right]
    if cur_sum==sum:
        print(arr[left],arr[right])
        break
    elif cur_sum>sum:
        right=right-1
    elif cur_sum<sum:
        left=left+1    





