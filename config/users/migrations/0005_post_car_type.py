# Generated by Django 3.1.2 on 2020-10-21 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_post_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='car_type',
            field=models.CharField(choices=[('corolla', 'Corolla'), ('prius', 'Prius'), ('voxy', 'Voxy')], default=1, max_length=20),
            preserve_default=False,
        ),
    ]
