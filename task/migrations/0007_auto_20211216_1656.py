# Generated by Django 3.2.9 on 2021-12-16 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0006_auto_20211216_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sub_task',
            name='sub_task_name',
            field=models.CharField(default='aa', max_length=250),
        ),
        migrations.AlterField(
            model_name='task',
            name='task',
            field=models.CharField(default='aaa', max_length=250),
        ),
    ]
