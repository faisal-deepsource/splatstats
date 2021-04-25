# Generated by Django 3.2 on 2021-04-23 16:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("two_battles", "0005_auto_20210422_2156"),
    ]

    operations = [
        migrations.AlterField(
            model_name="battle",
            name="my_team_count",
            field=models.DecimalField(decimal_places=1, max_digits=4),
        ),
        migrations.AlterField(
            model_name="battle",
            name="other_team_count",
            field=models.DecimalField(decimal_places=1, max_digits=4),
        ),
        migrations.AlterField(
            model_name="battle",
            name="player_result_player_weapon_special",
            field=models.CharField(max_length=2, verbose_name="Special"),
        ),
        migrations.AlterField(
            model_name="battle",
            name="player_result_player_weapon_sub",
            field=models.CharField(max_length=2, verbose_name="Sub Weapon"),
        ),
        migrations.RemoveField(
            model_name="battle",
            name="player_user",
        ),
        migrations.AddField(
            model_name="battle",
            name="player_user",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="auth.user"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="battle",
            name="player_weapon",
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name="battle",
            name="stage",
            field=models.CharField(max_length=2),
        ),
        migrations.DeleteModel(
            name="Player",
        ),
    ]