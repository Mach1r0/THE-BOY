# Generated by Django 5.1 on 2024-09-01 21:58

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Album', '0003_alter_album_releasedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='ReleaseDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
