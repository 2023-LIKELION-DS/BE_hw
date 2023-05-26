# from django.contrib import admin
from django.urls import path
from guest_app import views
# from guest_app.views import index
# from guest_app.views import viewspath, guestapp_list_view, GuestList, index

app_name='guest_app'

urlpatterns = [
    # path('', GuestList),
    # path('admin/', admin.site.urls),
    # path('', views.GuestList.as_view()),
    # path('', index, name="index"),
    # path('guestapp/', include('guest_app.urls')),
    # path('', views.gestbook_list_view ),                # ~주소/guestapp/
    
    
    path('', views.GuestList.as_view(), name='guestbook-list'),
    
]