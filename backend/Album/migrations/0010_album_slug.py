# Generated by Django 5.1 on 2024-09-07 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Album', '0009_album_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='slug',
            field=models.SlugField(default=1, max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
