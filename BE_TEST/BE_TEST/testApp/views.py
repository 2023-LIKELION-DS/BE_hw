from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Basic
from .forms import PostBaseForm, PostCreateForm
# Create your views here.
def index(request):
    list=Basic.objects.all()
    return render (request, "index.html", {"lists":list})


def create(request):
    if(request.method=="POST"):
        list=Basic()
        list.title=request.POST.get("title")
        list.content=request.POST.get('content')
        list.save()
        return redirect("index")
    return render(request, "create.html")

@login_required
def create_form_view(request):
    if request.method == 'GET':
        form = PostCreateForm()
        context = {'form': form}
        return render(request, 'create2.html', context)
    else:
        form = PostCreateForm(request.POST, request.FILES)
        
        if form.is_valid():
            Basic.objects.create(
                title=form.cleaned_data['title'],
                content=form.cleaned_data['content'],

            )
        else:
            return redirect('index')
        return redirect('index')

@login_required
def create_form_view2(request):
    if request.method == 'GET':
        form = PostBaseForm()
        context = {'form': form}
        return render(request, 'create2.html', context)
    else:
        form = PostBaseForm(request.POST, request.FILES)
        
        if form.is_valid():
            basic = Basic()
            basic.title = form.cleaned_data['title']
            basic.content = form.cleaned_data['content']
            basic.save()
            return redirect('index')
        else:
            return redirect('index')


def detail(request, id):
    list=get_object_or_404(Basic, pk=id)
    return render(request, "detail.html", {"list":list})

