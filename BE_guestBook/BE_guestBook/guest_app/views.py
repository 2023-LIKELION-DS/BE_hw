from django.shortcuts import render
from .models import GuestBook
from django.views.generic import ListView
# from django.view.list import ListView
# Create your views here.
def index(request):
    books = GuestBook.objects.all()
    return render(request, "index.html", {'books' : books})

class GuestList(ListView):
    model = GuestBook
    # template_name = 'class_view.html'
    ordering = ['-datetime']
    
def guestapp_list(request):
    return render(request, 'guestbook_list.html')