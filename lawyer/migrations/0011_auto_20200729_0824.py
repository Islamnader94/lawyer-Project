# Generated by Django 3.0.5 on 2020-07-29 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('authtoken', '0002_auto_20160226_1747'),
        ('lawyer', '0010_auto_20200728_0943'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.AlterModelOptions(
            name='case',
            options={'permissions': (('manage_case', 'Who can manage and view list of cases'),)},
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'permissions': (('manage_task', 'Who can manage and view list of tasks'),)},
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('lawyer.baseuser',),
        ),
    ]
