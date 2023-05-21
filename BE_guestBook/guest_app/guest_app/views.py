from django.shortcuts import render
from . import GuestBook
from django.views.generic import ListView

def GuestBook(request):
    return render(request, "guestbook_list.html")