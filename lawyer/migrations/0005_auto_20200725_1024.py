# Generated by Django 3.0.5 on 2020-07-25 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lawyer', '0004_auto_20200725_1018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicaltask',
            name='tag_name',
        ),
        migrations.RemoveField(
            model_name='task',
            name='tag_name',
        ),
    ]