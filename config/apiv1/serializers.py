from rest_framework import serializers

from users.models import User, Post, Comment, Profile, Tag, Message


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class TagSerializer(serializers.ModelSerializer):
    # post = PostSerializer()

    class Meta:
        model = Tag
        fields = ('__all__')


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
        # return Profile(**validated_data)

    def update(self, instance, validated_data): 
        instance.introduction = validated_data.get('introduction', instance.introduction)
        instance.address = validated_data.get('address', instance.address)
        instance.userpro.username = validated_data.get('username', instance.userpro.username)
        instance.icon = validated_data.get('icon', instance.icon)
        instance.save()
        return instance


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    profile = ProfileSerializer()

    tag = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'profile', 'photo', 'text', 'pr1', 'pr2', 'pr3', 'pr4', 'tag', 'price', 'place', 'car_type']

    def create(self, validated_data):
        author_data = validated_data.pop('author', None)
        if author_data:
            user = User.objects.get_or_create(**author_data)[0]
            validated_data['author'] = user
        tags = validated_data.pop('tag')
        profile = validated_data.pop('profile')
        post = Post.objects.create(**validated_data)
        user = User.objects.create(**validated_data)
        for tag in tags:
            post.tag.add(Tag.objects.create(**tag))
        post.profile = Profile.objects.create(**profile)
        post.profile.userpro = User.objects.create(**user)
        post.save()
        return post

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


class CommentSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'username', 'point', 'profile', 'comment']

    def update(self, instance, validated_data): 
        instance.username = validated_data.get('username', instance.username)
        instance.point = validated_data.get('point', instance.point)
        instance.profile.userpro.id = validated_data.get('id', instance.profile.userpro.id)
        instance.profile.userpro.username = validated_data.get('username', instance.profile.userpro.id)
        instance.profile.icon = validated_data.get('icon', instance.profile.icon)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.save()
        return instance




class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer()
    receiver = UserSerializer()
    profile = ProfileSerializer()

    class Meta:
        model = Message
        fields = ['id', 'sender', 'receiver', 'message', 'profile']
