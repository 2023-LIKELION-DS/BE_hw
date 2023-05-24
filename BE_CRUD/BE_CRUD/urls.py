from django.contrib import admin
from django.urls import path, include
from crudApp import views
from crudApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crudApp.urls')), #앱 urls랑 연결해주는 역할
]
