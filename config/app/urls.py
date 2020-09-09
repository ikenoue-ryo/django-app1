from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.indexfunc, name='index'),
    path('create_profile/', views.profilefunc, name='create_profile'),
    path('post/', views.post, name='post'),
    path('new/', views.new, name='new'),
    path('car_list/', views.listfunc, name='car_list'),

    path('car_detail/<int:pk>/', views.detailfunc, name='car_detail'),

]