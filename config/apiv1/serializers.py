from rest_framework import serializers

from app.models import Post
from users.models import Profile


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'text', 'price', 'photo']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'username', 'introduction', 'address', 'userpro', 'post', 'icon']
        # extra_kwargs = {'userpro': { 'read_only': True }}