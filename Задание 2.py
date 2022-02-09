class Book:
    def __init__(self, name, author, data_published, genre, *reviews):
        self.name = name
        self.author = author
        self.date_published = data_published
        self.genre = genre
        self.reviews = reviews  # assigning tuple of Book_review objects

    def __repr__(self):
        return f'{self.name}, {self.author}, {self.date_published}, {self.genre}'

    def __str__(self):  # this is what gets printed if print is called
        list_of_reviews = 'Reviews: '  # str variable to concat all the reviews
        for i in self.reviews:
            if i.name == self.name:  # check if the review is for the selected book
                list_of_reviews += str(i) + '; '  # concat all reviews for the selected book under one variable

        return f'{self.name}, {self.author}, {self.date_published}, {self.genre}. \n{list_of_reviews}' #  print it

    def __eq__(self, other):  # to compare instances of a class Book
        if isinstance(other, Book):
            return (
                    self.name == other.name and
                    self.author == other.author and
                    self.date_published == self.date_published and
                    self.genre == other.genre)
        return NotImplemented  # Do not know what it means -> just copied from internet


class Book_review:
    def __init__(self, name, review):
        self.name = name
        self.review = review

    def __str__(self):  # it has to return str as we will pass the reviews later on
        return f'{self.review}'


# Testing clause
review1 = Book_review('Harry potter', "The book is good")  # Review 1
review2 = Book_review('Harry potter', "The book is good for me also")  # Review 2
review3 = Book_review('Python for Probability', "The book is complicated")  # Review 3

book1 = Book('Harry potter', 'J.K.Rowling', '1999', 'adventure', review1, review2)  # Passing only relevant reviews
book2 = Book('Python for Probability', 'Jose Unpingco', '2019', 'puzzle', review1, review2, review3)
# Passing all reviews on line 45

print(book1)
print()
print(book2)
