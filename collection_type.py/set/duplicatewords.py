text="this is a test to remove duplicate words this test is simple"
#split text with space
text2="this simple test remove duplicate words"

words=text.split(" ")

words1=text2.split(" ")

print(set(words1).issubset(words))
#print(set(words))