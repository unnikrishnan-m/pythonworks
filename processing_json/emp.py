from json import load

f=open("C:\\Users\\sarat\\OneDrive\\Desktop\\pythonworks\\processing_json\\emp.json")

data=load(f)

for emp in data:

    print(emp)