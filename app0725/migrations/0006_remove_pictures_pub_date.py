# Generated by Django 3.0.8 on 2020-07-23 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app0725', '0005_auto_20200723_2307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pictures',
            name='pub_date',
        ),
    ]
