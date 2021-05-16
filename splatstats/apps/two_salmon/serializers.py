from rest_framework.validators import UniqueTogetherValidator
from rest_framework import serializers
from .models import Shift


class ShiftSerializer(serializers.HyperlinkedModelSerializer):
    player_user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Shift
        fields = [
            "url",
            "splatnet_upload",
            "stat_ink_upload",
            "player_user",
            "wave_1_power_eggs",
            "wave_1_golden_delivered",
            "wave_1_golden_appear",
            "wave_1_quota",
            "wave_1_water_level",
            "wave_1_event_type",
            "wave_2_power_eggs",
            "wave_2_golden_delivered",
            "wave_2_golden_appear",
            "wave_2_quota",
            "wave_2_water_level",
            "wave_2_event_type",
            "wave_3_power_eggs",
            "wave_3_golden_delivered",
            "wave_3_golden_appear",
            "wave_3_quota",
            "wave_3_water_level",
            "wave_3_event_type",
            "schedule_weapon_0",
            "schedule_weapon_1",
            "schedule_weapon_2",
            "schedule_weapon_3",
            "stage",
            "schedule_starttime",
            "schedule_endtime",
            "playtime",
            "endtime",
            "starttime",
            "grade_point_delta",
            "job_score",
            "job_failure_reason",
            "is_clear",
            "failure_wave",
            "grade_point",
            "job_id",
            "danger_rate",
            "steel_eel_count",
            "maws_count",
            "scrapper_count",
            "stinger_count",
            "steelhead_count",
            "flyfish_count",
            "drizzler_count",
            "goldie_count",
            "player_species",
            "player_gender",
            "player_title",
            "player_golden_eggs",
            "player_name",
            "player_special",
            "player_weapon_w1",
            "player_weapon_w2",
            "player_weapon_w3",
            "player_revive_count",
            "player_death_count",
            "player_id",
            "player_goldie_kills",
            "player_drizzler_kills",
            "player_griller_kills",
            "player_flyfish_kills",
            "player_steelhead_kills",
            "player_stinger_kills",
            "player_maws_kills",
            "player_scrapper_kills",
            "player_steel_eel_kills",
            "player_w1_specials",
            "player_w2_specials",
            "player_w3_specials",
            "teammate0_species",
            "teammate0_gender",
            "teammate0_title",
            "teammate0_golden_eggs",
            "teammate0_name",
            "teammate0_special",
            "teammate0_weapon_w1",
            "teammate0_weapon_w2",
            "teammate0_weapon_w3",
            "teammate0_revive_count",
            "teammate0_death_count",
            "teammate0_id",
            "teammate0_goldie_kills",
            "teammate0_drizzler_kills",
            "teammate0_griller_kills",
            "teammate0_flyfish_kills",
            "teammate0_steelhead_kills",
            "teammate0_stinger_kills",
            "teammate0_maws_kills",
            "teammate0_scrapper_kills",
            "teammate0_steel_eel_kills",
            "teammate0_w1_specials",
            "teammate0_w2_specials",
            "teammate0_w3_specials",
            "teammate1_species",
            "teammate1_gender",
            "teammate1_title",
            "teammate1_golden_eggs",
            "teammate1_name",
            "teammate1_special",
            "teammate1_weapon_w1",
            "teammate1_weapon_w2",
            "teammate1_weapon_w3",
            "teammate1_revive_count",
            "teammate1_death_count",
            "teammate1_id",
            "teammate1_goldie_kills",
            "teammate1_drizzler_kills",
            "teammate1_griller_kills",
            "teammate1_flyfish_kills",
            "teammate1_steelhead_kills",
            "teammate1_stinger_kills",
            "teammate1_maws_kills",
            "teammate1_scrapper_kills",
            "teammate1_steel_eel_kills",
            "teammate1_w1_specials",
            "teammate1_w2_specials",
            "teammate1_w3_specials",
            "teammate2_species",
            "teammate2_gender",
            "teammate2_title",
            "teammate2_golden_eggs",
            "teammate2_name",
            "teammate2_special",
            "teammate2_weapon_w1",
            "teammate2_weapon_w2",
            "teammate2_weapon_w3",
            "teammate2_revive_count",
            "teammate2_death_count",
            "teammate2_id",
            "teammate2_goldie_kills",
            "teammate2_drizzler_kills",
            "teammate2_griller_kills",
            "teammate2_flyfish_kills",
            "teammate2_steelhead_kills",
            "teammate2_stinger_kills",
            "teammate2_maws_kills",
            "teammate2_scrapper_kills",
            "teammate2_steel_eel_kills",
            "teammate2_w1_specials",
            "teammate2_w2_specials",
            "teammate2_w3_specials",
        ]
        validators = [
            UniqueTogetherValidator(
                queryset=Shift.objects.all(),
                fields=['player_id', 'job_id']
            )
        ]
