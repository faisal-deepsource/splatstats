# Generated by Django 3.2 on 2021-04-25 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('two_battles', '0025_alter_battle_teammate1_rank'),
    ]

    operations = [
        migrations.AddField(
            model_name='battle',
            name='teammate2_assists',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='battle',
            name='teammate2_clothes',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='battle',
            name='teammate2_clothes_main',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='battle',
            name='teammate2_clothes_sub0',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='battle',
            name='teammate2_clothes_sub1',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='battle',
            name='teammate2_clothes_sub2',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='battle',
            name='teammate2_deaths',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='battle',
            name='teammate2_game_paint_point',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='battle',
            name='teammate2_gender',
            field=models.CharField(choices=[('girl', 'Female'), ('boy', 'Male')], max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='battle',
            name='teammate2_headgear',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='battle',
            name='teammate2_headgear_main',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='battle',
            name='teammate2_headgear_sub0',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='battle',
            name='teammate2_headgear_sub1',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='battle',
            name='teammate2_headgear_sub2',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='battle',
            name='teammate2_kills',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='battle',
            name='teammate2_level',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='battle',
            name='teammate2_level_star',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='battle',
            name='teammate2_name',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='battle',
            name='teammate2_rank',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='battle',
            name='teammate2_shoes',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='battle',
            name='teammate2_shoes_main',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='battle',
            name='teammate2_shoes_sub0',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='battle',
            name='teammate2_shoes_sub1',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='battle',
            name='teammate2_shoes_sub2',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='battle',
            name='teammate2_specials',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='battle',
            name='teammate2_species',
            field=models.CharField(choices=[('inklings', 'Inkling'), ('octolings', 'Octoling')], max_length=9, null=True),
        ),
        migrations.AddField(
            model_name='battle',
            name='teammate2_splatnet_id',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='battle',
            name='teammate2_weapon',
            field=models.CharField(max_length=4, null=True),
        ),
    ]
