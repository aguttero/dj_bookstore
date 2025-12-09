# esto no me funciono, sospecho que por los directorios de python
from models import Book

def add_slug():
    books = books = Book.objects.all()
    for book in books:
        book.save()
        print (book.slug)

add_slug()