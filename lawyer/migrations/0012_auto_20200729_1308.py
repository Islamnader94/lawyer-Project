# Generated by Django 3.0.5 on 2020-07-29 13:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('lawyer', '0011_auto_20200729_0824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpermission',
            name='account',
        ),
        migrations.RemoveField(
            model_name='userpermission',
            name='value',
        ),
        migrations.AddField(
            model_name='userpermission',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='userpermission',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_lawyer_userpermission', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userpermission',
            name='name',
            field=models.CharField(default='test', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userpermission',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='userpermission',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_lawyer_userpermission', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='HistoricalUserPermission',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False, null=True)),
                ('updated', models.DateTimeField(blank=True, editable=False, null=True)),
                ('name', models.CharField(max_length=100)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('created_by', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('feature', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='lawyer.Feature')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('permission', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='auth.Permission')),
                ('updated_by', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical user permission',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
