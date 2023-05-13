from django.contrib import admin
from django.urls import path, include

from posts.views import index, url_view, url_parameter_view, function_view, class_view #꼭 import해야함 

urlpatterns = [  #리스트 형태이기 때문에 콤마를 무조건 작성하자 
    path('admin/', admin.site.urls),
    path('url/',url_view),
    path('url/<str:username>/', url_parameter_view ), #경로로 받는 것. int로 적으면 오류
    path('fbv/',function_view),
    path('cbv/', class_view.as_view(), name='cbv'),

    path('', index, name='index'),
    path('posts/', include('posts.urls', namespace='posts')),
]
