class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def read(self):
        print("You are reading", self.title)

    def details(self):
        print("Title:", self.title)
        print("Author:", self.author)

b1 = Book("Sherlock Holmes", "Arthur Conan Doyle")

b1.details()
b1.read()
