# Generated by Django 2.2 on 2019-05-16 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circles', '0009_auto_20190516_1651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='circle',
            name='leads',
        ),
        migrations.RemoveField(
            model_name='circle',
            name='members',
        ),
    ]
