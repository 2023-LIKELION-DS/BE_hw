from django.shortcuts import render, redirect, get_object_or_404
from .models import Index
from django.utils import timezone

# Create your views here.
def index(request):
    todo = Index.objects.all()
    return render(request, "index.html", {"todo":todo})

def create(request):
    if request.method == 'POST':
        index = Index()
        index.title = request.POST.get("title") #html에서 입력받은 title
        index.content = request.POST.get("content")
        index.save()
        return redirect('crudApp:index') #urls.py의 index로 url을 이동해줘
    return render(request, "create.html")

def detail(request, id):
    todo = get_object_or_404(Index, pk=id)
    return render(request, "detail.html", {"todo":todo})

def update(request, id):
    update_todo = get_object_or_404(Index, pk=id)
    if request.method == 'POST':
        update_todo.title = request.POST.get("title") #html에서 입력받은 title
        update_todo.content = request.POST.get("content")
        update_todo.date = timezone.now()
        update_todo.save()
        return redirect('crudApp:detail', id = update_todo.pk) #urls.py의 index로 url을 이동해줘
    return render(request, "update.html", {"update_todo":update_todo})

def delete(request, id):
    delete_todo = get_object_or_404(Index, pk=id)
    delete_todo.delete()
    return redirect('crudApp:index')