from django.shortcuts import render, redirect
from .models import *
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    todo = Index.objects.all()
    return render(request, "index.html", {"todo": todo})

def create(request):
    if request.method =="POST":
        index = Index()
        index.title = request.POST.get("title")
        index.content = request.POST.get("content")
        index.save()
        return redirect("index")
    return render(request, "create.html")


def detail(request, id):
    todo = get_object_or_404(Index, pk=id)
    return render (request, "detail.html", {"todo": todo})