# Generated by Django 3.0.8 on 2020-07-23 14:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app0725', '0006_remove_pictures_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='pictures',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='pictures',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]