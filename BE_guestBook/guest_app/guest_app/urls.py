from django.urls import path
from guest_app import views

app_name = 'guest_app'


urlpatterns=[
        path('', views.GuestList.as_view, name = 'guestbook-list'),
]
