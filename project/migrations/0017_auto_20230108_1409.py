# Generated by Django 3.2.16 on 2023-01-08 14:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0016_auto_20230108_1353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='worker',
        ),
        migrations.AddField(
            model_name='project',
            name='civil_eng',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='civil_eng', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='project',
            name='designer_eng',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='designer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='project',
            name='manger',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='manager', to=settings.AUTH_USER_MODEL),
        ),
    ]