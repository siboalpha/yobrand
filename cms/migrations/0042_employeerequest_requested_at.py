# Generated by Django 4.0.4 on 2022-04-27 11:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0041_remove_employeerequest_requested_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeerequest',
            name='requested_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 27, 11, 1, 35, 209908)),
        ),
    ]
