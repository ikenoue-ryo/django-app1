from django.urls import path, include
from rest_framework import routers

from . import views

app_name = 'app'

urlpatterns = [
    path('booking/', views.sendmail, name='booking'),
]
