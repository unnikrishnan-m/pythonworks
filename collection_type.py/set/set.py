users=["rahul","rohit","kohli","rishab","sanju","pandya","bumrah"]

rahul_followers=["rahul","rohit","pandya","bumrah"]

#follow suggessions["sanju","pandya","bumrah"]
sanju_followers=["sanju","rohit","kohli"]

users_set=set(users)

rahul_followers_set=set(rahul_followers)


suggession_set=users_set.difference(rahul_followers_set)

print(suggession_set)


#mutual friends

sanju_followers_set=set(sanju_followers)

mutual_friends=sanju_followers_set.intersection(rahul_followers_set)

print(mutual_friends)


