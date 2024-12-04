def review(rating):
    assert rating>0,"too low"
    assert rating in range(0,11),"too high"
print("rated")

try:

    review(10)


except Exception as e:

    print(e)    