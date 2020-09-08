from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.indexfunc, name='index'),
    path('create_profile/', views.profilefunc, name='create_profile'),
    path('post/', views.post, name='post'),

]