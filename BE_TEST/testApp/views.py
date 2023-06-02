from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# from .forms import PostBaseForm
from .models import *

# Create your views here.
def index(request):
    list = Basic.objects.all()        
    return render(request, "index.html", {"list": list})

@login_required
def create(request):
    if request.method =="POST":
        basic = Basic()
        basic.title = request.POST.get("title")
        basic.content = request.POST.get("content")
        basic.save()
        return redirect("testApp:index")
    return render(request, "create.html")

# def create_form(request):
#     if request.method =="POST":
#         basic = Basic()
#         basic.title = request.POST.get("title")
#         basic.content = request.POST.get("content")
#         basic.save()
#         return redirect("testApp:index")
#     return render(request, "create.html")

def detail(request, id):
    list = get_object_or_404(Basic, pk=id)
    return render(request, "detail.html", {"list":list})