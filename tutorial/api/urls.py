from django.urls import path
from . import views


urlpatterns = [

    
    path('users/',views.get_Users, name='get_User'),
    path('addusers/',views.add_User, name='add_User'),
    path('users/<int:pk>',views.userDetail, name='userDetail'),
    
]