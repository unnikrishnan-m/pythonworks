from re import finditer

text="i have 3 cars,2 bike and 1 cycle "

#pattern="\w"#[a-zA-Z0-9] alphanumeric

#pattern="\d"#"[0-9]""

# pattern="\D"#"[^0-9]" exclude digit

#pattern="\W"  #special characters

pattern="\s"#space

# pattern="\S" #
# exclude space

matcher=finditer(pattern,text)

for obj in matcher:

    print(obj.start(),obj.group())
