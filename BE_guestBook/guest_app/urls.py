from django.urls import path
from .views import guest_list
from . import views


app_name = 'guest_app'

urlpatterns = [
    path('',  views.guest_list, name="guest_list"),
]
