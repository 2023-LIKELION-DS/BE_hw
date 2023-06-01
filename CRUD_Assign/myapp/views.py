from django.shortcuts import render, redirect, get_object_or_404
from .models import *

#MAIN

def index(request):
    my_show=Show.objects.all().order_by("-date")
    return render(request, "index.html", {"my_show":my_show})

#CREATE

def create(request):
    if request.method=="POST":
        shows=Show()
        shows.title=request.POST.get("title")
        shows.content=request.POST.get("content")
        shows.date=request.POST.get("date")
        shows.date=request.POST.get("comment")
        shows.save()
        return redirect("index")  #index로 이동해야함 
    return render(request, "create.html")  #create와 연결해주어야 함 index안됨 

#(detail)

def detail(request,id):
    detail_show=get_object_or_404(Show, pk=id)
    if request.method=="POST":
        detail_show.title=request.POST.get("title")
        detail_show.content=request.POST.get("content")
        detail_show.content=request.POST.get("date")
        detail_show.comment=request.POST.get("comment")
        return redirect("detail",detail_show.pk)
    return render(request, "detail.html",{'detail_show':detail_show})

#UPDATE

def update(request, id):
    update_show=get_object_or_404(Show, pk=id)
    if request.method=="POST":
        update_show.title=request.POST.get('title')
        update_show.content=request.POST.get('content')
        update_show.date=request.POST.get('date')
  
        update_show.save()
        return redirect("detail", update_show.pk)
    return render(request,"update.html", {"update_show":update_show})

def delete(request, id):
    delete_show=get_object_or_404(Show, pk=id)
    delete_show.delete()
    return redirect("index")

def create_comment(request, id):
    comment_show=get_object_or_404(Show, pk=id)
    if(request.method=="POST"):
        comment_show.comment=request.POST.get("comment")
        comment_show.save()
        return redirect("index")
    return render(request,"create_comment.html", {'comment_show':comment_show})
