# Generated by Django 5.0.1 on 2024-10-10 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='adduser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('email_id', models.EmailField(max_length=254)),
                ('active', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='excel')),
            ],
        ),
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_id', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('year_founded', models.IntegerField()),
                ('industry', models.CharField(max_length=50)),
                ('size_range', models.IntegerField()),
                ('locality', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('linkedin_url', models.CharField(max_length=50)),
                ('current_empl_estimate', models.IntegerField()),
                ('total_employee_estimate', models.IntegerField()),
            ],
        ),
    ]
