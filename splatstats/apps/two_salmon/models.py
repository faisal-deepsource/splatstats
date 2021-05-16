from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from ...models import species, gender

# Create your models here.

events = (
    ("cohock-charge", _("Cohock Charge")),
    ("fog", _("Fog")),
    ("griller", _("The Griller")),
    ("goldie-seeking", _("Goldie Seeking")),
    ("rush", _("Rush")),
    ("the-mothership", _("The Mothership")),
    ("water-levels", _("-")),
)

tides = (("low", _("Low Tide")), ("normal", _("Normal")), ("high", _("High tide")))

fail_reasons = (("wipe_out", _("wipe_out")), ("time_limit", _("time_limit")))

titles = (
    ("1", _("Apprentice")),
    ("2", _("Part Timer")),
    ("3", _("Go Getter")),
    ("4", "Overachiever"),
    ("5", _("Profreshional")),
)

specials = (
    ("2", _("Splat-Bomb Launcher")),
    ("7", _("Sting Ray")),
    ("8", _("Inkjet")),
    ("9", _("Splashdown")),
)

weapons = (
    ("all", _("All Weapons")),
    ("-1", _("Random")),
    ("0", _("Sploosh-o-matic")),
    ("10", _("Splattershot Jr.")),
    ("20", _("Splash-o-matic")),
    ("30", _("Aerospray MG")),
    ("40", _("Splattershot")),
    ("50", _(".52 Gal")),
    ("60", _("N-ZAP '85")),
    ("70", _("Splattershot Pro")),
    ("80", _(".96 Gal")),
    ("90", _("Jet Squelcher")),
    ("200", _("Luna Blaster")),
    ("210", _("Blaster")),
    ("220", _("Range Blaster")),
    ("230", _("Clash Blaster")),
    ("240", _("Rapid Blaster")),
    ("250", _("Rapid Blaster Pro")),
    ("300", _("L-3 Nozzlenose")),
    ("310", _("H-3 Nozzlenose")),
    ("400", _("Squeezer")),
    ("1000", _("Carbon Roller")),
    ("1010", _("Splat Roller")),
    ("1020", _("Dynamo Roller")),
    ("1030", _("Flingza Roller")),
    ("1100", _("Inkbrush")),
    ("1110", _("Octobrush")),
    ("2000", _("Classic Squiffer")),
    ("2010", _("Splat Charger")),
    ("2020", _("Splatterscope")),
    ("2030", _("E-liter 4K")),
    ("2040", _("E-liter 4K Scope")),
    ("2050", _("Bamboozler 14 Mk I")),
    ("2060", _("Goo Tuber")),
    ("3000", _("Slosher")),
    ("3002", _("Soda Slosher")),
    ("3010", _("Tri-Slosher")),
    ("3020", _("Sloshing Machine")),
    ("3030", _("Bloblobber")),
    ("3040", _("Explosher")),
    ("4000", _("Mini Splatling")),
    ("4010", _("Heavy Splatling")),
    ("4020", _("Hydra Splatling")),
    ("4030", _("Ballpoint Splatling")),
    ("4040", _("Nautilus 47")),
    ("5000", _("Dapple Dualies")),
    ("5010", _("Splat Dualies")),
    ("5020", _("Glooga Dualies")),
    ("5030", _("Dualie Squelchers")),
    ("5040", _("Dark Tetra Dualies")),
    ("6000", _("Splat Brella")),
    ("6010", _("Tenta Brella")),
    ("6020", _("Undercover Brella")),
    ("20000", _("Grizzco Blaster")),
    ("20010", _("Grizzco Brella")),
    ("20020", _("Grizzco Charger")),
    ("20030", _("Grizzco Slosher")),
)

stages = (
    ("Salmonid Smokeyard", _("Salmonid Smokeyard")),
    ("Ruins of Ark Polaris", _("Ruins of Ark Polaris")),
    ("Spawning Grounds", _("Spawning Grounds")),
    ("Marooner's Bay", _("Marooner's Bay")),
    ("Lost Outpost", _("Lost Outpost")),
)


class Shift(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["player_id", "job_id"], name="unique-two-shift"
            ),
        ]

    player_user = models.ForeignKey(
        User, related_name="two_salmon", on_delete=models.CASCADE, null=True
    )
    splatnet_json = models.JSONField("splatNet 2 JSON file", blank=True, null=True)
    splatnet_upload = models.BooleanField(null=True)
    stat_ink_upload = models.BooleanField(null=True)
    wave_1_power_eggs = models.PositiveSmallIntegerField(null=True)
    wave_1_golden_delivered = models.PositiveSmallIntegerField(null=True)
    wave_1_golden_appear = models.PositiveSmallIntegerField(null=True)
    wave_1_quota = models.PositiveSmallIntegerField(null=True)
    wave_1_water_level = models.CharField(max_length=6, choices=tides, null=True)
    wave_1_event_type = models.CharField(max_length=20, choices=events, null=True)
    wave_2_power_eggs = models.PositiveSmallIntegerField(null=True)
    wave_2_golden_delivered = models.PositiveSmallIntegerField(null=True)
    wave_2_golden_appear = models.PositiveSmallIntegerField(null=True)
    wave_2_quota = models.PositiveSmallIntegerField(null=True)
    wave_2_water_level = models.CharField(max_length=6, choices=tides, null=True)
    wave_2_event_type = models.CharField(max_length=20, choices=events, null=True)
    wave_3_power_eggs = models.PositiveSmallIntegerField(null=True)
    wave_3_golden_delivered = models.PositiveSmallIntegerField(null=True)
    wave_3_golden_appear = models.PositiveSmallIntegerField(null=True)
    wave_3_quota = models.PositiveSmallIntegerField(null=True)
    wave_3_water_level = models.CharField(max_length=6, choices=tides, null=True)
    wave_3_event_type = models.CharField(max_length=20, choices=events, null=True)
    schedule_weapon_0 = models.CharField(max_length=5, choices=weapons, null=True)
    schedule_weapon_1 = models.CharField(max_length=5, choices=weapons, null=True)
    schedule_weapon_2 = models.CharField(max_length=5, choices=weapons, null=True)
    schedule_weapon_3 = models.CharField(max_length=5, choices=weapons, null=True)
    stage = models.CharField(max_length=20, choices=stages, null=True)
    schedule_starttime = models.DateTimeField(null=True)
    schedule_endtime = models.DateTimeField(null=True)
    playtime = models.DateTimeField(null=True)
    endtime = models.DateTimeField(null=True)
    starttime = models.DateTimeField(null=True)
    grade_point_delta = models.SmallIntegerField(null=True)
    job_score = models.PositiveSmallIntegerField(null=True)
    job_failure_reason = models.CharField(
        max_length=20, choices=fail_reasons, null=True
    )
    is_clear = models.BooleanField(null=True)
    failure_wave = models.PositiveSmallIntegerField(null=True)
    grade_point = models.PositiveSmallIntegerField(null=True)
    job_id = models.PositiveIntegerField(null=True)
    danger_rate = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    steel_eel_count = models.PositiveSmallIntegerField(null=True)
    maws_count = models.PositiveSmallIntegerField(null=True)
    scrapper_count = models.PositiveSmallIntegerField(null=True)
    stinger_count = models.PositiveSmallIntegerField(null=True)
    steelhead_count = models.PositiveSmallIntegerField(null=True)
    flyfish_count = models.PositiveSmallIntegerField(null=True)
    drizzler_count = models.PositiveSmallIntegerField(null=True)
    griller_count = models.PositiveSmallIntegerField(null=True)
    goldie_count = models.PositiveSmallIntegerField(null=True)
    player_species = models.CharField(max_length=9, choices=species, null=True)
    player_gender = models.CharField(max_length=4, choices=gender, null=True)
    player_title = models.CharField(max_length=1, choices=titles, null=True)
    player_golden_eggs = models.PositiveSmallIntegerField(null=True)
    player_power_eggs = models.PositiveSmallIntegerField(null=True)
    player_name = models.CharField(max_length=10, null=True)
    player_special = models.CharField(max_length=2, choices=specials, null=True)
    player_weapon_w1 = models.CharField(max_length=5, choices=weapons, null=True)
    player_weapon_w2 = models.CharField(max_length=5, choices=weapons, null=True)
    player_weapon_w3 = models.CharField(max_length=5, choices=weapons, null=True)
    player_revive_count = models.PositiveSmallIntegerField(null=True)
    player_death_count = models.PositiveSmallIntegerField(null=True)
    player_id = models.CharField(max_length=16, null=True)
    player_goldie_kills = models.PositiveSmallIntegerField(null=True)
    player_drizzler_kills = models.PositiveSmallIntegerField(null=True)
    player_griller_kills = models.PositiveSmallIntegerField(null=True)
    player_flyfish_kills = models.PositiveSmallIntegerField(null=True)
    player_steelhead_kills = models.PositiveSmallIntegerField(null=True)
    player_stinger_kills = models.PositiveSmallIntegerField(null=True)
    player_maws_kills = models.PositiveSmallIntegerField(null=True)
    player_scrapper_kills = models.PositiveSmallIntegerField(null=True)
    player_steel_eel_kills = models.PositiveSmallIntegerField(null=True)
    player_w1_specials = models.PositiveSmallIntegerField(null=True)
    player_w2_specials = models.PositiveSmallIntegerField(null=True)
    player_w3_specials = models.PositiveSmallIntegerField(null=True)
    teammate0_species = models.CharField(max_length=9, choices=species, null=True)
    teammate0_gender = models.CharField(max_length=4, choices=gender, null=True)
    teammate0_title = models.CharField(max_length=1, choices=titles, null=True)
    teammate0_golden_eggs = models.PositiveSmallIntegerField(null=True)
    teammate0_power_eggs = models.PositiveSmallIntegerField(null=True)
    teammate0_name = models.CharField(max_length=10, null=True)
    teammate0_special = models.CharField(max_length=2, choices=specials, null=True)
    teammate0_weapon_w1 = models.CharField(max_length=5, choices=weapons, null=True)
    teammate0_weapon_w2 = models.CharField(max_length=5, choices=weapons, null=True)
    teammate0_weapon_w3 = models.CharField(max_length=5, choices=weapons, null=True)
    teammate0_revive_count = models.PositiveSmallIntegerField(null=True)
    teammate0_death_count = models.PositiveSmallIntegerField(null=True)
    teammate0_id = models.CharField(max_length=16, null=True)
    teammate0_goldie_kills = models.PositiveSmallIntegerField(null=True)
    teammate0_drizzler_kills = models.PositiveSmallIntegerField(null=True)
    teammate0_griller_kills = models.PositiveSmallIntegerField(null=True)
    teammate0_flyfish_kills = models.PositiveSmallIntegerField(null=True)
    teammate0_steelhead_kills = models.PositiveSmallIntegerField(null=True)
    teammate0_stinger_kills = models.PositiveSmallIntegerField(null=True)
    teammate0_maws_kills = models.PositiveSmallIntegerField(null=True)
    teammate0_scrapper_kills = models.PositiveSmallIntegerField(null=True)
    teammate0_steel_eel_kills = models.PositiveSmallIntegerField(null=True)
    teammate0_w1_specials = models.PositiveSmallIntegerField(null=True)
    teammate0_w2_specials = models.PositiveSmallIntegerField(null=True)
    teammate0_w3_specials = models.PositiveSmallIntegerField(null=True)
    teammate1_species = models.CharField(max_length=9, choices=species, null=True)
    teammate1_gender = models.CharField(max_length=4, choices=gender, null=True)
    teammate1_title = models.CharField(max_length=1, choices=titles, null=True)
    teammate1_golden_eggs = models.PositiveSmallIntegerField(null=True)
    teammate1_power_eggs = models.PositiveSmallIntegerField(null=True)
    teammate1_name = models.CharField(max_length=10, null=True)
    teammate1_special = models.CharField(max_length=2, choices=specials, null=True)
    teammate1_weapon_w1 = models.CharField(max_length=5, choices=weapons, null=True)
    teammate1_weapon_w2 = models.CharField(max_length=5, choices=weapons, null=True)
    teammate1_weapon_w3 = models.CharField(max_length=5, choices=weapons, null=True)
    teammate1_revive_count = models.PositiveSmallIntegerField(null=True)
    teammate1_death_count = models.PositiveSmallIntegerField(null=True)
    teammate1_id = models.CharField(max_length=16, null=True)
    teammate1_goldie_kills = models.PositiveSmallIntegerField(null=True)
    teammate1_drizzler_kills = models.PositiveSmallIntegerField(null=True)
    teammate1_griller_kills = models.PositiveSmallIntegerField(null=True)
    teammate1_flyfish_kills = models.PositiveSmallIntegerField(null=True)
    teammate1_steelhead_kills = models.PositiveSmallIntegerField(null=True)
    teammate1_stinger_kills = models.PositiveSmallIntegerField(null=True)
    teammate1_maws_kills = models.PositiveSmallIntegerField(null=True)
    teammate1_scrapper_kills = models.PositiveSmallIntegerField(null=True)
    teammate1_steel_eel_kills = models.PositiveSmallIntegerField(null=True)
    teammate1_w1_specials = models.PositiveSmallIntegerField(null=True)
    teammate1_w2_specials = models.PositiveSmallIntegerField(null=True)
    teammate1_w3_specials = models.PositiveSmallIntegerField(null=True)
    teammate2_species = models.CharField(max_length=9, choices=species, null=True)
    teammate2_gender = models.CharField(max_length=4, choices=gender, null=True)
    teammate2_title = models.CharField(max_length=1, choices=titles, null=True)
    teammate2_golden_eggs = models.PositiveSmallIntegerField(null=True)
    teammate2_power_eggs = models.PositiveSmallIntegerField(null=True)
    teammate2_name = models.CharField(max_length=10, null=True)
    teammate2_special = models.CharField(max_length=2, choices=specials, null=True)
    teammate2_weapon_w1 = models.CharField(max_length=5, choices=weapons, null=True)
    teammate2_weapon_w2 = models.CharField(max_length=5, choices=weapons, null=True)
    teammate2_weapon_w3 = models.CharField(max_length=5, choices=weapons, null=True)
    teammate2_revive_count = models.PositiveSmallIntegerField(null=True)
    teammate2_death_count = models.PositiveSmallIntegerField(null=True)
    teammate2_id = models.CharField(max_length=16, null=True)
    teammate2_goldie_kills = models.PositiveSmallIntegerField(null=True)
    teammate2_drizzler_kills = models.PositiveSmallIntegerField(null=True)
    teammate2_griller_kills = models.PositiveSmallIntegerField(null=True)
    teammate2_flyfish_kills = models.PositiveSmallIntegerField(null=True)
    teammate2_steelhead_kills = models.PositiveSmallIntegerField(null=True)
    teammate2_stinger_kills = models.PositiveSmallIntegerField(null=True)
    teammate2_maws_kills = models.PositiveSmallIntegerField(null=True)
    teammate2_scrapper_kills = models.PositiveSmallIntegerField(null=True)
    teammate2_steel_eel_kills = models.PositiveSmallIntegerField(null=True)
    teammate2_w1_specials = models.PositiveSmallIntegerField(null=True)
    teammate2_w2_specials = models.PositiveSmallIntegerField(null=True)
    teammate2_w3_specials = models.PositiveSmallIntegerField(null=True)
