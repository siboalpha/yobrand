# Generated by Django 4.0.3 on 2022-03-30 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0005_remove_task_due_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='status',
        ),
        migrations.AddField(
            model_name='task',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]
