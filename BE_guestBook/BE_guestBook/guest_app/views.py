from django.shortcuts import render
from .models import *
from django.views.generic import ListView


# Create your views here.
def index(request):
  books = GuestBook.objects.all()
  return render(request, "index.html", {"books": books})

class GuestList(ListView):
  model = GuestBook
  ordering = ['-datetime']

def main(request):
  return render(request, "guest_app/main.html")
