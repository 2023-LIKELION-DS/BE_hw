from django.contrib import admin
from django.urls import path, include
from guest_app import views
from guest_app.views import *

urlpatterns = [
path('admin/', admin.site.urls),
path('', views.index, name='index'),
path('guestapp/', include('guest_app.urls')),
]