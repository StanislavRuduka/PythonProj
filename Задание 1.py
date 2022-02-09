class Book:
    def __init__(self, name, author, data_published, genre):
        self.name = name
        self.author = author
        self.date_published = data_published
        self.genre = genre

    def __repr__(self):
        return f'{self.name}, {self.author}, {self.date_published}, {self.genre}'

    def __str__(self):
        return f'{self.name}, {self.author}, {self.date_published}, {self.genre}'

    def __eq__(self, other):
        if isinstance(other, Book):
            return (
                        self.name == other.name and
                        self.author == other.author and
                        self.date_published == self.date_published and
                        self.genre == other.genre)
        return NotImplemented


book1 = Book('Harry potter', 'J.K.Rowling', '1999', 'adventure')
book2 = Book('Python for Probability', 'Jose Unpingco', '2019', 'puzzle')
book3 = Book('Harry potter', 'J.K.Rowling', '1999', 'adventure')

print(book1 == book2)
print(book1 == book3)
