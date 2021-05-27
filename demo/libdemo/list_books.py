from bs4 import BeautifulSoup

f = open("books.xml", "rt")
bs = BeautifulSoup(f.read(), "xml")
books = bs.find_all("book")

for book in books:
    print(f"{book.find('title').text:30} {int(book.find('price').text):4}")

f.close()