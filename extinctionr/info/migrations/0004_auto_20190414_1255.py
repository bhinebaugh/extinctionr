# Generated by Django 2.2 on 2019-04-14 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_auto_20190413_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='caption',
            field=models.TextField(blank=True, default=''),
        ),
    ]