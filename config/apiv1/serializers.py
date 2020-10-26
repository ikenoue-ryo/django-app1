from rest_framework import serializers

from users.models import User, Post, Comment, Profile, Tag


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('__all__')


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    tag = TagSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'photo', 'title', 'text', 'pr1', 'pr2', 'pr3', 'pr4', 'tag', 'price', 'car_type']

    def update(self, instance, validated_data): 
        instance.author.username = validated_data.get('author', instance.author.username)
        instance.title = validated_data.get('title', instance.title)
        instance.text = validated_data.get('text', instance.text)
        instance.pr1 = validated_data.get('pr1', instance.pr1)
        instance.pr2 = validated_data.get('pr2', instance.pr2)
        instance.pr3 = validated_data.get('pr3', instance.pr3)
        instance.pr4 = validated_data.get('pr4', instance.pr4)
        instance.tag = validated_data.get('tag', instance.tag)
        instance.price = validated_data.get('price', instance.price)
        instance.car_type = validated_data.get('car_type', instance.car_type)
        instance.save()
        return instance


class ProfileSerializer(serializers.ModelSerializer):
    userpro = UserSerializer()

    class Meta:
        model = Profile
        fields = ['id', 'introduction', 'address', 'userpro', 'icon']
        # extra_kwargs = {
        #     'userpro': {'validators': []},
        # }

    def create(self, validated_data):
        userpro_data = validated_data.pop('userpro', None)
        if userpro_data:
            user = User.objects.get_or_create(**userpro_data)[0]
            validated_data['userpro'] = user
        return Profile.objects.create(**validated_data)
        
        return Profile(**validated_data)

    def update(self, instance, validated_data): 
        instance.introduction = validated_data.get('introduction', instance.introduction)
        instance.address = validated_data.get('address', instance.address)
        instance.userpro.username = validated_data.get('username', instance.userpro.username)
        instance.icon = validated_data.get('icon', instance.icon)
        instance.save()
        return instance


class CommentSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = Comment
        fields = ['id', 'username', 'point', 'profile', 'comment']

    def update(self, instance, validated_data): 
        instance.username = validated_data.get('username', instance.username)
        instance.point = validated_data.get('point', instance.point)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.save()
        return instance