# Generated by Django 3.0.8 on 2020-07-23 14:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app0725', '0004_pictures_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pictures',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 23, 23, 7, 26, 376874), verbose_name='date published'),
        ),
    ]
