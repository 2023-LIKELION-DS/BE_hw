from django.shortcuts import render
from .models import GuestBook
from django.views.generic.list import ListView

# Create your views here.

def index(request):
    books = GuestBook.objects.all()
    return render(request, "index.html", {'books' : books})

class class_view(ListView):
    model = GuestBook
    ordering = ['-datetime']