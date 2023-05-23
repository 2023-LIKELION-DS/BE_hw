from django.urls import path
from . import views  #view 가져와야함!!

urlpatterns = [
    path('',views.index, name="index"),
    path('create',views.create, name="create"),
    path('detail/<int:id>',views.detail, name="detail"),
    path('update/<int:id>',views.update, name="update"),
    path('delete/<int:id>',views.delete, name="delete"),
    path('create_comment/<int:id>',views.create_comment, name="create_comment"),
]
