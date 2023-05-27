from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .forms import UserCreateForm, SingUpForm

from users.models import User

def signup_view(request):

    if request.method == 'GET':
        form = SingUpForm
        context = {'form': form}
        return render(request, 'signup.html', context)
    else:
        form = SingUpForm(request.POST)

        if form.is_valid():

            instance = form.save() 
            return redirect('index')           
        else:

            return redirect('signup')
        
def login_view(reqeust):
    if reqeust.method == 'GET':
        return render(reqeust, 'login.html', {'form': AuthenticationForm()})
    else:

        form = AuthenticationForm(reqeust, data=reqeust.POST)
        if form.is_valid():

            login(reqeust, form.user_cache)

            return redirect('index')
        else:

            return render(reqeust, 'login.html', {'form': form})
def logout_view(request):

    if request.user.is_authenticated:
        logout(request)
    #응답
    return redirect('index')