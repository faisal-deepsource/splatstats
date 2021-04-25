from rest_framework import serializers
from rest_framework import permissions
from .models import Battle
from .permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Battle.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username']

class BattleSerializer(serializers.Serializer):
    splatnet_json = serializers.JSONField(required=False)
    stat_ink_json = serializers.JSONField(required=False)

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    
    def get_player_user(self, obj):
        return obj.player_user.username

    def create(self, cleaned_data):
        player_user = self.context['request'].user
        if "splatnet_json" in cleaned_data:
            splatnet_json = cleaned_data["splatnet_json"]
            rule = splatnet_json["rule"]["key"]
            match_type = splatnet_json["type"]
            stage = splatnet_json["stage"]["id"]
            player_weapon = splatnet_json["player_result"]["player"]["weapon"]["id"]
            if "udemae" in splatnet_json:
                player_rank = splatnet_json["udemae"]["number"]
            else:
                player_rank = None
            win = splatnet_json["my_team_result"]["key"] == "victory"
            has_disconnected_player = False
            for teammate in splatnet_json["my_team_members"]:
                has_disconnected_player = has_disconnected_player or (
                    teammate["game_paint_point"] == 0
                    and teammate["kill_count"] == 0
                    and teammate["special_count"] == 0
                    and teammate["death_count"] == 0
                    and teammate["assist_count"] == 0
                )
            for opponent in splatnet_json["other_team_members"]:
                has_disconnected_player = has_disconnected_player or (
                    opponent["game_paint_point"] == 0
                    and opponent["kill_count"] == 0
                    and opponent["special_count"] == 0
                    and opponent["death_count"] == 0
                    and opponent["assist_count"] == 0
                )
            time = splatnet_json["start_time"]
            battle_number = splatnet_json["battle_number"]
            if "win_meter" in splatnet_json:
                win_meter = splatnet_json["win_meter"]
            else:
                win_meter = None
            if rule == "turf_war":
                elapsed_time = 180
            else:
                elapsed_time = splatnet_json["elapsed_time"]

            if "tag_id" in splatnet_json:
                tag_id = splatnet_json["tag_id"]
            else:
                tag_id = None
            if "league_point" in splatnet_json:
                league_point = splatnet_json["league_point"]
            else:
                league_point = None

            splatfest_point = None
            splatfest_title_after = None

            player_level = splatnet_json["player_rank"]
            if "my_team_count" in splatnet_json:
                my_team_count = splatnet_json["my_team_count"]
            elif "my_team_percentage" in splatnet_json:
                my_team_count = splatnet_json["my_team_percentage"]
            else:
                my_team_count = None
            if "other_team_count" in splatnet_json:
                other_team_count = splatnet_json["other_team_count"]
            elif "other_team_percentage" in splatnet_json:
                other_team_count = splatnet_json["other_team_percentage"]
            else:
                other_team_count = None
            player_kills = splatnet_json["player_result"]["kill_count"]
            player_deaths = splatnet_json["player_result"]["death_count"]
            player_assists = splatnet_json["player_result"]["assist_count"]
            player_specials = splatnet_json["player_result"]["special_count"]
            player_game_paint_point = splatnet_json["player_result"]["game_paint_point"]
            player_splatfest_title = None
            if "x_power" in splatnet_json:
                player_x_power = splatnet_json["x_power"]
            else:
                player_x_power = None

            player_headgear = splatnet_json["player_result"]["player"]["head"]["id"]
            player_headgear_main = splatnet_json["player_result"]["player"]["head_skills"]["main"]["id"]
            subs = splatnet_json["player_result"]["player"]["head_skills"]["subs"]
            if len(subs) > 0:
                player_headgear_sub0 = subs[0]["id"]
            if len(subs) > 1:
                player_headgear_sub1 = subs[1]["id"]
            if len(subs) > 2:
                player_headgear_sub2 = subs[2]["id"]
            # clothes
            player_clothes = splatnet_json["player_result"]["player"]["clothes"]["id"]
            player_clothes_main = splatnet_json["player_result"]["player"]["clothes_skills"]["main"]["id"]
            subs = splatnet_json["player_result"]["player"]["clothes_skills"]["subs"]
            if len(subs) > 0:
                player_clothes_sub0 = subs[0]["id"]
            else:
                player_clothes_sub0 = None
            if len(subs) > 1:
                player_clothes_sub1 = subs[1]["id"]
            else:
                player_clothes_sub1 = None
            if len(subs) > 2:
                player_clothes_sub2 = subs[2]["id"]
            else:
                player_clothes_sub2 = None
            # shoes
            player_shoes = splatnet_json["player_result"]["player"]["shoes"]["id"]
            player_shoes_main = splatnet_json["player_result"]["player"]["shoes_skills"]["main"]["id"]
            subs = splatnet_json["player_result"]["player"]["shoes_skills"]["subs"]
            if len(subs) > 0:
                player_shoes_sub0 = subs[0]["id"]
            else:
                player_shoes_sub0 = None
            if len(subs) > 1:
                player_shoes_sub1 = subs[1]["id"]
            else:
                player_shoes_sub1 = None
            if len(subs) > 2:
                player_shoes_sub2 = subs[2]["id"]
            else:
                player_shoes_sub2 = None
            
            if "stat_ink_json" in cleaned_data:
                battle = Battle.objects.create(
                    stat_ink_json=cleaned_data["stat_ink_json"],
                    splatnet_json=splatnet_json,
                    rule=rule,
                    match_type=match_type,
                    stage=stage,
                    player_weapon=player_weapon,
                    player_rank=player_rank,
                    win=win,
                    has_disconnected_player=has_disconnected_player,
                    time=time,
                    battle_number=battle_number,
                    win_meter=win_meter,
                    tag_id=tag_id,
                    player_x_power=player_x_power,
                    league_point=league_point,
                    splatfest_point=splatfest_point,
                    player_splatfest_title=player_splatfest_title,
                    splatfest_title_after=splatfest_title_after,
                    player_level=player_level,
                    my_team_count=my_team_count,
                    other_team_count=other_team_count,
                    player_kills=player_kills,
                    player_deaths=player_deaths,
                    player_assists=player_assists,
                    player_specials=player_specials,
                    player_game_paint_point=player_game_paint_point,
                    elapsed_time=elapsed_time,
                    player_user=player_user,
                    player_headgear=player_headgear,
                    player_headgear_main=player_headgear_main,
                    player_headgear_sub0=player_headgear_sub0,
                    player_headgear_sub1=player_headgear_sub1,
                    player_headgear_sub2=player_headgear_sub2,
                    player_clothes=player_clothes,
                    player_clothes_main=player_clothes_main,
                    player_clothes_sub0=player_clothes_sub0,
                    player_clothes_sub1=player_clothes_sub1,
                    player_clothes_sub2=player_clothes_sub2,
                    player_shoes=player_shoes,
                    player_shoes_main=player_shoes_main,
                    player_shoes_sub0=player_shoes_sub0,
                    player_shoes_sub1=player_shoes_sub1,
                    player_shoes_sub2=player_shoes_sub2,
                )
            else:
                battle = Battle.objects.create(
                    splatnet_json=splatnet_json,
                    rule=rule,
                    match_type=match_type,
                    stage=stage,
                    player_weapon=player_weapon,
                    player_rank=player_rank,
                    win=win,
                    has_disconnected_player=has_disconnected_player,
                    time=time,
                    battle_number=battle_number,
                    win_meter=win_meter,
                    tag_id=tag_id,
                    player_x_power=player_x_power,
                    league_point=league_point,
                    splatfest_point=splatfest_point,
                    player_splatfest_title=player_splatfest_title,
                    splatfest_title_after=splatfest_title_after,
                    player_level=player_level,
                    my_team_count=my_team_count,
                    other_team_count=other_team_count,
                    player_kills=player_kills,
                    player_deaths=player_deaths,
                    player_assists=player_assists,
                    player_specials=player_specials,
                    player_game_paint_point=player_game_paint_point,
                    elapsed_time=elapsed_time,
                    player_user=player_user,
                    player_headgear=player_headgear,
                    player_headgear_main=player_headgear_main,
                    player_headgear_sub0=player_headgear_sub0,
                    player_headgear_sub1=player_headgear_sub1,
                    player_headgear_sub2=player_headgear_sub2,
                    player_clothes=player_clothes,
                    player_clothes_main=player_clothes_main,
                    player_clothes_sub0=player_clothes_sub0,
                    player_clothes_sub1=player_clothes_sub1,
                    player_clothes_sub2=player_clothes_sub2,
                    player_shoes=player_shoes,
                    player_shoes_main=player_shoes_main,
                    player_shoes_sub0=player_shoes_sub0,
                    player_shoes_sub1=player_shoes_sub1,
                    player_shoes_sub2=player_shoes_sub2,
                )
            return battle
        elif "stat_ink_json" in cleaned_data:
            battle = Battle.objects.create(stat_ink_json=cleaned_data["stat_ink_json"])
            return battle
        else:
            return None
