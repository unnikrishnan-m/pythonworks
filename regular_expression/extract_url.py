from re import findall

f=open("C:\\Users\\sarat\\OneDrive\\Desktop\\pythonworks\\regular_expression\\url.txt")

content=f.read()



pattern="https?://[\w\S./]+"

urls=findall(pattern,content)

for url in urls:
    print(url)
