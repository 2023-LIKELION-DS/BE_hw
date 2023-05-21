from django.urls import path,include
from .views import *
from guest_app import views

app_name = 'guest_app'


urlpatterns=[
        path('', GuestList.as_view, name = 'guestbook-list'),
]
