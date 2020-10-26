# Generated by Django 3.1.2 on 2020-10-24 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20201021_2342'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='point',
            field=models.IntegerField(choices=[(1, '★1'), (2, '★2'), (3, '★3'), (4, '★4'), (5, '★5')], default=1, verbose_name='評価点'),
            preserve_default=False,
        ),
    ]
