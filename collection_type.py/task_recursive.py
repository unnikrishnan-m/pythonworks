def most_frequent_word():
    text="hello world hello everyone welcome to the world"
    words=text.split()
    word_frequency={w:words.count(w) for w in words}

    print(max(word_frequency))

most_frequent_word()    