# Generated by Django 4.0.4 on 2022-05-09 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_remove_filesadmin_title'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FilesAdmin',
        ),
        migrations.AlterField(
            model_name='home',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
