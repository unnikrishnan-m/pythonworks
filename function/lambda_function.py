#lambda function

add=lambda n1,n2:n1+n2
print(add(30,2))

sub=lambda n1,n2:n1-n2

print(sub(20,2))

cube=lambda n:n**3

print(cube(2))


max_two=lambda str1,str2:str1 if len(str1)>len(str2)else str2
print(max_two("hai","moring"))

min_two=lambda str1,str2:str1 if len(str1)<len(str2)else str2

print(min_two("hai","moring"))

smart_sub=lambda num1,num2:num1-num2 if num1>num2 else num2-num1

print(smart_sub(20,100))

words=["hello","hai","morning","test","apple"]

def get_length(word):
    return len(word)

print(max(words,key=get_length))


text="this is a simple programming question a to find word with maximum number of characters"

#split
words=text.split()

def get_length(w):
    return len(w)

srt_word=sorted(words,key=get_length,reverse=True)

print(srt_word)

print(max(words,key=get_length))

max_len=lambda word:len(words)
print(max_len)


#most recursive word

def get_count(w):
    
    return words.count(w)

most_recursive_word=max(words,key=get_count)
print("is  ",most_recursive_word)

#most recursive character

text="ABAABBC"
def get_count(w):
    return text.count(w)

most_recursive_character=max(text,key=get_count)
print(most_recursive_character)

# non recursive character
