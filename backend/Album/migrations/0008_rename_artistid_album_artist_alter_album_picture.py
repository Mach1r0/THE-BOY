# Generated by Django 5.1 on 2024-09-03 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Album', '0007_album_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='ArtistId',
            new_name='Artist',
        ),
        migrations.AlterField(
            model_name='album',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='albums-img/'),
        ),
    ]
