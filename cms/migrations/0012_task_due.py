# Generated by Django 4.0.3 on 2022-03-31 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0011_remove_task_task_for_task_complete_task_employee_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='due',
            field=models.DateTimeField(null=True),
        ),
    ]
