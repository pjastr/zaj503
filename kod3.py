class Book:

    def __init__(self, title, author, page):
        self.title = title
        self.author = author
        self.page = page

    def __repr__(self):
        return f'Ilość stron: {self.page}, "{self.title}".'

    def __lt__(self, other):
        return (self.page, self.title) < (other.page, other.title)


books = [Book('title1', 'author1', 248),
         Book('title2', 'author2', 135),
         Book('title3', 'author3', 150),
         Book('title4', 'author4', 542),
         Book('title5', 'author5', 248)]
print(books)
books.sort()
print(books)
