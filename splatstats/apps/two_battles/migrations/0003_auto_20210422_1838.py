# Generated by Django 3.2 on 2021-04-22 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("two_battles", "0002_auto_20210422_1659"),
    ]

    operations = [
        migrations.AddField(
            model_name="battle",
            name="assists",
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="battle",
            name="deaths",
            field=models.PositiveSmallIntegerField(default=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="battle",
            name="elapsed_time",
            field=models.PositiveIntegerField(default=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="battle",
            name="game_paint_point",
            field=models.PositiveSmallIntegerField(default=904),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="battle",
            name="kills",
            field=models.PositiveSmallIntegerField(default=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="battle",
            name="league_point",
            field=models.DecimalField(
                blank=True, decimal_places=1, max_digits=5, null=True
            ),
        ),
        migrations.AddField(
            model_name="battle",
            name="level",
            field=models.PositiveSmallIntegerField(default=19),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="battle",
            name="my_team_count",
            field=models.DecimalField(decimal_places=1, default=77, max_digits=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="battle",
            name="other_team_count",
            field=models.DecimalField(decimal_places=1, default=78, max_digits=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="battle",
            name="player_rank_after",
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name="battle",
            name="specials",
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="battle",
            name="splatfest_point",
            field=models.DecimalField(
                blank=True, decimal_places=1, max_digits=5, null=True
            ),
        ),
        migrations.AddField(
            model_name="battle",
            name="splatfest_title",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="battle",
            name="splatfest_title_after",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="battle",
            name="x_power",
            field=models.DecimalField(
                blank=True, decimal_places=1, max_digits=5, null=True
            ),
        ),
        migrations.AlterField(
            model_name="battle",
            name="player_rank",
            field=models.CharField(blank=True, max_length=4),
        ),
        migrations.AlterField(
            model_name="battle",
            name="tag_id",
            field=models.CharField(
                blank=True, max_length=11, null=True, verbose_name="Team ID"
            ),
        ),
    ]
