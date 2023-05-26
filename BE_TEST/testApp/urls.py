from django.urls import path
from testApp import views
urlpatterns = [
    path('create/', views.create, name="create"),
    path('detail/<int:id>', views.detail, name="detail"),
]


# pk를 같이 넘겨 글을 식별할 수 있음.