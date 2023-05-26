from django.contrib import admin
from django.urls import path, include
from guest_app import views
from guest_app.views import index
# from django.urls import views, include, guestapp_list_view
# from guest_app import viewspath
# import  include path 

# 실제 출력 링크  
urlpatterns = [
    path('admin/', admin.site.urls),
    
    # path('', views.GuestList.as_view()),            # * 실습 1  
    
    # * 실습 2 사진 
    path('', index, name="index"),
    path('guestapp/', include('guest_app.urls')),  # main에서 guest url 클릭시 연결해줌 
    
    
]
    # path('', views.GuestList, name="index"),