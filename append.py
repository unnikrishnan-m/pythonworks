user_input=input("enter a text : ")

f=open("C:\\Users\\sarat\\OneDrive\\Desktop\\pythonworks\\read_write.txt","a")
f.write(user_input + "\n")  

f.close()