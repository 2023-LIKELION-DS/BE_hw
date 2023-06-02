from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .forms import UserCreateForm, SignUpForm

from users.models import User

def signup_view(request):
    #GET 요청시 HTML 응답
    if request.method == 'GET':
        form = SignUpForm
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)
    else:
        # POST 요청 시 데이터 확인 후 회원 생성
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            #회원가입 처리
            # form.cleaned_data['username']
            # form.cleaned_data['email']
            # form.cleaned_data['password2']
            instance = form.save()
            return redirect('testApp:index')
        else:
            #리다이렉트 / 회원가입 조건 불총족 -> 기존 form으로 다시 렌더링
            return render(request, 'accounts/signup.html', {'form': form})
        
def login_view(request):
    # GET, POST 분리
    if request.method == 'GET':
        # 로그인 HTML 응답
        return render(request, 'accounts/login.html', {'form': AuthenticationForm()})
    else:
        # 데이터 유효성 검사
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # 비즈니스 로직 처리 - 로그인 처리
            login(request, form.user_cache)
            # 응답
            return redirect('testApp:index') ### testApp: 추가
        else:
            # 비즈니스 로직 처리 - 로그인 실패
            # 응답
            return render(request, 'accounts/login.html', {'form': form})
        
        # password = request.POST.get('password')
    # 데이터 유효성 검사
    # 비즈니스 로직 처리
    # 응답
    
    # username = request.POST.get('username')
    # if username == '' or username == None:
    #         pass
    # user = User.objects.get(username=username)
    # if user == None:
    #         pass
    # password = request.POST.get('password')

