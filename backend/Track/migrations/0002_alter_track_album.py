# Generated by Django 5.1 on 2024-09-01 21:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Album', '0004_alter_album_releasedate'),
        ('Track', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to='Album.album'),
        ),
    ]
