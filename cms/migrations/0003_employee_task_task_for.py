# Generated by Django 4.0.3 on 2022-03-29 16:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cms', '0002_rename_duetade_task_due_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40, null=True)),
                ('last_name', models.CharField(max_length=40, null=True)),
                ('email', models.EmailField(max_length=30)),
                ('phone', models.CharField(max_length=12)),
                ('birthday', models.DateTimeField()),
                ('gender', models.CharField(choices=[('WEB DESIGNER', 'WEB DESIGNER'), ('CONTENT CONTENT_MANAGER', 'CONTENT MANAGER'), ('SOCIAL SOCIAL_MANAGER', 'SOCIAL_MANAGER')], default='WEB DESIGNER', max_length=40)),
                ('usermane', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='task_for',
            field=models.ManyToManyField(to='cms.employee'),
        ),
    ]
