# from django.urls import path
# from .import views
# from crudApp.views import create

from crudApp import views
from django.urls import path

app_name = 'crudApp'

urlpatterns =[
    path("", views.index, name="index"),
    path("create/", views.create, name='create'),
    path("detail/<int:id>", views.detail, name="detail"),
    path("update/<int:id>", views.update, name="update"),
    path("delete/<int:id>", views.delete, name="delete"),
]