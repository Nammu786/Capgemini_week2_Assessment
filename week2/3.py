
''' 3. You are building a Library Management System. Create a `Book` class with properties like `title`, `author`, and `isbn`.
         Write a method to display book details.'''
class Library:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
    def details(self):
        print(f"Book name: {self.title}\nAuthor: {self.author}\nisbn: {self.isbn}")
l=Library("python OOPS","Guido",123)
l.details()