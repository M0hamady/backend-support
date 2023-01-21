# Generated by Django 3.2.16 on 2023-01-20 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '0002_auto_20230120_1419'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('location', models.CharField(max_length=150, null=True)),
                ('number', models.CharField(max_length=150, null=True)),
                ('name', models.CharField(max_length=150, null=True)),
                ('is_success', models.BooleanField(default=False)),
                ('is_accepted', models.BooleanField(default=False)),
                ('last_ip', models.CharField(max_length=150, null=True)),
                ('meet_at', models.DateField(null=True)),
                ('meet_time', models.TimeField(null=True)),
                ('orders', models.ManyToManyField(to='project.Project')),
            ],
        ),
    ]