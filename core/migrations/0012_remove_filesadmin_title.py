# Generated by Django 4.0.4 on 2022-05-06 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_filesadmin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filesadmin',
            name='title',
        ),
    ]
