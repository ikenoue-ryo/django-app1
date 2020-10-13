from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from app.models import Post
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
