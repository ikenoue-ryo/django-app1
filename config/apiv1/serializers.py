from rest_framework import serializers

from users.models import Post, Comment, Profile


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'profile', 'title', 'text', 'price', 'photo']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'username', 'introduction', 'address', 'userpro', 'icon']
        # extra_kwargs = {'userpro': { 'read_only': True }}

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('__all__')