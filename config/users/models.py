
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings

def upload_path(instance, filename):
    ext = filename.split('.')[-1]
    return '/'.join(['image', str(instance.userpro.id)+str(instance.nickname)+str(".")+str(ext)])

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
    nickname = models.CharField(max_length=20)
    userpro = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='userpro',
        on_delete=models.CASCADE
    )
    created_on = models.DateTimeField(auto_now_add=True)
    friends = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='friends',
    )
    img = models.ImageField(blank=True, null=True, upload_to=upload_path)

    def __str__(self):
        return self.nickname