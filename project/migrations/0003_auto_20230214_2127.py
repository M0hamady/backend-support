# Generated by Django 3.2.16 on 2023-02-14 19:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20230214_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images_step',
            name='uuid',
            field=models.CharField(default=uuid.UUID('7b7d5f11-ff22-4bb0-818b-45ce0633ca61'), max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='moshtarayet',
            name='uuid',
            field=models.CharField(default=uuid.UUID('1de70e04-95e9-4ada-a379-09710f6a9cbd'), max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='uuid',
            field=models.CharField(default=uuid.UUID('7faeb88f-4199-433c-8d61-4dfb93724b3b'), max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='step',
            name='uuid',
            field=models.CharField(default=uuid.UUID('24b77310-88dd-41ca-bbad-286dc7701271'), max_length=100, null=True),
        ),
    ]
