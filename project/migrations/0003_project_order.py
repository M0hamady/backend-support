# Generated by Django 3.2.16 on 2022-12-20 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0011_rename_is_succeded_meeting_is_success'),
        ('project', '0002_step_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='meetings.meeting'),
        ),
    ]