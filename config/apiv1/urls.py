from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('user', views.UserViewSet)
router.register('posts', views.PostViewSet)
router.register('profile', views.ProfileViewSet)
router.register('comment', views.CommentViewSet)
router.register('tag', views.TagViewSet)

app_name = 'apiv1'
urlpatterns = [
    path('', include(router.urls)),
]
