from django.urls import path
from testApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('detail/<int:id>/', views.detail, name='detail'),
]