# # #capitalize
# # #casefold
# # #isdigit
# # #isalnum




# # text="hellopython"

# # result=text.capitalize()
# # print(result)

# # print(text.casefold())

# # print(text.isdigit())
# # print(text.isalpha())

# # print(text.isalnum())

# # print(text.startswith("he"))
# # print(text.endswith("ox"))


# # for ch in text:
# #     print(ch)

# text="helloworld"
# for ch in text:
#     if ch=="a" or ch=="e"or ch=="i" or ch=="o" or ch=="u":
#        print(ch)       

text="pneumonoultramicroscopicsilicovolcanoconiosis"
vowel=(a,e,i,o,u)
v_count=0
c_count=0
for ch in text:
    if ch=="a" or ch=="e"or ch=="i" or ch=="o" or ch=="u": #if ch in vowel: 
        v_count=v_count+1
    else:
        c_count=c_count+1    
# print("vowel count",v_count)
# print("consonant count",c_count)

#split()
text="hello,world,python"

words="hello,world,python"

word=text.split(",")

# print(words)

# new_text=_"\n this is \na line\n"

#print(new_text)
#lstrip()
#rstrip()


#remove \n
new_text=text.strip("\t")

#replace()

text="hello world program"

#o=>a

new_text=text.replace("o","a",3)

# print(new_text)
#slice()

text="python programming" # index starts from 0

#string_object[start:end:step]
print(text[:6])
print(text[7:])
print(text[::2])
print(text[0:6])

string="hello"

reversed_text=string[::-1]

print(reversed_text)


#index()

text="helloworld"
#     0123456789

# index of first o

#text.replace()

#text.index("o")=>4

# print(text.index('o'))

# text="vipinkumar@gmail.com"

#find indexof @

#slice text from 0:index of slice

# index=text.index("@")
# print(text[:index])

text="hellopython"

#llehopython
#0123456789
index=text.index("o")
slice=text[index-1::-1]
print(slice)
remaining=text[index:]
result=slice+remaining

print(result)


