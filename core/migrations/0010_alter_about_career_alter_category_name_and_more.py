# Generated by Django 4.0.4 on 2022-05-06 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_portfolio_delete_project_alter_about_career_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='career',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='skills',
            name='skill_name',
            field=models.CharField(max_length=50),
        ),
    ]
