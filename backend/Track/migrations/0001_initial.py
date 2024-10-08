# Generated by Django 5.1 on 2024-09-01 21:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Album', '0002_initial'),
        ('Artist', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('duration', models.FloatField()),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Album.album')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Artist.artist')),
            ],
        ),
    ]
