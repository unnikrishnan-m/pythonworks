arr=[
    1,2,
    [10,20],
    [1,2,5,[10,3]],
    100
    ]
    
list_objects=[item for item in arr if isinstance(item,list)]

print(max(list_objects,key=len))




#task2

student_data={
              "hari":[45,40,35],
              "vipin":[34,40,45],
              "vinay":[45,40,35],
              "binoy":[33,38,35],
              "anvin":[32,30,40]
              }
# index1 hari's avg mark

index=int(input("enter id"))
for i,element in enumerate(student_data):

    if i+1==index:

        marks=student_data.get(element)
        avg=sum(marks)//len(marks)
        print(avg)

student_avg_marks={k:sum(v)//len(v) for k,v in student_data.items()}
print(student_avg_marks)


