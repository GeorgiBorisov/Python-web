# Generated by Django 3.1.3 on 2020-12-06 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('python_web_exam', '0005_auto_20201206_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]