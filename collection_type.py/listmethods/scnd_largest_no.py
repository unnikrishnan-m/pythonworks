arr=[1,2,6,7,5]

arr.sort()

dup=arr.copy()

for i in range(0,len(arr)-1):
    i=0
    j=i+1

    temp=arr[j]-arr[i]

    if arr[j] in dup:
        ind=dup.index(arr[j])
        dup.pop(ind)

print(dup[len(dup)-2],"is the scnd lasrgest no")        
                



   
    


