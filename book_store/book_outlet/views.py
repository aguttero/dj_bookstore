from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Book

# Create your views here.
def index(request):
    books = Book.objects.all()
    return render(request, "book_outlet/index.html", {
        "books": books
    })

def book_detail(request, book_db_id):
    # try:
    #     book = Book.objects.get(id=book_db_id)
    #     # book = Book.objects.get(pk=book_db_id) pk: primary key
    # except:
    #     raise Http404()
    book = get_object_or_404(Book, pk=book_db_id)
    return render (request, "book_outlet/book_detail.html", {
            "book": book
        })

## dummy data 
def detail(request):
    return render (request, "book_outlet/book_detail.html")

