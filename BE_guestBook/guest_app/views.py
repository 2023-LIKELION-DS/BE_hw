from django.shortcuts import render
from .models import GuestBook
from django.views.generic import ListView

def guest_list(request):
    books=GuestBook.objects.all().order_by('-datetime')
    return render(request, "guestapp/guestbook_list.html", {'books':books})

#def GuestList(request):
#    books=GuestBool.objects.all()
#    return render(request, "index.html", {'books':books})

#class GuestList(ListView):
#    model=GuestBook
#    ordering=['-datetime']

def index(request):
    return render(request, "index.html")

