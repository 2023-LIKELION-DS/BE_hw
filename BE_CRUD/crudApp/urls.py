from django.urls import path
from . import views



urlpatterns = [
    path('', views.index,name="index"),
    path("create/",views.create ,name="create"),
    path("detail/<int:id>", views.detail, name="detail"),
    path("update/<int:id>",views.update, name="update"),  #views.(url함수)
    path("delete/<int:id>",views.delete, name="delete"),
]