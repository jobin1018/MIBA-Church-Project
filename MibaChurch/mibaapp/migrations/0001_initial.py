# Generated by Django 3.0.7 on 2020-06-30 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sermons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('link', models.CharField(blank=True, max_length=200, null=True)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Sermons',
            },
        ),
    ]
