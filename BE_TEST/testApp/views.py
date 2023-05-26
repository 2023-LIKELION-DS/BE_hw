from django.shortcuts import render, redirect
from .models import *
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
  obj = Basic.objects.all()
  context = {
    'obj': obj,
  }
  return render(request, 'testApp/index.html', context=context)

def create(request):
  if request.method == 'POST':
    basic = Basic()
    basic.title = request.POST.get('title')
    basic.content = request.POST.get('content')
    basic.save()
    return redirect('index')
  return render(request, 'testApp/create.html')

def detail(request, pk):
  obj = get_object_or_404(Basic, pk=pk)
  context = {
    'obj': obj,
  }
  return render(request,'testApp/detail.html', context=context)
