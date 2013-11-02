from books.models import Authors
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render


def gets(request):
    authors = Authors.objects.all()
    return render(request, "authors.html", {'authors': authors})


def get(request, authorId):
    try:
        author = Authors.objects.get(id=authorId)
    except ObjectDoesNotExist:
        return "Unexisting author"
    return render(request, "author.html", {'author': author})