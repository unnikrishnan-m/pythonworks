f=open("C:\\Users\\sarat\\OneDrive\\Desktop\\pythonworks\\frame_work.txt","a")

frame_works=["wordpress","springboot","oodo","fastapi"]

for fw in frame_works:
    f.write(fw+"\n")
f.close()
