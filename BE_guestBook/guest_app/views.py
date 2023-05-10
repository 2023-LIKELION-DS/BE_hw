from django.shortcuts import render
from .models import GuestBook

def index(request):
    books = GuestBook.objects.all()
    return render(request, "index.html", {'books' : books})

# Create your views here.
