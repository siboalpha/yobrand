# Generated by Django 4.0.4 on 2022-04-21 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0035_alter_project_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('COMPLETE', 'COMPLETE'), ('PENDING', 'PENDING'), ('UNCOMPLETE', 'UNCOMPLETE')], default='UNCOMPLETE', max_length=40),
        ),
    ]
