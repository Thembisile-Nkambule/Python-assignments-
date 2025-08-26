class Book:
    # Constructor: runs when you create a Book
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # A simple method to describe the book
    def describe(self):
        print(f"'{self.title}' by {self.author}, {self.pages} pages")

# Inherits from Book
class Ebook(Book):  
    def __init__(self, title, author, pages, filesize):
        super().__init__(title, author, pages)
        self.filesize = filesize

# Polymorphism (method overriding)
    def describe(self):  
        print(f"'{self.title}' by {self.author}, {self.pages} pages, File size: {self.filesize}MB")

# Create objects (books) 
book1 = Book("Nearly All the Men in Lagos are Mad", "Damilare Kuku", 500)
ebook1 = Ebook("Desciple Walking with God", "rorisang thandekiso", 300, 5)

# Use the method
book1.describe()
ebook1.describe()

print()
#Activity 2
class Car:
    def move(self):
        print("Driving!")

class Plane:
    def move(self):
        print("Flying!")

class Boat:
    def move(self):
        print("Sailing!")

class Bicycle:
    def move(self):
        print("Pedaling!")

# Create objects
car = Car()
plane = Plane()
boat = Boat()
bicycle = Bicycle()

# Use the same method name, but each behaves differently
car.move()
plane.move()
boat.move()
bicycle.move()
