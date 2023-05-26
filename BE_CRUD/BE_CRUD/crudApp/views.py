from django.shortcuts import render, redirect, get_object_or_404
from .models import *

# Create your views here.

#* create 부분 
def create(request):
    if request.method == "POST":        #* POST 요청 시 
        index = Index()
        index.title = request.POST.get("title")
        index.content = request.POST.get("content")
        index.save()                                    #* index 객체 저장 후 index url으로 돌아감 
        return redirect("index")
    return render(request, "crudApp/create.html")               #* get 요청 시 

#* 기본 
def index(request):
    todo = Index.objects.all()
    return render(request, "crudApp/index.html", {"todo":todo})


#* read 부분 
def detail(request, id):
    todo = get_object_or_404(Index, pk=id)
    return render(request, "detail.html", {"todo":todo})


#* views 부분
def update(request, id):
    update_todo = get_object_or_404(Index, pk=id)
    if request.method == "POST":
        update_todo.title=request.POST.get("content")
        update_todo.content=request.POST.get("content")
        update_todo.date=request.POST.get("date")
        update_todo.save()
        return redirect("detail", update_todo.pk)
    return render(request, "update.html", {"update_todo": update_todo})

#* delete 삭제 부분 
def delete(request, id):
    delete_todo=get_object_or_404(Index, pk=id)
    delete_todo.delete()
    return redirect("index")