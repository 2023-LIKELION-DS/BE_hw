from django.urls import path, include
from guest_app import views
from guest_app.views import *

app_name = 'guest_app'

urlpatterns = [
path('', GuestList.as_view(), name='guestbook-list'),
]