from json import load
f=open("C:\\Users\\sarat\\OneDrive\\Desktop\\pythonworks\\processing_json\\books.json")
data=load(f)

for book in data:
    print(book)

all_titles=[book.get("title") for book in data]    

#print(all_titles)

#books with pages <250

page_filter= [book.get("title") for book in data if book.get("pages")<250]

#print(page_filter)

#print all genres

all_genres=[book.get("genre")for book in data]

print(set(all_genres))

genre_count={genre:all_genres.count(genre)for genre in all_genres}

print(genre_count)

#costly book
# max_price=max(book.get("price")for book in data)
# costly_book=[book.get("title") for book in data if book.get("price")==max_price]
# print(costly_book)

costly_book=max(data,key=lambda d:d.get("price"))

#print(costly_book)

#author with more than one book

mutiple_book=[book.get("author")for book in data]

author_count={author:mutiple_book.count(author)for author in mutiple_book}

print([k for k,v in author_count.items() if v > 1])

