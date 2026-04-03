from django.shortcuts import render
from app4.models import Book
from django.http import HttpResponse
# Create your views here.

def test_debug(request):
    books =Book.objects.all()
    return HttpResponse(f"Total users: {books.count()}")