# Generated by Django 3.2.16 on 2022-12-22 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_step_start_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step',
            name='finished_at',
            field=models.DateTimeField(null=True),
        ),
    ]
