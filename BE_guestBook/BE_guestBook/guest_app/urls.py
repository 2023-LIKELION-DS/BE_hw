from django.urls import path
from guest_app import views

app_name = 'guest_app'

urlpatterns = [
    path('', views.GuestList.as_view(), name='guestbook-list'),  #index에서 연결할 수 있도록 app_name, GuestList의 name space 추가
]
