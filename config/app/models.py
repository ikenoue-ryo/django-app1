import uuid

from django.db import models
from django.utils import timezone


class Post(models.Model):
    """投稿モデル"""

    class Meta:
        db_table = 'post'
        
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(verbose_name='タイトル', max_length=120, null=True, blank=True )
    text = models.TextField(verbose_name='本文', null=True, blank=True)
    price = models.IntegerField(verbose_name='価格', null=True, blank=True)
    photo = models.ImageField(upload_to='photo/', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

