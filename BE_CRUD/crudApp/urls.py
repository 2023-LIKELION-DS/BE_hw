from django.urls import path, include
from .views import *

urlpatterns = [
  path('', index, name='index'),
  path('create/', create, name='create'),
  path('detail/<int:pk>/', detail, name='detail'),
  path('update/<int:pk>/', update, name='update'),
  path('delete/<int:pk>/', delete, name='delete'),
]    