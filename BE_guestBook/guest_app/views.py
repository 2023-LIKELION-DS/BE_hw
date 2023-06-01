from django.shortcuts import render
from .models import GuestBook
from django.views.generic import ListView

class GuestList(ListView):
    model = GuestBook
    ordering = ['-datetime']


def index(request):
    return render(request, "guest_app/index.html")

# Create your views here.
