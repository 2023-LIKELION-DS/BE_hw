from django.contrib import admin
from django.urls import path
from .models import Basic
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    #path('create/',views.create, name="create"),
    path('<int:id>/', views.detail, name="detial"),
    path('create/',views.create_form_view, name="create")

]
