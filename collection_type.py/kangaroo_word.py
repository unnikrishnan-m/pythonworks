# source="CHICKEN"
# target="NIKE"

# character_count={}

# for ch in source:
#     if ch in character_count:
#         character_count[ch]+=1
#     else:
#         character_count[ch]=1    


# #or 

# character_count={ch:source.count(ch) for ch in source}
# is_kangarro=True

# for ch in target:
#     if ch in character_count and character_count.get(ch)>0:

#         character_count[ch]-=1

#     else:

#         is_kangarro=False

#         break
# print(is_kangarro)        
       


user_input=input("enter bracket pairs")#()

brackets={"(":")","[":"]","{":"}"}#(

symbol_stack=[]
top=-1
is_valid=True
for b in user_input:#()
    if b in brackets:
      top=top+1
      symbol_stack.append(b)
    elif top==-1:
       is_valid=False

    
    elif b==brackets.get(symbol_stack[top]):
      top=top-1
      symbol_stack.pop()
    else:
        is_valid=False
if len(symbol_stack)==0 and is_valid==True:
   print("valid")
else:
   print("invalid")


         