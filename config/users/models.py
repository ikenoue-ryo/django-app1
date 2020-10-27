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


class Tag(models.Model):
    name = models.CharField('タグ名', max_length=20)

    def __str__(self):
        return self.name


class Post(models.Model):
    """投稿モデル"""

    CAR_TYPE = (
        ('corolla', 'corolla'),  # (DB値, 読みやすい値)
        ('prius', 'prius'),
        ('voxy', 'voxy'),
    )
    
    class Meta:
        db_table = 'post'
        
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='投稿者', on_delete=models.CASCADE)
    photo = models.ImageField(verbose_name='サムネイル画像', upload_to='photo/', null=False, blank=False)
    # title = models.CharField(verbose_name='タイトル', max_length=120, null=True, blank=True )
    text = models.TextField(verbose_name='本文', null=True, blank=True)
    pr1 = models.CharField(verbose_name='おすすめ1', max_length=20, null=True, blank=True )
    pr2 = models.CharField(verbose_name='おすすめ2', max_length=20, null=True, blank=True )
    pr3 = models.CharField(verbose_name='おすすめ3', max_length=20, null=True, blank=True )
    pr4 = models.CharField(verbose_name='おすすめ4', max_length=20, null=True, blank=True )
    tag = models.ManyToManyField(Tag, verbose_name='タグ', null=True, blank=True)
    car_type = models.CharField(max_length=20, choices=CAR_TYPE)
    price = models.IntegerField(verbose_name='価格', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.author.username


class Profile(models.Model):
    
    userpro = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='userpro',
        on_delete=models.CASCADE,
    )
    icon = models.ImageField(upload_to="image/", null=True, blank=True)
    introduction = models.TextField()
    address = models.CharField(max_length=50, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.userpro.username


SCORE_CHOICES = (
    (1, '★1'),
    (2, '★2'),
    (3, '★3'),
    (4, '★4'),
    (5, '★5'),
)

class Comment(models.Model):
    """コメントモデル"""

    username = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='投稿先', on_delete=models.CASCADE, null=True)
    point = models.IntegerField('評価点', choices=SCORE_CHOICES, default=3)
    profile = models.ForeignKey(to=Profile, verbose_name='投稿者', on_delete=models.CASCADE, null=True)
    comment = models.TextField()

    def __str__(self):
        return self.comment


class Message(models.Model):
    """メッセージモデル"""

    message = models.CharField(max_length=300)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='receiver', on_delete=models.CASCADE)
    profile = models.ForeignKey(to=Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.message
