# Generated by Django 3.2.8 on 2021-12-19 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='finished_date',
            field=models.DateField(verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='service',
            name='started_date',
            field=models.DateField(verbose_name='date published'),
        ),
    ]
