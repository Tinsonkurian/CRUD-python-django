
from django.urls import path, include
from . import views



urlpatterns = [

    path('', views.index, name='index'),
    path('adduser', views.adduser, name='adduser'),
    path('edituser/<int:id>/', views.edituser, name='edituser'),
    path('edituser/updateuser/<int:id>/', views.updateuser, name='updateuser'),
    path('deleteuser/<int:id>/', views.deleteuser, name='deleteuser'),

]