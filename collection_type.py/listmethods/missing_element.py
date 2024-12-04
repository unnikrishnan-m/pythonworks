arr=[1,3,4,5]

arr.sort()


for i in range(0,len(arr)-1):

    j=i+1

    result=arr[i]-arr[j]

    if result!=1:
        print(arr[i]+1,"is the missing element")
        break
    
        
              

               