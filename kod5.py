# Ćwiczenie 1. Stwórz klasę Book z polami author, title, price. Stwórz listę 10 książek i posortuj je po długości tytułu (od najkrótszego do najdłuższego).

class Book:

    def __init__(self, author, title, price):
        self.author = author
        self.title = title
        self.price = price

    def __repr__(self):
        return f'{self.title} ({self.price} zł)'

    def __lt__(self, other):
        return (len(self.title), self.price) < (len(other.title), other.price)


books = [Book('Machuga', 'To jest ksiąka 1', 48),
         Book('Ratuszniak', 'A teraz book nr 2', 35),
         Book('Autor 3', 'Ta książka jeszcze inny tytuł ma', 50),
         Book('Petrowski', 'Tytuł krótki 1', 42),
         Book('Flisak', 'Tytuł krótki 2', 27)]
books.sort()
print(books)