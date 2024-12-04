text="ABBACB"

char_count={}


for ch in text:
    if ch in char_count:
        char_count[ch]+=1

    else:
        char_count[ch]=1
print(char_count)    

# FIRST RECURSIVE CHARACTER

text="ABBACB"

rec={}
for ch in text:
    if ch in rec:
        print(ch)
        break
    else:
        rec[ch]=1