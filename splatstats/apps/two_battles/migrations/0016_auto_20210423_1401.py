# Generated by Django 3.2 on 2021-04-23 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("two_battles", "0015_alter_battle_game_paint_point"),
    ]

    operations = [
        migrations.AlterField(
            model_name="battle",
            name="kills",
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="battle",
            name="level",
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="battle",
            name="specials",
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]