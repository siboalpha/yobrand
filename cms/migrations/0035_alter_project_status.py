# Generated by Django 4.0.4 on 2022-04-21 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0034_alter_employeerequest_from_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('COMPLETE', 'COMPLETE'), ('PENDING', 'PENDING'), ('UNCOMPLETE', 'UNCOMPLETE')], default='WEBDESIGN', max_length=40),
        ),
    ]