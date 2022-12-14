# Generated by Django 4.1 on 2022-08-11 12:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('general_task', models.CharField(max_length=500)),
                ('project_management', models.CharField(blank=True, max_length=500)),
                ('quality_analyst', models.CharField(blank=True, max_length=500)),
                ('ui_or_ux', models.CharField(blank=True, max_length=500)),
                ('meeting', models.CharField(blank=True, max_length=500)),
                ('development', models.CharField(blank=True, max_length=500)),
                ('blockers', models.BooleanField(default=False)),
                ('comments', models.CharField(blank=True, max_length=500)),
                ('time_off', models.DateTimeField(auto_now_add=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]
