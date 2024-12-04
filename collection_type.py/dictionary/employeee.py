#create a dictionary with keys eid,name,salary,department,experience


employee={"eid":1001,"name":"sushant","salary":27000,"dept":"HR","experience":5}

print(employee)

#add employee contact number


employee["contact"]=8157925611



if employee["experience"]>5:
    employee["salary"]+=10000
else:
    employee["salary"]+=5000



print(employee)


#add role as SDE if exp > 5 else add role as JDE



if employee["experience"]>5:

    employee["role"]="SDE"

else :
    employee["role"]="JDE"


print(employee)