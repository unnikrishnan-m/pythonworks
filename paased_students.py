f1=open("C:\\Users\\sarat\\OneDrive\\Desktop\\pythonworks\\all_students.txt","r")
f2=open("C:\\Users\\sarat\\OneDrive\\Desktop\\pythonworks\\failed.txt","r")
all_students_set=set()

failed_students_set=set()


for line in f1:
    line=line.rstrip("\n")
    all_students_set.add(line)
for line in f2:
    line=line.rstrip("\n")
    failed_students_set.add(line)
paased_students=all_students_set.difference(failed_students_set)

print(paased_students)
f1.close()
f2.close()
