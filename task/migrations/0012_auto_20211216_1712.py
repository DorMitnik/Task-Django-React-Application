# Generated by Django 3.2.9 on 2021-12-16 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0011_task_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='date',
            new_name='deadline',
        ),
        migrations.AddField(
            model_name='sub_task',
            name='deadline',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
