from django.shortcuts import render, redirect
from .models import *
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
  index = Index.objects.all()
  return render(request, "crudApp/index.html", {"obj": index})

def create(request):
  if request.method == "POST":
    index = Index()
    index.title = request.POST.get('title')
    index.content = request.POST.get('content')
    index.save()
    return redirect('index')
  return render(request, "crudApp/create.html")

def detail(request, pk):
  obj = get_object_or_404(Index, pk=pk)
  return render(request, "crudApp/detail.html", {"obj": obj})

def update(request, pk):
  obj = get_object_or_404(Index, pk=pk)
  if request.method == "POST":
    obj.title = request.POST.get('title')
    obj.content = request.POST.get('content')
    obj.date = request.POST.get('date')
    obj.save()
    return redirect('detail', obj.pk)
  
  return render(request, "crudApp/update.html", {"obj" : obj})

def delete(request, pk):
  obj = get_object_or_404(Index, pk=pk)
  obj.delete()
  return redirect('index')