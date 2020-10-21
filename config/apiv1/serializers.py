from rest_framework import serializers

from users.models import User, Post, Comment, Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'text', 'price', 'car_type']


class ProfileSerializer(serializers.ModelSerializer):
    userpro = UserSerializer()

    class Meta:
        model = Profile
        fields = ['id', 'introduction', 'address', 'userpro', 'icon']
        # extra_kwargs = {'userpro': { 'read_only': True }}
        extra_kwargs = {
            'userpro': {'validators': []},
        }

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class CommentSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = Comment
        fields = ('__all__')