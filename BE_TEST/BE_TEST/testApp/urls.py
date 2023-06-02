# from django.urls import path
# from .import views
# from crudApp.views import create

from testApp import views
from django.urls import path

app_name = 'testApp'

urlpatterns =[
    path("", views.index, name="index"),
    path("create/", views.create, name='create'),
    path("detail/<int:id>", views.detail, name="detail"),

]