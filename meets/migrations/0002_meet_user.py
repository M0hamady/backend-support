# Generated by Django 3.2.16 on 2023-02-14 19:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('meets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meet',
            name='user',
            field=models.OneToOneField(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='auth_user_meet', to='auth.user', verbose_name='User'),
            preserve_default=False,
        ),
    ]