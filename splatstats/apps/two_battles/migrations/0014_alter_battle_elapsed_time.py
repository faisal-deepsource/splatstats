# Generated by Django 3.2 on 2021-04-23 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("two_battles", "0013_alter_battle_deaths"),
    ]

    operations = [
        migrations.AlterField(
            model_name="battle",
            name="elapsed_time",
            field=models.PositiveIntegerField(null=True),
        ),
    ]
