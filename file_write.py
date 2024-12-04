f=open("C:\\Users\\sarat\\OneDrive\\Desktop\\pythonworks\\file_write.txt","w")

languages=["python","java","c#","javascript"]

for l in languages:
    f.write(l+"\n")
f.close()