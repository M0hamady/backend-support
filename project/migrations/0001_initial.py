# Generated by Django 3.2.16 on 2023-02-14 17:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('useres', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('is_finished', models.BooleanField(default=False)),
                ('finished_at', models.DateTimeField(null=True)),
                ('address', models.CharField(max_length=300, null=True)),
                ('cost', models.FloatField(null=True)),
                ('uuid', models.CharField(default=uuid.UUID('90144bc2-e353-4690-8800-23b35d444f5d'), max_length=100, null=True)),
                ('civil_eng', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='civil_eng', to=settings.AUTH_USER_MODEL)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='creator', to=settings.AUTH_USER_MODEL)),
                ('designer_eng', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='designer', to=settings.AUTH_USER_MODEL)),
                ('manger', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='manager', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='owner', to=settings.AUTH_USER_MODEL)),
                ('worker', models.ManyToManyField(to='useres.User')),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, null=True)),
                ('cost', models.FloatField(null=True)),
                ('show_to_owner', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('start_at', models.DateField(null=True)),
                ('finished_at', models.DateTimeField(null=True)),
                ('is_finished', models.BooleanField(default=False)),
                ('uuid', models.CharField(default=uuid.UUID('4114e74b-4602-4cbe-8f11-a2e0a62dceaf'), max_length=100, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project')),
            ],
        ),
        migrations.CreateModel(
            name='Moshtarayet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, null=True)),
                ('cost', models.FloatField(null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.CharField(default=uuid.UUID('b9d7d833-a388-490b-a40c-bf018f958435'), max_length=100, null=True)),
                ('step', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.step')),
            ],
        ),
        migrations.CreateModel(
            name='Images_step',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(default=uuid.UUID('7bef5933-bf6e-4730-b36f-feaa261a6778'), max_length=120, null=True)),
                ('img', models.ImageField(null=True, upload_to='steps/images')),
                ('step', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.step')),
            ],
        ),
    ]
