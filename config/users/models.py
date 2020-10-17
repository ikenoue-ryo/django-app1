
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings
from app.models import Post


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
    #iconを必須に設定
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


class Profile(models.Model):
    # nickname = models.CharField(max_length=20, null=True, blank=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    introduction = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    post = models.ForeignKey(Post, verbose_name='投稿', null=True, blank=True, on_delete=models.CASCADE)
    userpro = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='userpro',
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    created_on = models.DateTimeField(auto_now_add=True)
    friends = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='friends',
    )
    icon = models.ImageField(upload_to="image/", null=True, blank=True)

    def __str__(self):
        return self.username