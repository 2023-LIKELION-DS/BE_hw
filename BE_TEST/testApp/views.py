from django.shortcuts import render,redirect,get_object_or_404
from .models import Basic
# Create your views here.

def index(request):
    con =Basic.objects.all()
    return render(request, "index.html",{'con': con})

def create(request):
    if request.method == "POST":
        basic = Basic()
        basic.title = request.POST.get("title")
        basic.content = request.POST.get("content")
        basic.save()
        return redirect("index")
    return render(request,"testApp/create.html")


def detail(request, id):
    con = get_object_or_404(Basic,pk=id)
    return render(request,"testApp/detail.html",{"con":con})


# get_object_or_404, 객체가 없으면 404를 반환함. redirect는 페이지를 넘기는 기능을 가짐