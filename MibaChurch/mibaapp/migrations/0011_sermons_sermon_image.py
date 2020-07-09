# Generated by Django 3.0.7 on 2020-07-07 09:11

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('mibaapp', '0010_auto_20200701_2226'),
    ]

    operations = [
        migrations.AddField(
            model_name='sermons',
            name='sermon_image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default='sermon_default.jpg', force_format=None, keep_meta=True, quality=100, size=[1000, 550], upload_to='sermon_images'),
        ),
    ]
