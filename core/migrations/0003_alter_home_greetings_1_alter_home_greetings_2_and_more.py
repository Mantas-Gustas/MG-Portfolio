# Generated by Django 4.0.4 on 2022-05-02 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_home_greetings_1_alter_home_greetings_2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='greetings_1',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='home',
            name='greetings_2',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='home',
            name='picture',
            field=models.ImageField(null=True, upload_to='picture/'),
        ),
    ]
