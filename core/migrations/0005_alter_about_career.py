# Generated by Django 4.0.4 on 2022-05-03 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_home_greetings_2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='career',
            field=models.CharField(max_length=50),
        ),
    ]
