# Generated by Django 4.2.5 on 2023-10-30 05:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='done',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='plan',
            name='sana',
            field=models.DateField(default=datetime.date(2023, 10, 30)),
        ),
        migrations.AlterField(
            model_name='author',
            name='age',
            field=models.PositiveSmallIntegerField(default=20),
        ),
        migrations.AlterField(
            model_name='author',
            name='course',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
