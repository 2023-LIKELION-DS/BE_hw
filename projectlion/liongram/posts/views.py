from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic.list import ListView
from .models import Post

# Create your views here.
def url_view(request):
    data={'code':'001'}
    print("url_view")
    return HttpResponse('url_view')   #html로 날아감.
    #return JsonResponse(data)  #딕셔너리 형태

def url_parameter_view(request,username):
    print('url_parameter_view()')
    print(f'username:{username}')
    print(f'username:{request.GET}') #딕셔너리 key value형태로 들어옴 
    return HttpResponse(username)

def function_view(request):
    print(f'request.method : {request.method}')  #get일때, post일때 구분 
    if request.method == 'GET':
        print(f'request.GET: {request.GET}')
    elif request.method == 'POST':
        print(f'request.POST : {request.POST}')
    return render(request,'view.html')

class class_view(ListView):  #class기반 
    model=Post
    template_name='cbv_view.html'