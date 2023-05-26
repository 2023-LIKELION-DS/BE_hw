from django.urls import path, include
from .views import *

urlpatterns = [
  path('', GuestList.as_view(), name='guestbook_list'),
]    