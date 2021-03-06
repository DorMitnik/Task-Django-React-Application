# Generated by Django 3.2.9 on 2021-12-17 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0013_auto_20211217_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sub_task',
            name='deadline',
            field=models.FloatField(blank=True, help_text='Min', null=True, unique_for_date=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.FloatField(blank=True, help_text='Min', null=True, unique_for_date=True),
        ),
    ]
