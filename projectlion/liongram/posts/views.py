from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404
from django.views.generic.list import ListView
from .models import Post
from django.contrib.auth.decorators import login_required

def index(request):
    post_list = Post.objects.all().order_by('-created_at')  # Post 전체 데이터 조회, 최신글-created의 역순, uqeryset apa에 나와있다!
    context = {
        'post_list': post_list,
    }
    return render(request, 'index.html', context)


def post_list_view(request):
    #post_list = Post.objects.all()  # all:Post 전체 데이터 조회, SQL문이 생김 
    post_list = Post.objects.filter(writer=request.user)  # 작성자가 로그인한 유저인 경우를 조회해달라-->관리자에서 로그인하면 됨. 작성자가 모두 admin  (<->non)
    # post_list = None
    context = {
        'post_list': post_list,  #딕셔너리 형태
    }
    return render(request, 'posts/post_list.html', context)



def post_detail_view(request, id):
    try:  #예외처리-->
        post = Post.objects.get(id=id) #하나를 불러오는 것 get써야, id값으로 조회할 수 있음 
    except Post.DoesNotExist:  #없을 때 나는 에러 
        return redirect('index')  #render보다는 redirect 없는데이터일때도 넘어감 
    context = {
        'post': post,
    }
    return render(request, 'posts/post_detail.html', context)


@login_required  #로그인을 했을 때만 처리하는 함수, user가 로그인되어있는지 확인.
def post_create_view(request):
    if request.method=='GET':
        return render(request, 'posts/post_form.html') #get 요청이 들어왔을 경우 폼을 보여줌-->
    else:
        image = request.FILES.get("image")  #이미지는 파일로 전송, 대문자
        content = request.POST.get('content')  #폼을 post로 날리기 때문에 post로 받아야  
        print(image)
        print(content)
        Post.objects.create(
        image=image,
        content=content,
        writer=request.user
        )
        return redirect('index')
    

#update의 경우 create와 detail이 합쳐졌다고 생각해도 !
def post_update_view(request, id): #데이터를 조회하는 과정 필요함.
    #post=Post.objects.get(id=id)  #objects복수형이어야 한다!-->

    post=get_object_or_404(Post, id=id)  #안전하게 코드를 짤 수 있음 -에러가 나면 404로 넘김 

    if request.method == 'GET':
        context = { 'post': post }
        return render(request, 'posts/post_form.html', context)
    elif request.method == 'POST':
        new_image = request.FILES.get('image')
        content = request.POST.get('content')
        print(new_image)
        print(content)  #이미지를 변경하지 않았는데도 새로운 이미지가 추가되는 문제점이 생김 
        if new_image:  #새로운 이미지가 있을때만 -->그런데 이미지가 바뀌지만 이미지가 늘ㄹ어남
            post.image.delete()  #지우기.
            post.image=new_image
        post.content=content
        post.save()  #실제로 저장됨 
        return redirect('posts:post-detail',post.id)

@login_required
def post_delete_view(request,id):
    post=get_object_or_404(Post, id=id) #writer=response.user
    if request.user != post.writer:
        raise Http404('잘못된 접근입니다.')   #에러유도
    if request.method=='GET':
        context={'post':post}
        return render(request, 'posts/post_comfirm_delete.html', context)
    else:
        post.delete()  #삭제 
        return redirect('index')
    


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


#url-->view함수를 처리해서 렌더링해서 출력
#딕셔너리 형태로 값을 넘겨주면 template에서 그 값을 사용할 수 있음
#템플릿 언어는 {{}}, 템플릿 태그가 따로 있다.