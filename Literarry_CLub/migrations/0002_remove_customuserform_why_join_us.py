# Generated by Django 3.1.6 on 2021-02-08 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Literarry_CLub', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuserform',
            name='why_join_us',
        ),
    ]
