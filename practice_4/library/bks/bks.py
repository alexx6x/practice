from books.models import Book
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render


def get(request):
    books = Book.objects.all()
    return render(request, "books.html", {'books': books})


def gets(request, bookId):
    try:
        book = Book.objects.get(id=bookId)
    except ObjectDoesNotExist:
        return "Unexisting book"
    return render(request, "book.html", {'book': book})