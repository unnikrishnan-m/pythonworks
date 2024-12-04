from re import finditer

text="fatcatrunsevereyfasttocatchtherat"

matcher=finditer("at",text)

for obj in matcher:

    print(obj.start(),obj.group())


