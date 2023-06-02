from django.shortcuts import render, redirect, get_object_or_404
from .models import *
# Create your views here.

def index(request):
    lists = Basic.objects.all()
    return render (request, 'index.html', {'lists':lists})

def create(request):
    if request.method == 'POST':
        basic=Basic()
        basic.title = request.POST.get('title')
        basic.date = request.POST.get('date')
        basic.content = request.POST.get('content')
        basic.save()
        return redirect('index')
    return render (request, 'create.html')

def detail(request, id):
    list_detail = get_object_or_404(Basic, pk=id)
    return render(request, 'detail.html', {'list_detail':list_detail})