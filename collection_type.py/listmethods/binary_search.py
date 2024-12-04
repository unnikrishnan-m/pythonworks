arr=[10,15,25,20,30]

arr.sort()
search_element=int(input("enter the search element"))
is_present=False
low=0

upp=len(arr)-1

while(low<=upp):
    mid=(low+upp)//2
    if search_element==arr[mid]:
        is_present=True
        break
    elif search_element<arr[mid]:
        upp=mid-1
    elif search_element>arr[mid]:
        low=mid+1

print(is_present)            