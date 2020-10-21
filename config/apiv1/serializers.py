from rest_framework import serializers

from users.models import Post, Comment, Profile


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'text', 'price', 'car_type']


class ProfileSerializer(serializers.ModelSerializer):
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
    class Meta:
        model = Comment
        fields = ('__all__')