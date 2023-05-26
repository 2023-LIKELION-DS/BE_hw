from django.shortcuts import render
from .models import GuestBook
from django.views.generic import ListView

def index(request):
    books = GuestBook.objects.all()
    return render(request, "index.html", {'books' : books})



# 목록
class GuestList(ListView):
    model = GuestBook
    ordering = ['-datetime']




# 목록 
# def gestbook_list_view(request):            
#     return render(request, 'guest_app/gestbook_list.html/')


# 클래스는 다 지워서? 해보? 세요? 라고? 하는데? 강의에 이 내용이 나왔다고 