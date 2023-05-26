from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, JsonResponse
from django.views.generic.list import ListView
from .models import Post



# 6강 내용
def index(request):
    post_list = Post.objects.all().order_by('-created_at')
    context = {'post_list':post_list,}   
    
    return render(request, 'index.html', context)

def post_list_view(request):
    post_list = Post.objects.all()  # post 전체 데이터 조회
    # post_list = Post.objects.filter(writer=request.user)   # post.writer가 현재 로그인 한 것 조회
    # post_list = None
    context = {
        'post_list': post_list,
    }
    return render(request, 'posts/post_list.html/', context)

@login_required
def post_create_view(request):
    if request.method == "GET":
        return render(request, 'posts/post_form.html/')
    else:
        image = request.FILES.get('image')
        content = request.POST.get('content')
        print(image)
        print(content)
        Post.objects.create(
            image=image,
            content=content,
            # writer=request.user
        )
        return redirect('index')

def post_detail_view(request, id):
    post = Post.objects.get(id=id)
    context = {
        'post':post,
    }
    return render(request, 'posts/post_detail.html/', context)

@login_required
def post_update_view(request, id):
    
    # post = Post.objects.get(id=id)
    post = get_object_or_404(Post, id=id)
    
    
    if request.method == 'GET':
        context = { 'post':post }
        return render(request, 'posts/post_form.html/', context)
    elif request.method == 'POST':
        new_image = request.FILES.get('image')
        content = request.POST.get('content')
        print(new_image)
        print(content)
        
        if new_image:
            post.image.delete()
            post.image = new_image
            
        post.content = content
        post.save()
        return redirect('posts:post-detail', post.id )

@login_required
def post_delete_view(request, id):
    post = get_object_or_404(Post, id=id, writer=request.user)
    
    # 예외처리 방법 
    if request.user != post.writer:
        return Http404('잘못된 접근')
    
    if request.method == 'GET':
        context = { 'post': post }
        return render(request, 'posts/post_confirm_delete.html', context)  
    else:
        post.delete()
        return redirect('index')




# 함수를 실행하는  방법
def url_view(request):
    print('url_view()')
    data = {'code': '001', 'msg': 'OK'}
    return HttpResponse('<h1>url_view</h1>')
    # return JsonResponse(data)


# 받는 방법
def url_parameter_view(request, username):
    print('url_parameter_view()')
    print(f'username: {username}')
    print(f'request.GET: {request.GET}')
    return HttpResponse(username)

def function_view(request):
    print(f'request.method: {request.method}')
    if request.method == 'GET':
        print(f'request.GET: {request.GET}')
    elif request.method == 'POST':
        print(f'request.POST: {request.POST}')
    return render(request, 'view.html')


#  클래스 기반 뷰 
class class_view(ListView):
    model = Post
    ordering = ['-id']
    # template_name = 'cbv_view.html'
    
    
def funtion_list_view(request):
    object_list = Post.objects.all().order_by('-id')
    return render(request, 'cbv_view.html', {'object_list': object_list})