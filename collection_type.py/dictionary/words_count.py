words=["hello","hai","hello","this","is","this","is","hello"]

word_frequency={w:words.count(w) for w in words}
print(word_frequency)

recursive_words=[k for k,v in word_frequency.items() if v>1]
print(recursive_words)
#non palindromrsive

non_recursive_words=[k for k,v in word_frequency.items() if v==1]
print(non_recursive_words)
#most_recursive
most_recursive=max(recursive_words)

print(most_recursive)