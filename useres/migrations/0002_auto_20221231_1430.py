# Generated by Django 3.2.16 on 2022-12-31 14:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('useres', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='info',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_visitor',
        ),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.AddField(
            model_name='user',
            name='date_joined',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=654, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=654, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_accountant',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=654, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='12345', max_length=654),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=654, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='uuid',
            field=models.CharField(default=uuid.uuid1, max_length=350),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_designer',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_eng',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_manager',
            field=models.BooleanField(default=False),
        ),
    ]
