# Generated by Django 3.0.7 on 2020-07-01 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mibaapp', '0005_auto_20200701_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hub',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
