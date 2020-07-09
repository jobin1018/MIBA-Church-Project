# Generated by Django 3.0.7 on 2020-07-08 17:28

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('mibaapp', '0013_auto_20200708_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songs',
            name='song_image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default='songs_default.jpg', force_format=None, keep_meta=True, quality=100, size=[1000, 550], upload_to='songs_images'),
        ),
    ]
