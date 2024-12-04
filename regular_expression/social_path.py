from re import finditer

f=open("C:\\Users\\sarat\\OneDrive\\Desktop\\pythonworks\\regular_expression\\social_post.txt")

for line in f:

    word= line.rstrip("\n")

    pattern="#\w"

    matcher=finditer(pattern,word)

    for obj in matcher:

        print(obj.group())