# Generated by Django 4.0.3 on 2022-04-11 20:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cms', '0027_activity_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='user',
        ),
        migrations.AddField(
            model_name='activity',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]