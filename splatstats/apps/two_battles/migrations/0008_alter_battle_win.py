# Generated by Django 3.2 on 2021-04-23 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("two_battles", "0007_alter_battle_player_rank"),
    ]

    operations = [
        migrations.AlterField(
            model_name="battle",
            name="win",
            field=models.BooleanField(null=True),
        ),
    ]