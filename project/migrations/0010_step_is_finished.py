# Generated by Django 3.2.16 on 2022-12-24 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_alter_step_finished_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='step',
            name='is_finished',
            field=models.BooleanField(default=False),
        ),
    ]
