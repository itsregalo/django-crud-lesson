# Generated by Django 3.2.3 on 2021-11-08 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_post_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]