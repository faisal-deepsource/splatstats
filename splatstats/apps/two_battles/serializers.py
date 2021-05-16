from rest_framework import serializers
from .models import Battle
from rest_framework.validators import UniqueTogetherValidator


class BattleSerializer(serializers.HyperlinkedModelSerializer):
    player_user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Battle
        fields = (
            "url",
            "id",
            "splatnet_json",
            "stat_ink_json",
            "splatnet_upload",
            "stat_ink_upload",
            "rule",
            "match_type",
            "stage",
            "win",
            "has_disconnected_player",
            "time",
            "battle_number",
            "win_meter",
            "my_team_count",
            "other_team_count",
            "elapsed_time",
            "image_result",
            "image_gear",
            "tag_id",
            "league_point",
            "splatfest_point",
            "splatfest_title_after",
            "player_x_power",
            "player_user",
            "player_weapon",
            "player_rank",
            "player_level",
            "player_level_star",
            "player_kills",
            "player_deaths",
            "player_assists",
            "player_specials",
            "player_game_paint_point",
            "player_splatfest_title",
            "player_splatnet_id",
            "player_name",
            "player_gender",
            "player_species",
            "player_headgear",
            "player_headgear_main",
            "player_headgear_sub0",
            "player_headgear_sub1",
            "player_headgear_sub2",
            "player_clothes",
            "player_clothes_main",
            "player_clothes_sub0",
            "player_clothes_sub1",
            "player_clothes_sub2",
            "player_shoes",
            "player_shoes_main",
            "player_shoes_sub0",
            "player_shoes_sub1",
            "player_shoes_sub2",
            "teammate0_weapon",
            "teammate0_rank",
            "teammate0_level",
            "teammate0_level_star",
            "teammate0_kills",
            "teammate0_deaths",
            "teammate0_assists",
            "teammate0_specials",
            "teammate0_game_paint_point",
            "teammate0_splatnet_id",
            "teammate0_name",
            "teammate0_gender",
            "teammate0_species",
            "teammate0_headgear",
            "teammate0_headgear_main",
            "teammate0_headgear_sub0",
            "teammate0_headgear_sub1",
            "teammate0_headgear_sub2",
            "teammate0_clothes",
            "teammate0_clothes_main",
            "teammate0_clothes_sub0",
            "teammate0_clothes_sub1",
            "teammate0_clothes_sub2",
            "teammate0_shoes",
            "teammate0_shoes_main",
            "teammate0_shoes_sub0",
            "teammate0_shoes_sub1",
            "teammate0_shoes_sub2",
            "teammate1_weapon",
            "teammate1_rank",
            "teammate1_level",
            "teammate1_level_star",
            "teammate1_kills",
            "teammate1_deaths",
            "teammate1_assists",
            "teammate1_specials",
            "teammate1_game_paint_point",
            "teammate1_splatnet_id",
            "teammate1_name",
            "teammate1_gender",
            "teammate1_species",
            "teammate1_headgear",
            "teammate1_headgear_main",
            "teammate1_headgear_sub0",
            "teammate1_headgear_sub1",
            "teammate1_headgear_sub2",
            "teammate1_clothes",
            "teammate1_clothes_main",
            "teammate1_clothes_sub0",
            "teammate1_clothes_sub1",
            "teammate1_clothes_sub2",
            "teammate1_shoes",
            "teammate1_shoes_main",
            "teammate1_shoes_sub0",
            "teammate1_shoes_sub1",
            "teammate1_shoes_sub2",
            "teammate2_weapon",
            "teammate2_rank",
            "teammate2_level",
            "teammate2_level_star",
            "teammate2_kills",
            "teammate2_deaths",
            "teammate2_assists",
            "teammate2_specials",
            "teammate2_game_paint_point",
            "teammate2_splatnet_id",
            "teammate2_name",
            "teammate2_gender",
            "teammate2_species",
            "teammate2_headgear",
            "teammate2_headgear_main",
            "teammate2_headgear_sub0",
            "teammate2_headgear_sub1",
            "teammate2_headgear_sub2",
            "teammate2_clothes",
            "teammate2_clothes_main",
            "teammate2_clothes_sub0",
            "teammate2_clothes_sub1",
            "teammate2_clothes_sub2",
            "teammate2_shoes",
            "teammate2_shoes_main",
            "teammate2_shoes_sub0",
            "teammate2_shoes_sub1",
            "teammate2_shoes_sub2",
            "opponent0_weapon",
            "opponent0_rank",
            "opponent0_level",
            "opponent0_level_star",
            "opponent0_kills",
            "opponent0_deaths",
            "opponent0_assists",
            "opponent0_specials",
            "opponent0_game_paint_point",
            "opponent0_splatnet_id",
            "opponent0_name",
            "opponent0_gender",
            "opponent0_species",
            "opponent0_headgear",
            "opponent0_headgear_main",
            "opponent0_headgear_sub0",
            "opponent0_headgear_sub1",
            "opponent0_headgear_sub2",
            "opponent0_clothes",
            "opponent0_clothes_main",
            "opponent0_clothes_sub0",
            "opponent0_clothes_sub1",
            "opponent0_clothes_sub2",
            "opponent0_shoes",
            "opponent0_shoes_main",
            "opponent0_shoes_sub0",
            "opponent0_shoes_sub1",
            "opponent0_shoes_sub2",
            "opponent1_weapon",
            "opponent1_rank",
            "opponent1_level",
            "opponent1_level_star",
            "opponent1_kills",
            "opponent1_deaths",
            "opponent1_assists",
            "opponent1_specials",
            "opponent1_game_paint_point",
            "opponent1_splatnet_id",
            "opponent1_name",
            "opponent1_gender",
            "opponent1_species",
            "opponent1_headgear",
            "opponent1_headgear_main",
            "opponent1_headgear_sub0",
            "opponent1_headgear_sub1",
            "opponent1_headgear_sub2",
            "opponent1_clothes",
            "opponent1_clothes_main",
            "opponent1_clothes_sub0",
            "opponent1_clothes_sub1",
            "opponent1_clothes_sub2",
            "opponent1_shoes",
            "opponent1_shoes_main",
            "opponent1_shoes_sub0",
            "opponent1_shoes_sub1",
            "opponent1_shoes_sub2",
            "opponent2_weapon",
            "opponent2_rank",
            "opponent2_level",
            "opponent2_level_star",
            "opponent2_kills",
            "opponent2_deaths",
            "opponent2_assists",
            "opponent2_specials",
            "opponent2_game_paint_point",
            "opponent2_splatnet_id",
            "opponent2_name",
            "opponent2_gender",
            "opponent2_species",
            "opponent2_headgear",
            "opponent2_headgear_main",
            "opponent2_headgear_sub0",
            "opponent2_headgear_sub1",
            "opponent2_headgear_sub2",
            "opponent2_clothes",
            "opponent2_clothes_main",
            "opponent2_clothes_sub0",
            "opponent2_clothes_sub1",
            "opponent2_clothes_sub2",
            "opponent2_shoes",
            "opponent2_shoes_main",
            "opponent2_shoes_sub0",
            "opponent2_shoes_sub1",
            "opponent2_shoes_sub2",
            "opponent3_weapon",
            "opponent3_rank",
            "opponent3_level",
            "opponent3_level_star",
            "opponent3_kills",
            "opponent3_deaths",
            "opponent3_assists",
            "opponent3_specials",
            "opponent3_game_paint_point",
            "opponent3_splatnet_id",
            "opponent3_name",
            "opponent3_gender",
            "opponent3_species",
            "opponent3_headgear",
            "opponent3_headgear_main",
            "opponent3_headgear_sub0",
            "opponent3_headgear_sub1",
            "opponent3_headgear_sub2",
            "opponent3_clothes",
            "opponent3_clothes_main",
            "opponent3_clothes_sub0",
            "opponent3_clothes_sub1",
            "opponent3_clothes_sub2",
            "opponent3_shoes",
            "opponent3_shoes_main",
            "opponent3_shoes_sub0",
            "opponent3_shoes_sub1",
            "opponent3_shoes_sub2",
        )
        validators = [
            UniqueTogetherValidator(
                queryset=Battle.objects.all(),
                fields=("player_splatnet_id", "battle_number"),
            )
        ]
