class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("your email was successfully changed to" + str(self.email))

    def __repr__(self):
        print("user: ", self.name, " email: ", self.email, " books: ", self.books.keys().count())

    def __eq__(self, other_user):
        return self.name  == other.name

    def read_book(self, book, rating = None):
        self.books[book] = rating

    def get_average_rating(self):
        self.total = 0
        for i in self.books.keys():
            total += self.books.get(i)
        return total / len(self.books)




class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("new ISBN assigned:", self.isbn)

    def add_rating(self, rating):
        if 0 <= rating <= 4:
            self.ratings.append(rating)
        else:
            print("invalid rating")

    def __eq__(self, other_book):
        return self.title == other_book.title and self.isbn == other_book.isbn

    def get_average_rating(self):
        self.total = 0
        for i in self.ratings:
            self.total += i
        return self.total / len(self.ratings)

    def __hash__(self):
        return hash((self.title, self.isbn))

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}".format(title = self.title, author = self.author)


class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title = self.title, level = self.level, subject = self.subject)


class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        return book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating = None):
        if email in self.users.keys():
            self.users.get(email)
            User.read_book(book, rating)
            Book.add_rating(book, rating)

        else:
            print("No user with email {email}!".format(email = email))

        if book in self.books:
            self.books[book] += 1
        else:
            self.books[book] = 1

    def add_user(self, name, email, user_books = None):
        User.name = name
        User.email = email
        if user_books is not None:
            for book in user_books:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        for key in self.books.keys():
            print(key)

    def print_users(self):
        for user in self.users:
            print(user)

    def most_read_book(self):
        self.keymax = ""
        self.vmax = 0
        for i in self.books.keys():
            if self.books[i] > self.vmax:
                self.vmax = self.books[i]
                self.keymax = i
        return self.keymax

    def highest_rated_book(self):
        self.bestbook = ""
        self.bestavg = 0
        for i in self.books.keys():
            if book.get_average_rating(self.books[i]) > self.bestavg:
                self.bestavg = self.books[i]
                self.bestbook = i

    def most_positive_user(self):
        self.posuser = ""
        self.posrating = 0
        for i in self.users.keys():
            if user.get_average_rating(self.users[i]) > self.posrating:
                self.posrating = self.books[i]
                self.posuser = i
