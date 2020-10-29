from rest_framework import viewsets
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated

from users.models import User, Post, Comment, Profile, Tag, Message
from .serializers import UserSerializer, PostSerializer, ProfileSerializer, CommentSerializer, TagSerializer, MessageSerializer

from django.core.mail import send_mail

"""User"""
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


"""投稿"""
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]


"""プロフィール"""
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # authentication_classes = (authentication.TokenAuthentication)
    # permission_classes = (permissions.IsAuthenticated,)

    # putで登録処理
    def get_object(self):
        if self.request.method == 'PUT':
            id = self.kwargs.get('pk')
            obj, created = Profile.objects.get_or_create(pk=id, userpro_id=id)
            return obj
        else:
            return super(ProfileViewSet, self).get_object()


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    # putで登録処理
    def get_object(self):
        if self.request.method == 'PUT':
            id = self.kwargs.get('pk')
            obj, created = Comment.objects.get_or_create(pk=id, profile_id=id)
            return obj
        else:
            return super(CommentViewSet, self).get_object()



"""メッセージ"""
class MessageViewSet(viewsets.ModelViewSet):
    # メッセージ
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    # リクエストユーザーの閲覧可能画面
    def get_queryset(self):
        return self.queryset.filter(sender=self.request.user)
    
class InboxListView(generics.ListAPIView):
    # メッセージ受信箱
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    # permission_classes = (IsAuthenticated,)

    # def get_queryset(self):
    #     return self.queryset.filter(receiver=self.request.user)


"""予約メール送信"""
def sendmail(request):
    send_mail('Example Subject', 'Example message', 'ryo.ikenoue@gmail.com', ['ikenoue.ryo@gmail.com'], fail_silently=False)
    return send_mail