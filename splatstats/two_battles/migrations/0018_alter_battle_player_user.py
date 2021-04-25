# Generated by Django 3.2 on 2021-04-23 18:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("two_battles", "0017_auto_20210423_1401"),
    ]

    operations = [
        migrations.AlterField(
            model_name="battle",
            name="player_user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
