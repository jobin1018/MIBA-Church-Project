# Generated by Django 3.0.7 on 2020-07-01 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mibaapp', '0009_auto_20200701_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
