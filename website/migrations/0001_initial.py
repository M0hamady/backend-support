# Generated by Django 3.2.16 on 2023-01-21 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Websiteindex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_welcome', models.CharField(max_length=150, null=True)),
                ('description_welcome', models.CharField(max_length=600, null=True)),
                ('pic_welcom', models.ImageField(upload_to='WelcomeIndex/%y')),
                ('pic_team', models.ImageField(upload_to='TeamIndex/%y')),
                ('title_team', models.CharField(max_length=150, null=True)),
                ('description_team', models.CharField(max_length=600, null=True)),
                ('team_first_title', models.CharField(max_length=150, null=True)),
                ('team_first_description', models.CharField(max_length=600, null=True)),
                ('team_seconed_title', models.CharField(max_length=150, null=True)),
                ('team_seconed_description', models.CharField(max_length=600, null=True)),
                ('company_title', models.CharField(max_length=160, null=True)),
                ('company_description', models.CharField(max_length=600, null=True)),
                ('pic_company_1', models.ImageField(upload_to='CompanyIndex/%y')),
                ('pic_company_2', models.ImageField(upload_to='CompanyIndex/%y')),
                ('pic_company_3', models.ImageField(upload_to='CompanyIndex/%y')),
                ('customer_title', models.CharField(max_length=160, null=True)),
                ('customer_description', models.CharField(max_length=600, null=True)),
                ('pic_customer_1', models.ImageField(upload_to='CustomerIndex/%y')),
                ('company_words_title', models.CharField(max_length=160, null=True)),
                ('company_words_description', models.CharField(max_length=600, null=True)),
                ('pic_saying_1', models.ImageField(upload_to='ImagIndex/%y')),
                ('pic_saying_1_title', models.CharField(max_length=160, null=True)),
                ('pic_saying_2', models.ImageField(upload_to='ImagIndex/%y')),
                ('pic_saying_2_title', models.CharField(max_length=160, null=True)),
                ('pic_saying_3', models.ImageField(upload_to='ImagIndex/%y')),
                ('pic_saying_3_title', models.CharField(max_length=160, null=True)),
                ('manager_title', models.CharField(max_length=300, null=True)),
                ('manager_description', models.CharField(max_length=600, null=True)),
            ],
        ),
    ]