# Generated by Django 2.0.1 on 2018-01-22 13:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_ifoundadog', '0002_auto_20180121_0145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dog_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
