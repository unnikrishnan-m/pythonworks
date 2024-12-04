text=["apple","iphone","orange","pottatto"]
vowel_words=[w for w in text if w[0] in['a','e','i','o','u']]
print(vowel_words)

vowel_words=[w for w in text if w[0] not in['a','e','i','o','u']]
print(vowel_words)