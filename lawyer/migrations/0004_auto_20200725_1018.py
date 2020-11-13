# Generated by Django 3.0.5 on 2020-07-25 10:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lawyer', '0003_auto_20200725_0819'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaltask',
            name='tag_name',
            field=models.SlugField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='tag_name',
            field=models.SlugField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
