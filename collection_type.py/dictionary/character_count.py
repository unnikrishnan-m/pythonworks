text="ABABBCCDDE"

character_frequency={ch:text.count(ch) for ch in text}

print(character_frequency)

#non recursive element

for k,v in character_frequency.items():
    if v==1:
        print(k)

#or

non_recursive_element=[k for k,v in character_frequency.items()  if v==1]

print(non_recursive_element)

