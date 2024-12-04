#merge two strings

#output PAQBRCST

#sample inputn1

text1="PQRS"

text2="ABCD"

#sample inputn1

#output:PAQBRCST

result=""

for i in range(0,len(text1)):
    result+=text1[i]+text2[i]
print(result)    


text1="PQRST"
text2="ABC"

smallest_text=text1 if len(text1)<len(text2) else text2

largest_text=text1 if len(text1)>len(text2) else text2

result=""

for i in range(0,len(smallest_text)):

    result+=text1[i]+text2[i]

bal_text=largest_text[len(smallest_text):]

result+=bal_text

print(result)
