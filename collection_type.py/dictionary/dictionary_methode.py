employee={"id":222,"name":"rinku","department":"HR","age":25,"salary":32000}
print(employee.get("department"))#get(key)
#inavlid key return none

#pop(key)   remove


employee.pop("salary")

print(employee)


for k in employee.keys():
    print(k)



for v in employee.values():
    print(v) 


for k,v in employee.items():

    print(k,v)    