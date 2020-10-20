from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings
from django.utils import timezone


class UserManager(BaseUserManager):

    def create_user(self, email, username, password=None, **extra_fields):

        if not email:
            raise ValueError('Email address is must')

        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(email, username, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(max_length=50, unique=True)
    username = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


class Profile(models.Model):
    # nickname = models.CharField(max_length=20, null=True, blank=True)
    # username = models.CharField(max_length=50, null=True, blank=True)
    introduction = models.TextField()
    address = models.CharField(max_length=50, null=True, blank=True)
    userpro = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='userpro',
        on_delete=models.CASCADE,
    )
    created_on = models.DateTimeField(auto_now_add=True)
    icon = models.ImageField(upload_to="image/", null=True, blank=True)

    # def __str__(self):
    #     return self.username


class Post(models.Model):
    """投稿モデル"""

    class Meta:
        db_table = 'post'
        
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='投稿者', on_delete=models.CASCADE)
    # profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(verbose_name='タイトル', max_length=120, null=True, blank=True )
    text = models.TextField(verbose_name='本文', null=True, blank=True)
    price = models.IntegerField(verbose_name='価格', null=True, blank=True)
    photo = models.ImageField(upload_to='photo/', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)



class Comment(models.Model):
    """コメントモデル"""

    username = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='投稿先', on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, verbose_name='投稿者', on_delete=models.CASCADE, related_name='author')
    comment = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.comment