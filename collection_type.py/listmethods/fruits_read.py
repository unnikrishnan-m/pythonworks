f=open("C:\\Users\\sarat\\OneDrive\\Desktop\\pythonworks\\collection_type.py\\listmethods\\fruit_txt","r")
fruits=[]

for line in f:
    fruits.append(line.rstrip("\n"))
print(fruits)    

