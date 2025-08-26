class Book:
  def __init__(self, title, price):
    self.title = title 
    self._price = price
  
  def bookInfo(self):
    print(f"title of book:{self.title}\n price of book: {self._price}\n")

class EBook(Book):
  def bookInfo(self):
    print(f"title of ebook:{self.title} \n price of book: {self._price}")

book1 = Book("kafka", 2000)
book1.bookInfo()

Ebook1 = EBook("man of war", 5000)
Ebook1.bookInfo()