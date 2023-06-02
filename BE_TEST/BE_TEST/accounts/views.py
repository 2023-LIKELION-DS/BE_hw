from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import UserCreateForm, SignUpForm

def signup_view(request):
    if request.method == 'GET': # GET 요청 시 HTML 응답
        form = SignUpForm
        context = {'form':form}
        return render(request, 'accounts/signup.html', context)
    else:
        # POST 요청 시 데이터 확인 후 회원 생성
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            #회원가입 처리
            instance = form.save()
            return redirect('index')
        else:
            #리다이렉트
            return redirect('accounts:signup')
        
def login_view(request):
    if request.method == 'GET':
        #로그인 HTML 응답
        return render(request, 'accounts/login.html', {'form':AuthenticationForm()})
    else:
        # 데이터 유효성 검사
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # 비즈니스 로직 처리 (회원가입 처리) - 로그인 처리
            login(request, form.user_cache)
        
            return redirect('index')
        else:
            # 비즈니스 로직 처리 (회원가입 처리) - 로그인 실패
            # 응답
            return render(request, 'accounts/login.html', {'form' : form})
        password = request.POST.get('password')
        
def logout_view(request):

    if request.user.is_authenticated:
        logout(request)
    return redirect('index')