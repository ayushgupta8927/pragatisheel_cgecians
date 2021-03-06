# Generated by Django 3.1.3 on 2021-04-11 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Literarry_CLub', '0007_auto_20210408_1258'),
    ]

    operations = [
        migrations.CreateModel(
            name='AriettaUserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('admission_year', models.CharField(max_length=30)),
                ('your_department', models.CharField(max_length=50)),
                ('contact_number', models.CharField(max_length=13)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='DebateUserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('admission_year', models.CharField(max_length=30)),
                ('your_department', models.CharField(max_length=50)),
                ('contact_number', models.CharField(max_length=13)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='LiterarryUserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('admission_year', models.CharField(max_length=30)),
                ('your_department', models.CharField(max_length=50)),
                ('contact_number', models.CharField(max_length=13)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PratibimbaUserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('admission_year', models.CharField(max_length=30)),
                ('your_department', models.CharField(max_length=50)),
                ('contact_number', models.CharField(max_length=13)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='RongmilantiUserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('admission_year', models.CharField(max_length=30)),
                ('your_department', models.CharField(max_length=50)),
                ('contact_number', models.CharField(max_length=13)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TechonicsUserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('admission_year', models.CharField(max_length=30)),
                ('your_department', models.CharField(max_length=50)),
                ('contact_number', models.CharField(max_length=13)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
    ]
