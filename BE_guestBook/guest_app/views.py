from django.shortcuts import render
from .models import GuestBook

# Create your views here.
def index(request):
    books = GuestBook.objects.all()
    return render(request, "index.html", {'books' : books})