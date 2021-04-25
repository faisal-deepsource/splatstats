from django.db import models
from django.db.models.deletion import CASCADE
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

# Create your models here.
class Battle(models.Model):
    class Rule(models.TextChoices):
        sz = "splat_zones", _("Splat Zones")
        rm = "rainmaker", _("Rainmaker")
        cb = "clam_blitz", _("Clam Blitz")
        tc = "tower_control", _("Tower Control")
        tw = "turf_war", _("Turf War")

    class Match_Type(models.TextChoices):
        lp = "league_pair", _("League Pair")
        lt = "league_team", _("League Team")
        rk = "gachi", _("Ranked")
        pv = "private", _("Private")
        rg = "regular", _("Turf War")
        fs = "fes_solo", _("Splatfest Solo/Pro")
        ft = "fes_team", _("Splatfest Team/Normal")

    # general match stats
    splatnet_json = models.JSONField("splatNet 2 JSON file", blank=True, null=True)
    stat_ink_json = models.JSONField("stat.ink JSON file", blank=True, null=True)
    rule = models.CharField(max_length=13, choices=Rule.choices)
    match_type = models.CharField(max_length=11, choices=Match_Type.choices)
    stage = models.CharField(max_length=2)
    win = models.BooleanField(null=True)
    has_disconnected_player = models.BooleanField(null=True)
    time = models.PositiveIntegerField(null=True)
    battle_number = models.CharField("SplatNet Battle Number", max_length=255)
    win_meter = models.IntegerField("Freshness", blank=True, null=True)
    my_team_count = models.DecimalField(decimal_places=1, max_digits=4, null=True)
    other_team_count = models.DecimalField(decimal_places=1, max_digits=4, null=True)
    elapsed_time = models.PositiveIntegerField(null=True)

    # team stuff
    tag_id = models.CharField("Team ID", null=True, blank=True, max_length=11)
    league_point = models.DecimalField(
        blank=True, null=True, decimal_places=1, max_digits=5
    )

    # splatfest stuff
    splatfest_point = models.DecimalField(
        blank=True, null=True, decimal_places=1, max_digits=5
    )
    splatfest_title_after = models.TextField(blank=True, null=True)

    # player basic stats
    player_x_power = models.DecimalField(blank=True, null=True, decimal_places=1, max_digits=5)
    player_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    player_weapon = models.CharField(max_length=4)
    player_rank = models.IntegerField(null=True)
    player_level = models.PositiveSmallIntegerField(null=True)
    player_level_star = models.PositiveSmallIntegerField(null=True)
    player_kills = models.PositiveSmallIntegerField(null=True)
    player_deaths = models.PositiveSmallIntegerField(null=True)
    player_assists = models.PositiveSmallIntegerField(null=True)
    player_specials = models.PositiveSmallIntegerField(null=True)
    player_game_paint_point = models.PositiveSmallIntegerField(null=True)
    player_splatfest_title = models.TextField(blank=True, null=True)
    player_splatnet_id = models.CharField(max_length=16, null=True)
    player_name = models.CharField(max_length=10, null=True)

    # player gear
    # headgear
    player_headgear = models.CharField(null=True, max_length=5)
    player_headgear_main = models.CharField(null=True, max_length=5)
    player_headgear_sub0 = models.CharField(null=True, max_length=5)
    player_headgear_sub1 = models.CharField(null=True, max_length=5)
    player_headgear_sub2 = models.CharField(null=True, max_length=5)
    # clothes
    player_clothes = models.CharField(null=True, max_length=5)
    player_clothes_main = models.CharField(null=True, max_length=5)
    player_clothes_sub0 = models.CharField(null=True, max_length=5)
    player_clothes_sub1 = models.CharField(null=True, max_length=5)
    player_clothes_sub2 = models.CharField(null=True, max_length=5)
    # shoes
    player_shoes = models.CharField(null=True, max_length=5)
    player_shoes_main = models.CharField(null=True, max_length=5)
    player_shoes_sub0 = models.CharField(null=True, max_length=5)
    player_shoes_sub1 = models.CharField(null=True, max_length=5)
    player_shoes_sub2 = models.CharField(null=True, max_length=5)

    @classmethod
    def create(cls, **kwargs):
        splatnet_json = None
        stat_ink_json = None
        player_user = kwargs["user"]
        if "splatnet_json" in kwargs:
            splatnet_json = kwargs["splatnet_json"]
            rule = splatnet_json["rule"]["key"]
            match_type = splatnet_json["type"]
            stage = splatnet_json["stage"]["id"]
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
            if rule == "turf_war":
                elapsed_time = 180
            else:
                elapsed_time = splatnet_json["elapsed_time"]

            if "tag_id" in splatnet_json:
                tag_id = splatnet_json["tag_id"]
            else:
                tag_id = None
            x_power = splatnet_json["x_power"]
            if "league_point" in splatnet_json:
                league_point = splatnet_json["league_point"]
            else:
                league_point = None
            
            splatfest_point = None
            splatfest_title_after = None
            
            player_splatnet_id = splatnet_json["player_result"]["player"]["principal_id"]
            player_name = splatnet_json["player_result"]["player"]["nickname"]
            player_weapon = splatnet_json["player_result"]["player"]["weapon"]["id"]
            player_rank = splatnet_json["udemae"]["number"]
            player_splatfest_title = None
            player_level_star = splatnet_json["star_rank"]
            player_level = splatnet_json["player_rank"]
            player_kills = splatnet_json["player_result"]["kill_count"]
            player_deaths = splatnet_json["player_result"]["death_count"]
            player_assists = splatnet_json["player_result"]["assist_count"]
            player_specials = splatnet_json["player_result"]["special_count"]
            player_game_paint_point = splatnet_json["player_result"]["game_paint_point"]

            # headgear
            player_headgear = splatnet_json["player_result"]["player"]["head"]["id"]
            player_headgear_main = splatnet_json["player_result"]["player"]["head_skills"]["main"]["id"]
            subs = splatnet_json["player_result"]["player"]["head_skills"]["subs"]
            if len(subs) > 0:
                player_headgear_sub0 = subs[0]["id"]
            else:
                player_headgear_sub0 = None
            if len(subs) > 1:
                player_headgear_sub1 = subs[1]["id"]
            else:
                player_headgear_sub1 = None
            if len(subs) > 2:
                player_headgear_sub2 = subs[2]["id"]
            else:
                player_headgear_sub2 = None
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

        if "stat_ink_json" in kwargs:
            stat_ink_json = kwargs["stat_ink_json"]

        battle = cls(
            splatnet_json=splatnet_json,
            stat_ink_json=stat_ink_json,
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
            x_power=x_power,
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
            player_splatnet_id=player_splatnet_id,
            player_name=player_name,
            player_level_star=player_level_star,
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

    def __str__(self):
        return str(self.id)


from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)