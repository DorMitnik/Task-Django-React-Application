# Generated by Django 3.2.9 on 2021-12-16 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0009_remove_sub_task_sub_task_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='sub_task',
            name='sub_task_name',
            field=models.CharField(default=None, max_length=250, null=True),
        ),
    ]