# Generated by Django 4.2.7 on 2023-11-05 11:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tickets', '0002_rename_userprofile_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='creator',
            field=models.ForeignKey(default='admin', on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to=settings.AUTH_USER_MODEL),
        ),
    ]
