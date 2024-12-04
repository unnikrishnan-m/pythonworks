arr1=[10,13,8,11,20]

arr2=[2,20,8,7,13]

for i in range(0,len(arr1)):
    for j in range(0,len(arr2)):
        

      if  arr1[i]==arr2[j]:
         
        

            print(arr1[i])


# arr1=[1,3,4,5]
#missing positive integer
#find least positive missing integer

# arr3=[1,2,3,5]

arr1=[1,3,4,5]
first=1
for i in range(0,len(arr1)):
    
    if first==arr1[i]:
        
      first+=1
    else:
        break  
    
print(first)



arr1=[1,2,3,5]
first=1
for i in range(0,len(arr1)):
    
    if first==arr1[i]:
        
      first+=1
    else:
        break  
    
print(first)

