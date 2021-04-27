from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
import sys

sys.path.append("..")
from models import Species, Gender

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
        rg = "turf_war", _("Turf War")
        fs = "fes_solo", _("Splatfest Solo/Pro")
        ft = "fes_team", _("Splatfest Team/Normal")

    class Ranks(models.IntegerChoices):
        c_minus = 0, _("C-")
        c_rank = 1, _("C")
        c_plus = 2, _("C+")
        b_minus = 3, _("B-")
        b_rank = 4, _("B")
        b_plus = 5, _("B+")
        a_minus = 6, _("A-")
        a_rank = 7, _("A")
        a_plus = 8, _("A+")
        s_rank = 9, _("S")
        s_plus0 = 10, _("S+0")
        s_plus1 = 11, _("S+1")
        s_plus2 = 12, _("S+2")

    class Weapons(models.TextChoices):
        bold = "0", _("Sploosh-o-matic")
        bold_neo = "1", _("Neo Sploosh-o-matic")
        bold_7 = "2", _("Sploosh-o-matic 7")
        wakaba = "10", _("Splattershot Jr.")
        momiji = "11", _("Custom Splattershot Jr.")
        ochiba = "12", _("Kensa Splattershot Jr.")
        sharp = "20", _("Splash-o-matic")
        sharp_neo = "21", _("Neo Splash-o-matic")
        promodeler_mg = "30", _("Aerospray MG")
        promodeler_rg = "31", _("Aerospray RG")
        promodeler_pg = "32", _("Aerospray PG")
        sshooter = "40", _("Splattershot")
        sshooter_collabo = "41", _("Tentatek Splattershot")
        sshooter_becchu = "42", _("Kensa Splattershot")
        heroshooter_replica = "45", _("Hero Shot Replica")
        octoshooter_replica = "46", _("Octo Shot Replica")
        five2gal = "50", _(".52 Gal")
        five2gal_deco = "51", _(".52 Gal Deco")
        five2gal_becchu = "52", _("Kensa .52 Gal")
        nzap85 = "60", _("N-ZAP '85")
        nzap89 = "61", _("N-ZAP '89")
        nzap83 = "62", _("N-ZAP '83")
        prime = "70", _("Splattershot Pro")
        prime_collabo = "71", _("Forge Splattershot Pro")
        prime_becchu = "72", _("Kensa Splattershot Pro")
        nine6gal = "80", _(".96 Gal")
        nine6gal_deco = "81", _(".96 Gal Deco")
        jetsweeper = "90", _("Jet Squelcher")
        jetsweeper_custom = "91", _("Custom Jet Squelcher")
        nova = "200", _("Luna Blaster")
        nova_neo = "201", _("Luna Blaster Neo")
        nova_becchu = "202", _("Kensa Luna Blaster")
        hotblaster = "210", _("Blaster")
        hotblaster_custom = "211", _("Custom Blaster")
        heroblaster_replica = "215", _("Hero Blaster Replica")
        longblaster = "220", _("Range Blaster")
        longblaster_custom = "221", _("Custom Range Blaster")
        longblaster_necro = "222", _("Grim Range Blaster")
        clashblaster = "230", _("Clash Blaster")
        clashblaster_neo = "231", _("Clash Blaster Neo")
        rapid = "240", _("Rapid Blaster")
        rapid_deco = "241", _("Rapid Blaster Deco")
        rapid_becchu = "242", _("Kensa Rapid Blaster")
        rapid_elite = "250", _("Rapid Blaster Pro")
        rapid_elite_deco = "251", _("Rapid Blaster Pro Deco")
        l3reelgun = "300", _("L-3 Nozzlenose")
        l3reelgun_d = "301", _("L-3 Nozzlenose D")
        l3reelgun_becchu = "302", _("Kensa L-3 Nozzlenose")
        h3reelgun = "310", _("H-3 Nozzlenose")
        h3reelgun_d = "311", _("H-3 Nozzlenose D")
        h3reelgun_cherry = "312", _("Cherry H-3 Nozzlenose")
        bottlegeyser = "400", _("Squeezer")
        bottlegeyser_foil = "401", _("Foil Squeezer")
        carbon = "1000", _("Carbon Roller")
        carbon_deco = "1001", _("Carbon Roller Deco")
        splatroller = "1010", _("Splat Roller")
        splatroller_collabu = "1011", _("Krak-On Splat Roller")
        splatroller_becchu = "1012", _("Kensa Splat Roller")
        heroroller_replica = "1015", _("Hero Roller Replica")
        dynamo = "1020", _("Dynamo Roller")
        dynamo_tesla = "1021", _("Gold Dynamo Roller")
        dynamo_becchu = "1022", _("Kensa Dynamo Roller")
        variableroller = "1030", _("Flingza Roller")
        variableroller_foil = "1031", _("Foil Flingza Roller")
        pablo = "1100", _("Inkbrush")
        pablo_hue = "1101", _("Inkbrush Nouveau")
        pablo_permanent = "1102", _("Permanent Inkbrush")
        hokusai = "1110", _("Octobrush")
        hokusai_hue = "1111", _("Octobrush Nouveau")
        hokusai_becchu = "1112", _("Kensa Octobrush")
        herobrush_replica = "1115", _("Herobrush Replica")
        squiclean_a = "2000", _("Classic Squiffer")
        squiclean_b = "2001", _("New Squiffer")
        squiclean_g = "2002", _("Fresh Squiffer")
        splatcharger = "2010", _("Splat Charger")
        splatcharger_collabo = "2011", _("Firefin Splat Charger")
        splatcharger_becchu = "2012", _("Kensa Charger")
        herocharger_replica = "2015", _("Hero Charger Replica")
        splatscope = "2020", _("Splatterscope")
        splatscope_colalbo = "2021", _("Firefin Splatterscope")
        splatscope_becchu = "2022", _("Kensa Splatterscope")
        liter4k = "2030", _("E-liter 4K")
        liter4k_custom = "2031", _("Custom E-liter 4K")
        liter4k_scope = "2040", _("E-liter 4K Scope")
        liter4k_scope_custom = "2041", _("Custom E-liter 4K Scope")
        bamboo14mk1 = "2050", _("Bamboozler 14 Mk I")
        bamboo14mk2 = "2051", _("Bamboozler 14 Mk II")
        bamboo14mk3 = "2052", _("Bamboozler 14 Mk III")
        soytuber = "2060", _("Goo Tuber")
        soytuber_custom = "2061", _("Custom Goo Tuber")
        bucketslosher = "3000", _("Slosher")
        bucketslosher_deco = "3001", _("Slosher Deco")
        bucketslosher_soda = "3002", _("Soda Slosher")
        heroslosher_replica = "3005", _("Hero Slosher Replica")
        hissen = "3010", _("Tri-Slosher")
        hissen_hue = "3011", _("Tri-Slosher Nouveau")
        screwslosher = "3020", _("Sloshing Machine")
        screwslosher_neo = "3021", _("Sloshing Machine Neo")
        screwslosher_becchu = "3022", _("Kensa Sloshing Machine")
        furo = "3030", _("Bloblobber")
        furo_deco = "3031", _("Bloblobber Deco")
        explosher = "3040", _("Explosher")
        explosher_custom = "3041", _("Custom Explosher")
        splatspinner = "4000", _("Mini Splatling")
        splatspinner_collabo = "4001", _("Zink Mini Splatling")
        splatspinner_becchu = "4002", _("Kensa Mini Splatling")
        barrelspinner = "4010", _("Heavy Splatling")
        barrelspinner_deco = "4011", _("Heavy Splating Deco")
        barrelspinner_remix = "4012", _("Heavy Splatling Remix")
        herospinner_replica = "4015", _("Hero Splatling Replica")
        hydra = "4020", _("Hydra Splatling")
        hydra_custom = "4021", _("Custom Hydra Splatling")
        kugelschreiber = "4030", _("Ballpoint Splatling")
        kugelschreiber_hue = "4031", _("Ballpoint Splatling Nouveau")
        sputtery = "5000", _("Dapple Dualies")
        sputtery_hue = "5001", _("Daple Dualies Nouveau")
        sputtery_clear = "5002", _("Clear Dapple Dualies")
        maneuver = "5010", _("Splat Dualies")
        maneuver_collabo = "5011", _("Enperry Splat Dualies")
        maneuver_becchu = "5012", _("Kensa Splat Dualies")
        heromaneuiver_replica = "5015", _("Hero Dualie Replicas")
        kelvin525 = "5020", _("Glooga Dualies")
        kelvin525_deco = "5021", _("Glooga Dualies Deco")
        kelvin525_becchu = "5022", _("Kensa Glooga Dualies")
        dualsweeper = "5030", _("Dualie Squelchers")
        dualsweeper_custom = "5031", _("Custom Dualie Squelchers")
        quadhopper_black = "5040", _("Dark Tetra Dualies")
        quadhopper_white = "5041", _("Light Tetra Dualies")
        parashelter = "6000", _("Splat Brella")
        parashelter_sorella = "6001", _("Sorella Brella")
        heroshelter_replica = "6005", _("Hero Brella Replica")
        campingshelter = "6010", _("Tenta Brella")
        campingshelter_sorella = "6011", _("Tenta Sorella Brella")
        campingshelter_camo = "6012", _("Tenta Camo Brella")
        spygadget = "6020", _("Undercover Brella")
        spygadget_sorella = "6021", _("Undercover Sorella Brella")
        spygadget_becchu = "6022", _("Kensa Undercover Brella")

    class Stage(models.TextChoices):
        reef = "0", _("The Reef")
        musselforge = "1", _("Musselforge Fitness")
        mainstage = "2", _("Starfish Mainstage")
        sturgeon = "3", _("Sturgeon Shipyard")
        inkblot = "4", _("Inkblot Art Academy")
        humpback = "5", _("Humpback Pump Track")
        manta = "6", _("Manta Maria")
        moray = "8", _("Moray Towers")
        snapper = "9", _("Snapper Canal")
        dome = "10", _("Kelp Dome")
        blackbelly = "11", _("Blackbelly Skatepark")
        shellendorf = "12", _("Shellendorf Institute")
        mart = "13", _("MakoMart")
        walleye = "14", _("Walleye Warehouse")
        mall = "15", _("Arowana Mall")
        camp = "16", _("Camp Triggerfish")
        pit = "17", _("Piranha Pit")
        goby = "18", _("Goby Arena")
        albacore = "19", _("New Albacore Hotel")
        wahoo = "20", _("Wahoo World")
        anchov = "21", _("Ancho-V Games")
        skipper = "22", _("Skipper Pavillion")

    class MainAbilities(models.TextChoices):
        ink_saver_main = "0"
        ink_saver_sub = "1"
        ink_recovery_up = "2"
        run_speed_up = "3"
        swim_speed_up = "4"
        special_charge_up = "5"
        special_saver = "6"
        special_power_up = "7"
        quick_respawn = "8"
        quick_super_jump = "9"
        sub_power_up = "10"
        ink_resistance_up = "11"
        opening_gambit = "100"
        last_ditch_effort = "101"
        tenacity = "102"
        comeback = "103"
        ninja_squid = "104"
        haunt = "105"
        thermal_ink = "106"
        respawn_punisher = "107"
        ability_doubler = "108"
        stealth_jump = "109"
        object_shredder = "110"
        drop_roller = "111"
        bomb_defense_up_dx = "200"
        main_power_up = "201"

    class SubAbilities(models.TextChoices):
        ink_saver_main = "0"
        ink_saver_sub = "1"
        ink_recovery_up = "2"
        run_speed_up = "3"
        swim_speed_up = "4"
        special_charge_up = "5"
        special_saver = "6"
        special_power_up = "7"
        quick_respawn = "8"
        quick_super_jump = "9"
        sub_power_up = "10"
        ink_resistance_up = "11"
        bomb_defense_up_dx = "200"
        main_power_up = "201"
        question_mark = "255"

    # general match stats
    splatnet_json = models.JSONField("splatNet 2 JSON file", blank=True, null=True)
    stat_ink_json = models.JSONField("stat.ink JSON file", blank=True, null=True)
    rule = models.CharField(max_length=13, choices=Rule.choices)
    match_type = models.CharField(max_length=11, choices=Match_Type.choices)
    stage = models.CharField(max_length=2, choices=Stage.choices)
    win = models.BooleanField(null=True)
    has_disconnected_player = models.BooleanField(null=True)
    time = models.PositiveIntegerField(null=True)
    battle_number = models.CharField("SplatNet Battle Number", max_length=255)
    win_meter = models.IntegerField("Freshness", blank=True, null=True)
    my_team_count = models.DecimalField(decimal_places=1, max_digits=4, null=True)
    other_team_count = models.DecimalField(decimal_places=1, max_digits=4, null=True)
    elapsed_time = models.PositiveIntegerField(null=True)
    image_result = models.ImageField(null=True)
    image_gear = models.ImageField(null=True)

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

    # player
    # basic stats
    player_x_power = models.DecimalField(
        blank=True, null=True, decimal_places=1, max_digits=5
    )
    player_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    player_weapon = models.CharField(max_length=4, choices=Weapons.choices)
    player_rank = models.PositiveSmallIntegerField(null=True, choices=Ranks.choices)
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
    player_gender = models.CharField(max_length=4, null=True, choices=Gender.choices)
    player_species = models.CharField(max_length=9, null=True, choices=Species.choices)
    # headgear
    player_headgear = models.CharField(null=True, max_length=5)
    player_headgear_main = models.CharField(
        null=True, max_length=3, choices=MainAbilities.choices
    )
    player_headgear_sub0 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    player_headgear_sub1 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    player_headgear_sub2 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    # clothes
    player_clothes = models.CharField(null=True, max_length=5)
    player_clothes_main = models.CharField(
        null=True, max_length=3, choices=MainAbilities.choices
    )
    player_clothes_sub0 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    player_clothes_sub1 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    player_clothes_sub2 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    # shoes
    player_shoes = models.CharField(null=True, max_length=5)
    player_shoes_main = models.CharField(
        null=True, max_length=3, choices=MainAbilities.choices
    )
    player_shoes_sub0 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    player_shoes_sub1 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    player_shoes_sub2 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )

    # teammate 1
    # basic stats
    teammate1_splatnet_id = models.CharField(null=True, max_length=16)
    teammate1_name = models.CharField(null=True, max_length=10)
    teammate1_level_star = models.PositiveSmallIntegerField(null=True)
    teammate1_level = models.PositiveSmallIntegerField(null=True)
    teammate1_rank = models.PositiveSmallIntegerField(null=True, choices=Ranks.choices)
    teammate1_weapon = models.CharField(
        null=True, max_length=4, choices=Weapons.choices
    )
    teammate1_gender = models.CharField(max_length=4, null=True, choices=Gender.choices)
    teammate1_species = models.CharField(
        max_length=9, null=True, choices=Species.choices
    )
    teammate1_kills = models.PositiveSmallIntegerField(null=True)
    teammate1_deaths = models.PositiveSmallIntegerField(null=True)
    teammate1_assists = models.PositiveSmallIntegerField(null=True)
    teammate1_game_paint_point = models.PositiveSmallIntegerField(null=True)
    teammate1_specials = models.PositiveSmallIntegerField(null=True)
    # headgear
    teammate1_headgear = models.CharField(null=True, max_length=5)
    teammate1_headgear_main = models.CharField(
        null=True, max_length=3, choices=MainAbilities.choices
    )
    teammate1_headgear_sub0 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    teammate1_headgear_sub1 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    teammate1_headgear_sub2 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    # clothes
    teammate1_clothes = models.CharField(null=True, max_length=5)
    teammate1_clothes_main = models.CharField(
        null=True, max_length=3, choices=MainAbilities.choices
    )
    teammate1_clothes_sub0 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    teammate1_clothes_sub1 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    teammate1_clothes_sub2 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    # shoes
    teammate1_shoes = models.CharField(null=True, max_length=5)
    teammate1_shoes_main = models.CharField(
        null=True, max_length=3, choices=MainAbilities.choices
    )
    teammate1_shoes_sub0 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    teammate1_shoes_sub1 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    teammate1_shoes_sub2 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )

    # teammate 2
    # basic stats
    teammate2_splatnet_id = models.CharField(null=True, max_length=16)
    teammate2_name = models.CharField(null=True, max_length=10)
    teammate2_level_star = models.PositiveSmallIntegerField(null=True)
    teammate2_level = models.PositiveSmallIntegerField(null=True)
    teammate2_rank = models.PositiveSmallIntegerField(null=True, choices=Ranks.choices)
    teammate2_weapon = models.CharField(
        null=True, max_length=4, choices=Weapons.choices
    )
    teammate2_gender = models.CharField(max_length=4, null=True, choices=Gender.choices)
    teammate2_species = models.CharField(
        max_length=9, null=True, choices=Species.choices
    )
    teammate2_kills = models.PositiveSmallIntegerField(null=True)
    teammate2_deaths = models.PositiveSmallIntegerField(null=True)
    teammate2_assists = models.PositiveSmallIntegerField(null=True)
    teammate2_game_paint_point = models.PositiveSmallIntegerField(null=True)
    teammate2_specials = models.PositiveSmallIntegerField(null=True)
    # headgear
    teammate2_headgear = models.CharField(null=True, max_length=5)
    teammate2_headgear_main = models.CharField(
        null=True, max_length=3, choices=MainAbilities.choices
    )
    teammate2_headgear_sub0 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    teammate2_headgear_sub1 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    teammate2_headgear_sub2 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    # clothes
    teammate2_clothes = models.CharField(null=True, max_length=5)
    teammate2_clothes_main = models.CharField(
        null=True, max_length=3, choices=MainAbilities.choices
    )
    teammate2_clothes_sub0 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    teammate2_clothes_sub1 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    teammate2_clothes_sub2 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    # shoes
    teammate2_shoes = models.CharField(null=True, max_length=5)
    teammate2_shoes_main = models.CharField(
        null=True, max_length=3, choices=MainAbilities.choices
    )
    teammate2_shoes_sub0 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    teammate2_shoes_sub1 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    teammate2_shoes_sub2 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )

    # teammate 3
    # basic stats
    teammate3_splatnet_id = models.CharField(null=True, max_length=16)
    teammate3_name = models.CharField(null=True, max_length=10)
    teammate3_level_star = models.PositiveSmallIntegerField(null=True)
    teammate3_level = models.PositiveSmallIntegerField(null=True)
    teammate3_rank = models.PositiveSmallIntegerField(null=True, choices=Ranks.choices)
    teammate3_weapon = models.CharField(
        null=True, max_length=4, choices=Weapons.choices
    )
    teammate3_gender = models.CharField(max_length=4, null=True, choices=Gender.choices)
    teammate3_species = models.CharField(
        max_length=9, null=True, choices=Species.choices
    )
    teammate3_kills = models.PositiveSmallIntegerField(null=True)
    teammate3_deaths = models.PositiveSmallIntegerField(null=True)
    teammate3_assists = models.PositiveSmallIntegerField(null=True)
    teammate3_game_paint_point = models.PositiveSmallIntegerField(null=True)
    teammate3_specials = models.PositiveSmallIntegerField(null=True)
    # headgear
    teammate3_headgear = models.CharField(null=True, max_length=5)
    teammate3_headgear_main = models.CharField(
        null=True, max_length=3, choices=MainAbilities.choices
    )
    teammate3_headgear_sub0 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    teammate3_headgear_sub1 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    teammate3_headgear_sub2 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    # clothes
    teammate3_clothes = models.CharField(null=True, max_length=5)
    teammate3_clothes_main = models.CharField(
        null=True, max_length=3, choices=MainAbilities.choices
    )
    teammate3_clothes_sub0 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    teammate3_clothes_sub1 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    teammate3_clothes_sub2 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    # shoes
    teammate3_shoes = models.CharField(null=True, max_length=5)
    teammate3_shoes_main = models.CharField(
        null=True, max_length=3, choices=MainAbilities.choices
    )
    teammate3_shoes_sub0 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    teammate3_shoes_sub1 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    teammate3_shoes_sub2 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )

    # opponent 0
    # basic stats
    opponent0_splatnet_id = models.CharField(null=True, max_length=16)
    opponent0_name = models.CharField(null=True, max_length=10)
    opponent0_level_star = models.PositiveSmallIntegerField(null=True)
    opponent0_level = models.PositiveSmallIntegerField(null=True)
    opponent0_rank = models.PositiveSmallIntegerField(null=True, choices=Ranks.choices)
    opponent0_weapon = models.CharField(
        null=True, max_length=4, choices=Weapons.choices
    )
    opponent0_gender = models.CharField(max_length=4, null=True, choices=Gender.choices)
    opponent0_species = models.CharField(
        max_length=9, null=True, choices=Species.choices
    )
    opponent0_kills = models.PositiveSmallIntegerField(null=True)
    opponent0_deaths = models.PositiveSmallIntegerField(null=True)
    opponent0_assists = models.PositiveSmallIntegerField(null=True)
    opponent0_game_paint_point = models.PositiveSmallIntegerField(null=True)
    opponent0_specials = models.PositiveSmallIntegerField(null=True)
    # headgear
    opponent0_headgear = models.CharField(null=True, max_length=5)
    opponent0_headgear_main = models.CharField(
        null=True, max_length=3, choices=MainAbilities.choices
    )
    opponent0_headgear_sub0 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    opponent0_headgear_sub1 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    opponent0_headgear_sub2 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    # clothes
    opponent0_clothes = models.CharField(null=True, max_length=5)
    opponent0_clothes_main = models.CharField(
        null=True, max_length=3, choices=MainAbilities.choices
    )
    opponent0_clothes_sub0 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    opponent0_clothes_sub1 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    opponent0_clothes_sub2 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    # shoes
    opponent0_shoes = models.CharField(null=True, max_length=5)
    opponent0_shoes_main = models.CharField(
        null=True, max_length=3, choices=MainAbilities.choices
    )
    opponent0_shoes_sub0 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    opponent0_shoes_sub1 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    opponent0_shoes_sub2 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )

    # opponent 1
    # basic stats
    opponent1_splatnet_id = models.CharField(null=True, max_length=16)
    opponent1_name = models.CharField(null=True, max_length=10)
    opponent1_level_star = models.PositiveSmallIntegerField(null=True)
    opponent1_level = models.PositiveSmallIntegerField(null=True)
    opponent1_rank = models.PositiveSmallIntegerField(null=True, choices=Ranks.choices)
    opponent1_weapon = models.CharField(
        null=True, max_length=4, choices=Weapons.choices
    )
    opponent1_gender = models.CharField(max_length=4, null=True, choices=Gender.choices)
    opponent1_species = models.CharField(
        max_length=9, null=True, choices=Species.choices
    )
    opponent1_kills = models.PositiveSmallIntegerField(null=True)
    opponent1_deaths = models.PositiveSmallIntegerField(null=True)
    opponent1_assists = models.PositiveSmallIntegerField(null=True)
    opponent1_game_paint_point = models.PositiveSmallIntegerField(null=True)
    opponent1_specials = models.PositiveSmallIntegerField(null=True)
    # headgear
    opponent1_headgear = models.CharField(null=True, max_length=5)
    opponent1_headgear_main = models.CharField(
        null=True, max_length=3, choices=MainAbilities.choices
    )
    opponent1_headgear_sub0 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    opponent1_headgear_sub1 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    opponent1_headgear_sub2 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    # clothes
    opponent1_clothes = models.CharField(null=True, max_length=5)
    opponent1_clothes_main = models.CharField(
        null=True, max_length=3, choices=MainAbilities.choices
    )
    opponent1_clothes_sub0 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    opponent1_clothes_sub1 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    opponent1_clothes_sub2 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    # shoes
    opponent1_shoes = models.CharField(null=True, max_length=5)
    opponent1_shoes_main = models.CharField(
        null=True, max_length=3, choices=MainAbilities.choices
    )
    opponent1_shoes_sub0 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    opponent1_shoes_sub1 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    opponent1_shoes_sub2 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )

    # opponent 2
    # basic stats
    opponent2_splatnet_id = models.CharField(null=True, max_length=16)
    opponent2_name = models.CharField(null=True, max_length=10)
    opponent2_level_star = models.PositiveSmallIntegerField(null=True)
    opponent2_level = models.PositiveSmallIntegerField(null=True)
    opponent2_rank = models.PositiveSmallIntegerField(null=True, choices=Ranks.choices)
    opponent2_weapon = models.CharField(
        null=True, max_length=4, choices=Weapons.choices
    )
    opponent2_gender = models.CharField(max_length=4, null=True, choices=Gender.choices)
    opponent2_species = models.CharField(
        max_length=9, null=True, choices=Species.choices
    )
    opponent2_kills = models.PositiveSmallIntegerField(null=True)
    opponent2_deaths = models.PositiveSmallIntegerField(null=True)
    opponent2_assists = models.PositiveSmallIntegerField(null=True)
    opponent2_game_paint_point = models.PositiveSmallIntegerField(null=True)
    opponent2_specials = models.PositiveSmallIntegerField(null=True)
    # headgear
    opponent2_headgear = models.CharField(null=True, max_length=5)
    opponent2_headgear_main = models.CharField(
        null=True, max_length=3, choices=MainAbilities.choices
    )
    opponent2_headgear_sub0 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    opponent2_headgear_sub1 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    opponent2_headgear_sub2 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    # clothes
    opponent2_clothes = models.CharField(null=True, max_length=5)
    opponent2_clothes_main = models.CharField(
        null=True, max_length=3, choices=MainAbilities.choices
    )
    opponent2_clothes_sub0 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    opponent2_clothes_sub1 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    opponent2_clothes_sub2 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    # shoes
    opponent2_shoes = models.CharField(null=True, max_length=5)
    opponent2_shoes_main = models.CharField(
        null=True, max_length=3, choices=MainAbilities.choices
    )
    opponent2_shoes_sub0 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    opponent2_shoes_sub1 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    opponent2_shoes_sub2 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )

    # opponent 3
    # basic stats
    opponent3_splatnet_id = models.CharField(null=True, max_length=16)
    opponent3_name = models.CharField(null=True, max_length=10)
    opponent3_level_star = models.PositiveSmallIntegerField(null=True)
    opponent3_level = models.PositiveSmallIntegerField(null=True)
    opponent3_rank = models.PositiveSmallIntegerField(null=True, choices=Ranks.choices)
    opponent3_weapon = models.CharField(
        null=True, max_length=4, choices=Weapons.choices
    )
    opponent3_gender = models.CharField(max_length=4, null=True, choices=Gender.choices)
    opponent3_species = models.CharField(
        max_length=9, null=True, choices=Species.choices
    )
    opponent3_kills = models.PositiveSmallIntegerField(null=True)
    opponent3_deaths = models.PositiveSmallIntegerField(null=True)
    opponent3_assists = models.PositiveSmallIntegerField(null=True)
    opponent3_game_paint_point = models.PositiveSmallIntegerField(null=True)
    opponent3_specials = models.PositiveSmallIntegerField(null=True)
    # headgear
    opponent3_headgear = models.CharField(null=True, max_length=5)
    opponent3_headgear_main = models.CharField(
        null=True, max_length=3, choices=MainAbilities.choices
    )
    opponent3_headgear_sub0 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    opponent3_headgear_sub1 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    opponent3_headgear_sub2 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    # clothes
    opponent3_clothes = models.CharField(null=True, max_length=5)
    opponent3_clothes_main = models.CharField(
        null=True, max_length=3, choices=MainAbilities.choices
    )
    opponent3_clothes_sub0 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    opponent3_clothes_sub1 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    opponent3_clothes_sub2 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    # shoes
    opponent3_shoes = models.CharField(null=True, max_length=5)
    opponent3_shoes_main = models.CharField(
        null=True, max_length=3, choices=MainAbilities.choices
    )
    opponent3_shoes_sub0 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    opponent3_shoes_sub1 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    opponent3_shoes_sub2 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )

    @classmethod
    def create(cls, **kwargs):
        splatnet_json = None
        stat_ink_json = None
        player_user = kwargs["user"]
        if "splatnet_json" in kwargs:
            # general match stats
            splatnet_json = kwargs["splatnet_json"]
            rule = splatnet_json["rule"]["key"]
            match_type = splatnet_json["game_mode"]["key"]
            stage = splatnet_json["stage"]["id"]
            win = splatnet_json["my_team_result"]["key"] == "victory"
            has_disconnected_player = False
            if (
                "my_team_members" in splatnet_json
                and "other_team_members" in splatnet_json
            ):
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
            else:
                has_disconnected_player = None
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

            # league battle stuff
            if "tag_id" in splatnet_json:
                tag_id = splatnet_json["tag_id"]
            else:
                tag_id = None
            if "league_point" in splatnet_json:
                league_point = splatnet_json["league_point"]
            else:
                league_point = None

            # splatfest
            splatfest_point = None
            splatfest_title_after = None

            # player
            # basic stats
            player_splatnet_id = splatnet_json["player_result"]["player"][
                "principal_id"
            ]
            player_name = splatnet_json["player_result"]["player"]["nickname"]
            player_weapon = splatnet_json["player_result"]["player"]["weapon"]["id"]
            if "udemae" in splatnet_json:
                player_rank = splatnet_json["udemae"]["number"]
            else:
                player_rank = None
            player_splatfest_title = None
            player_level_star = splatnet_json["star_rank"]
            player_level = splatnet_json["player_rank"]
            player_kills = splatnet_json["player_result"]["kill_count"]
            player_deaths = splatnet_json["player_result"]["death_count"]
            player_assists = splatnet_json["player_result"]["assist_count"]
            player_specials = splatnet_json["player_result"]["special_count"]
            player_game_paint_point = splatnet_json["player_result"]["game_paint_point"]
            player_gender = splatnet_json["player_result"]["player"]["player_type"][
                "style"
            ]
            player_species = splatnet_json["player_result"]["player"]["player_type"][
                "species"
            ]
            if "x_power" in splatnet_json:
                player_x_power = splatnet_json["x_power"]
            else:
                player_x_power = None
            # headgear
            player_headgear = splatnet_json["player_result"]["player"]["head"]["id"]
            player_headgear_main = splatnet_json["player_result"]["player"][
                "head_skills"
            ]["main"]["id"]
            subs = splatnet_json["player_result"]["player"]["head_skills"]["subs"]
            if subs[0] is not None:
                player_headgear_sub0 = subs[0]["id"]
                if subs[1] is not None:
                    player_headgear_sub1 = subs[1]["id"]
                    if subs[2] is not None:
                        player_headgear_sub2 = subs[2]["id"]
                    else:
                        player_headgear_sub2 = None
                else:
                    player_headgear_sub1 = None
                    player_headgear_sub2 = None
            else:
                player_headgear_sub0 = None
                player_headgear_sub1 = None
                player_headgear_sub2 = None
            # clothes
            player_clothes = splatnet_json["player_result"]["player"]["clothes"]["id"]
            player_clothes_main = splatnet_json["player_result"]["player"][
                "clothes_skills"
            ]["main"]["id"]
            subs = splatnet_json["player_result"]["player"]["clothes_skills"]["subs"]
            if subs[0] is not None:
                player_clothes_sub0 = subs[0]["id"]
                if subs[1] is not None:
                    player_clothes_sub1 = subs[1]["id"]
                    if subs[2] is not None:
                        player_clothes_sub2 = subs[2]["id"]
                    else:
                        player_clothes_sub2 = None
                else:
                    player_clothes_sub1 = None
                    player_clothes_sub2 = None
            else:
                player_clothes_sub0 = None
                player_clothes_sub1 = None
                player_clothes_sub2 = None
            # shoes
            player_shoes = splatnet_json["player_result"]["player"]["shoes"]["id"]
            player_shoes_main = splatnet_json["player_result"]["player"][
                "shoes_skills"
            ]["main"]["id"]
            subs = splatnet_json["player_result"]["player"]["shoes_skills"]["subs"]
            if subs[0] is not None:
                player_shoes_sub0 = subs[0]["id"]
                if subs[1] is not None:
                    player_shoes_sub1 = subs[1]["id"]
                    if subs[2] is not None:
                        player_shoes_sub2 = subs[2]["id"]
                    else:
                        player_shoes_sub2 = None
                else:
                    player_shoes_sub1 = None
                    player_shoes_sub2 = None
            else:
                player_shoes_sub0 = None
                player_shoes_sub1 = None
                player_shoes_sub2 = None

            if "my_team_members" in splatnet_json:
                # teammate 1
                if len(splatnet_json["my_team_members"]) > 0:
                    # basic stats
                    player = splatnet_json["my_team_members"][0]
                    teammate1_splatnet_id = player["player"]["principal_id"]
                    teammate1_name = player["player"]["nickname"]
                    teammate1_level_star = player["player"]["star_rank"]
                    teammate1_level = player["player"]["player_rank"]
                    if "udemae" in player["player"]:
                        teammate1_rank = splatnet_json["udemae"]["number"]
                    else:
                        teammate1_rank = None
                    teammate1_weapon = player["player"]["weapon"]["id"]
                    teammate1_gender = player["player"]["player_type"]["style"]
                    teammate1_species = player["player"]["player_type"]["species"]
                    teammate1_kills = player["kill_count"]
                    teammate1_deaths = player["death_count"]
                    teammate1_assists = player["assist_count"]
                    teammate1_game_paint_point = player["game_paint_point"]
                    teammate1_specials = player["special_count"]
                    # headgear
                    teammate1_headgear = player["player"]["head"]["id"]
                    teammate1_headgear_main = player["player"]["head_skills"]["main"][
                        "id"
                    ]
                    subs = player["player"]["head_skills"]["subs"]
                    if subs[0] is not None:
                        teammate1_headgear_sub0 = subs[0]["id"]
                        if subs[1] is not None:
                            teammate1_headgear_sub1 = subs[1]["id"]
                            if subs[2] is not None:
                                teammate1_headgear_sub2 = subs[2]["id"]
                            else:
                                teammate1_headgear_sub2 = None
                        else:
                            teammate1_headgear_sub1 = None
                            teammate1_headgear_sub2 = None
                    else:
                        teammate1_headgear_sub0 = None
                        teammate1_headgear_sub1 = None
                        teammate1_headgear_sub2 = None
                    # clothes
                    teammate1_clothes = player["player"]["clothes"]["id"]
                    teammate1_clothes_main = player["player"]["clothes_skills"]["main"][
                        "id"
                    ]
                    subs = player["player"]["clothes_skills"]["subs"]
                    if subs[1] is not None:
                        teammate1_clothes_sub0 = subs[0]["id"]
                        if subs[1] is not None:
                            teammate1_clothes_sub1 = subs[1]["id"]
                            if subs[2] is not None:
                                teammate1_clothes_sub2 = subs[2]["id"]
                            else:
                                teammate1_clothes_sub2 = None
                        else:
                            teammate1_clothes_sub1 = None
                            teammate1_clothes_sub2 = None
                    else:
                        teammate1_clothes_sub0 = None
                        teammate1_clothes_sub1 = None
                        teammate1_clothes_sub2 = None
                    # shoes
                    teammate1_shoes = player["player"]["shoes"]["id"]
                    teammate1_shoes_main = player["player"]["shoes_skills"]["main"][
                        "id"
                    ]
                    subs = player["player"]["shoes_skills"]["subs"]
                    if subs[0] is not None:
                        teammate1_shoes_sub0 = subs[0]["id"]
                        if subs[1] is not None:
                            teammate1_shoes_sub1 = subs[1]["id"]
                            if subs[2] is not None:
                                teammate1_shoes_sub2 = subs[2]["id"]
                            else:
                                teammate1_shoes_sub2 = None
                        else:
                            teammate1_shoes_sub1 = None
                            teammate1_shoes_sub2 = None
                    else:
                        teammate1_shoes_sub0 = None
                        teammate1_shoes_sub1 = None
                        teammate1_shoes_sub2 = None
                else:
                    teammate1_splatnet_id = None
                    teammate1_name = None
                    teammate1_level_star = None
                    teammate1_level = None
                    teammate1_rank = None
                    teammate1_weapon = None
                    teammate1_gender = None
                    teammate1_species = None
                    teammate1_kills = None
                    teammate1_deaths = None
                    teammate1_assists = None
                    teammate1_game_paint_point = None
                    teammate1_specials = None
                    teammate1_headgear = None
                    teammate1_headgear_main = None
                    teammate1_headgear_sub0 = None
                    teammate1_headgear_sub1 = None
                    teammate1_headgear_sub2 = None
                    teammate1_clothes = None
                    teammate1_clothes_main = None
                    teammate1_clothes_sub0 = None
                    teammate1_clothes_sub1 = None
                    teammate1_clothes_sub2 = None
                    teammate1_shoes = None
                    teammate1_shoes_main = None
                    teammate1_shoes_sub0 = None
                    teammate1_shoes_sub1 = None
                    teammate1_shoes_sub2 = None

                # teammate 2
                if len(splatnet_json["my_team_members"]) > 1:
                    # basic stats
                    player = splatnet_json["my_team_members"][1]
                    teammate2_splatnet_id = player["player"]["principal_id"]
                    teammate2_name = player["player"]["nickname"]
                    teammate2_level_star = player["player"]["star_rank"]
                    teammate2_level = player["player"]["player_rank"]
                    if "udemae" in player["player"]:
                        teammate2_rank = splatnet_json["udemae"]["number"]
                    else:
                        teammate2_rank = None
                    teammate2_weapon = player["player"]["weapon"]["id"]
                    teammate2_gender = player["player"]["player_type"]["style"]
                    teammate2_species = player["player"]["player_type"]["species"]
                    teammate2_kills = player["kill_count"]
                    teammate2_deaths = player["death_count"]
                    teammate2_assists = player["assist_count"]
                    teammate2_game_paint_point = player["game_paint_point"]
                    teammate2_specials = player["special_count"]
                    # headgear
                    teammate2_headgear = player["player"]["head"]["id"]
                    teammate2_headgear_main = player["player"]["head_skills"]["main"][
                        "id"
                    ]
                    subs = player["player"]["head_skills"]["subs"]
                    if subs[0] is not None:
                        teammate2_headgear_sub0 = subs[0]["id"]
                        if subs[1] is not None:
                            teammate2_headgear_sub1 = subs[1]["id"]
                            if subs[2] is not None:
                                teammate2_headgear_sub2 = subs[2]["id"]
                            else:
                                teammate2_headgear_sub2 = None
                        else:
                            teammate2_headgear_sub1 = None
                            teammate2_headgear_sub2 = None
                    else:
                        teammate2_headgear_sub0 = None
                        teammate2_headgear_sub1 = None
                        teammate2_headgear_sub2 = None
                    # clothes
                    teammate2_clothes = player["player"]["clothes"]["id"]
                    teammate2_clothes_main = player["player"]["clothes_skills"]["main"][
                        "id"
                    ]
                    subs = player["player"]["clothes_skills"]["subs"]
                    if subs[0] is not None:
                        teammate2_clothes_sub0 = subs[0]["id"]
                        if subs[1] is not None:
                            teammate2_clothes_sub1 = subs[1]["id"]
                            if subs[2] is not None:
                                teammate2_clothes_sub2 = subs[2]["id"]
                            else:
                                teammate2_clothes_sub2 = None
                        else:
                            teammate2_clothes_sub1 = None
                            teammate2_clothes_sub2 = None
                    else:
                        teammate2_clothes_sub0 = None
                        teammate2_clothes_sub1 = None
                        teammate2_clothes_sub2 = None
                    # shoes
                    teammate2_shoes = player["player"]["shoes"]["id"]
                    teammate2_shoes_main = player["player"]["shoes_skills"]["main"][
                        "id"
                    ]
                    subs = player["player"]["shoes_skills"]["subs"]
                    if subs[0] is not None:
                        teammate2_shoes_sub0 = subs[0]["id"]
                        if subs[1] is not None:
                            teammate2_shoes_sub1 = subs[1]["id"]
                            if subs[2] is not None:
                                teammate2_shoes_sub2 = subs[2]["id"]
                            else:
                                teammate2_shoes_sub2 = None
                        else:
                            teammate2_shoes_sub1 = None
                            teammate2_shoes_sub2 = None
                    else:
                        teammate2_shoes_sub0 = None
                        teammate2_shoes_sub1 = None
                        teammate2_shoes_sub2 = None
                else:
                    teammate2_splatnet_id = None
                    teammate2_name = None
                    teammate2_level_star = None
                    teammate2_level = None
                    teammate2_rank = None
                    teammate2_weapon = None
                    teammate2_gender = None
                    teammate2_species = None
                    teammate2_kills = None
                    teammate2_deaths = None
                    teammate2_assists = None
                    teammate2_game_paint_point = None
                    teammate2_specials = None
                    teammate2_headgear = None
                    teammate2_headgear_main = None
                    teammate2_headgear_sub0 = None
                    teammate2_headgear_sub1 = None
                    teammate2_headgear_sub2 = None
                    teammate2_clothes = None
                    teammate2_clothes_main = None
                    teammate2_clothes_sub0 = None
                    teammate2_clothes_sub1 = None
                    teammate2_clothes_sub2 = None
                    teammate2_shoes = None
                    teammate2_shoes_main = None
                    teammate2_shoes_sub0 = None
                    teammate2_shoes_sub1 = None
                    teammate2_shoes_sub2 = None

                # teammate 3
                if len(splatnet_json["my_team_members"]) > 2:
                    # basic stats
                    player = splatnet_json["my_team_members"][2]
                    teammate3_splatnet_id = player["player"]["principal_id"]
                    teammate3_name = player["player"]["nickname"]
                    teammate3_level_star = player["player"]["star_rank"]
                    teammate3_level = player["player"]["player_rank"]
                    if "udemae" in player["player"]:
                        teammate3_rank = splatnet_json["udemae"]["number"]
                    else:
                        teammate3_rank = None
                    teammate3_weapon = player["player"]["weapon"]["id"]
                    teammate3_gender = player["player"]["player_type"]["style"]
                    teammate3_species = player["player"]["player_type"]["species"]
                    teammate3_kills = player["kill_count"]
                    teammate3_deaths = player["death_count"]
                    teammate3_assists = player["assist_count"]
                    teammate3_game_paint_point = player["game_paint_point"]
                    teammate3_specials = player["special_count"]
                    # headgear
                    teammate3_headgear = player["player"]["head"]["id"]
                    teammate3_headgear_main = player["player"]["head_skills"]["main"][
                        "id"
                    ]
                    subs = player["player"]["head_skills"]["subs"]
                    if subs[0] is not None:
                        teammate3_headgear_sub0 = subs[0]["id"]
                        if subs[1] is not None:
                            teammate3_headgear_sub1 = subs[1]["id"]
                            if subs[2] is not None:
                                teammate3_headgear_sub2 = subs[2]["id"]
                            else:
                                teammate3_headgear_sub2 = None
                        else:
                            teammate3_headgear_sub1 = None
                            teammate3_headgear_sub2 = None
                    else:
                        teammate3_headgear_sub0 = None
                        teammate3_headgear_sub1 = None
                        teammate3_headgear_sub2 = None
                    # clothes
                    teammate3_clothes = player["player"]["clothes"]["id"]
                    teammate3_clothes_main = player["player"]["clothes_skills"]["main"][
                        "id"
                    ]
                    subs = player["player"]["clothes_skills"]["subs"]
                    if subs[0] is not None:
                        teammate3_clothes_sub0 = subs[0]["id"]
                        if subs[1] is not None:
                            teammate3_clothes_sub1 = subs[1]["id"]
                            if subs[2] is not None:
                                teammate3_clothes_sub2 = subs[2]["id"]
                            else:
                                teammate3_clothes_sub2 = None
                        else:
                            teammate3_clothes_sub1 = None
                            teammate3_clothes_sub2 = None
                    else:
                        teammate3_clothes_sub0 = None
                        teammate3_clothes_sub1 = None
                        teammate3_clothes_sub2 = None
                    # shoes
                    teammate3_shoes = player["player"]["shoes"]["id"]
                    teammate3_shoes_main = player["player"]["shoes_skills"]["main"][
                        "id"
                    ]
                    subs = player["player"]["shoes_skills"]["subs"]
                    if subs[0] is not None:
                        teammate3_shoes_sub0 = subs[0]["id"]
                        if subs[1] is not None:
                            teammate3_shoes_sub1 = subs[1]["id"]
                            if subs[2] is not None:
                                teammate3_shoes_sub2 = subs[2]["id"]
                            else:
                                teammate3_shoes_sub2 = None
                        else:
                            teammate3_shoes_sub1 = None
                            teammate3_shoes_sub2 = None
                    else:
                        teammate3_shoes_sub0 = None
                        teammate3_shoes_sub1 = None
                        teammate3_shoes_sub2 = None
                else:
                    teammate3_splatnet_id = None
                    teammate3_name = None
                    teammate3_level_star = None
                    teammate3_level = None
                    teammate3_rank = None
                    teammate3_weapon = None
                    teammate3_gender = None
                    teammate3_species = None
                    teammate3_kills = None
                    teammate3_deaths = None
                    teammate3_assists = None
                    teammate3_game_paint_point = None
                    teammate3_specials = None
                    teammate3_headgear = None
                    teammate3_headgear_main = None
                    teammate3_headgear_sub0 = None
                    teammate3_headgear_sub1 = None
                    teammate3_headgear_sub2 = None
                    teammate3_clothes = None
                    teammate3_clothes_main = None
                    teammate3_clothes_sub0 = None
                    teammate3_clothes_sub1 = None
                    teammate3_clothes_sub2 = None
                    teammate3_shoes = None
                    teammate3_shoes_main = None
                    teammate3_shoes_sub0 = None
                    teammate3_shoes_sub1 = None
                    teammate3_shoes_sub2 = None
            else:
                teammate1_splatnet_id = None
                teammate1_name = None
                teammate1_level_star = None
                teammate1_level = None
                teammate1_rank = None
                teammate1_weapon = None
                teammate1_gender = None
                teammate1_species = None
                teammate1_kills = None
                teammate1_deaths = None
                teammate1_assists = None
                teammate1_game_paint_point = None
                teammate1_specials = None
                teammate1_headgear = None
                teammate1_headgear_main = None
                teammate1_headgear_sub0 = None
                teammate1_headgear_sub1 = None
                teammate1_headgear_sub2 = None
                teammate1_clothes = None
                teammate1_clothes_main = None
                teammate1_clothes_sub0 = None
                teammate1_clothes_sub1 = None
                teammate1_clothes_sub2 = None
                teammate1_shoes = None
                teammate1_shoes_main = None
                teammate1_shoes_sub0 = None
                teammate1_shoes_sub1 = None
                teammate1_shoes_sub2 = None
                teammate2_splatnet_id = None
                teammate2_name = None
                teammate2_level_star = None
                teammate2_level = None
                teammate2_rank = None
                teammate2_weapon = None
                teammate2_gender = None
                teammate2_species = None
                teammate2_kills = None
                teammate2_deaths = None
                teammate2_assists = None
                teammate2_game_paint_point = None
                teammate2_specials = None
                teammate2_headgear = None
                teammate2_headgear_main = None
                teammate2_headgear_sub0 = None
                teammate2_headgear_sub1 = None
                teammate2_headgear_sub2 = None
                teammate2_clothes = None
                teammate2_clothes_main = None
                teammate2_clothes_sub0 = None
                teammate2_clothes_sub1 = None
                teammate2_clothes_sub2 = None
                teammate2_shoes = None
                teammate2_shoes_main = None
                teammate2_shoes_sub0 = None
                teammate2_shoes_sub1 = None
                teammate2_shoes_sub2 = None
                teammate3_splatnet_id = None
                teammate3_name = None
                teammate3_level_star = None
                teammate3_level = None
                teammate3_rank = None
                teammate3_weapon = None
                teammate3_gender = None
                teammate3_species = None
                teammate3_kills = None
                teammate3_deaths = None
                teammate3_assists = None
                teammate3_game_paint_point = None
                teammate3_specials = None
                teammate3_headgear = None
                teammate3_headgear_main = None
                teammate3_headgear_sub0 = None
                teammate3_headgear_sub1 = None
                teammate3_headgear_sub2 = None
                teammate3_clothes = None
                teammate3_clothes_main = None
                teammate3_clothes_sub0 = None
                teammate3_clothes_sub1 = None
                teammate3_clothes_sub2 = None
                teammate3_shoes = None
                teammate3_shoes_main = None
                teammate3_shoes_sub0 = None
                teammate3_shoes_sub1 = None
                teammate3_shoes_sub2 = None

            if "other_team_members" in splatnet_json:
                # opponent 0
                if len(splatnet_json["other_team_members"]) > 0:
                    # basic stats
                    player = splatnet_json["other_team_members"][0]
                    opponent0_splatnet_id = player["player"]["principal_id"]
                    opponent0_name = player["player"]["nickname"]
                    opponent0_level_star = player["player"]["star_rank"]
                    opponent0_level = player["player"]["player_rank"]
                    if "udemae" in player["player"]:
                        opponent0_rank = splatnet_json["udemae"]["number"]
                    else:
                        opponent0_rank = None
                    opponent0_weapon = player["player"]["weapon"]["id"]
                    opponent0_gender = player["player"]["player_type"]["style"]
                    opponent0_species = player["player"]["player_type"]["species"]
                    opponent0_kills = player["kill_count"]
                    opponent0_deaths = player["death_count"]
                    opponent0_assists = player["assist_count"]
                    opponent0_game_paint_point = player["game_paint_point"]
                    opponent0_specials = player["special_count"]
                    # headgear
                    opponent0_headgear = player["player"]["head"]["id"]
                    opponent0_headgear_main = player["player"]["head_skills"]["main"][
                        "id"
                    ]
                    subs = player["player"]["head_skills"]["subs"]
                    if subs[0] is not None:
                        opponent0_headgear_sub0 = subs[0]["id"]
                        if subs[1] is not None:
                            opponent0_headgear_sub1 = subs[1]["id"]
                            if subs[2] is not None:
                                opponent0_headgear_sub2 = subs[2]["id"]
                            else:
                                opponent0_headgear_sub2 = None
                        else:
                            opponent0_headgear_sub1 = None
                            opponent0_headgear_sub2 = None
                    else:
                        opponent0_headgear_sub0 = None
                        opponent0_headgear_sub1 = None
                        opponent0_headgear_sub2 = None
                    # clothes
                    opponent0_clothes = player["player"]["clothes"]["id"]
                    opponent0_clothes_main = player["player"]["clothes_skills"]["main"][
                        "id"
                    ]
                    subs = player["player"]["clothes_skills"]["subs"]
                    if subs[0] is not None:
                        opponent0_clothes_sub0 = subs[0]["id"]
                        if subs[1] is not None:
                            opponent0_clothes_sub1 = subs[1]["id"]
                            if subs[2] is not None:
                                opponent0_clothes_sub2 = subs[2]["id"]
                            else:
                                opponent0_clothes_sub2 = None
                        else:
                            opponent0_clothes_sub1 = None
                            opponent0_clothes_sub2 = None
                    else:
                        opponent0_clothes_sub0 = None
                        opponent0_clothes_sub1 = None
                        opponent0_clothes_sub2 = None
                    # shoes
                    opponent0_shoes = player["player"]["shoes"]["id"]
                    opponent0_shoes_main = player["player"]["shoes_skills"]["main"][
                        "id"
                    ]
                    subs = player["player"]["shoes_skills"]["subs"]
                    if subs[0] is not None:
                        opponent0_shoes_sub0 = subs[0]["id"]
                        if subs[1] is not None:
                            opponent0_shoes_sub1 = subs[1]["id"]
                            if subs[2] is not None:
                                opponent0_shoes_sub2 = subs[2]["id"]
                            else:
                                opponent0_shoes_sub2 = None
                        else:
                            opponent0_shoes_sub1 = None
                            opponent0_shoes_sub2 = None
                    else:
                        opponent0_shoes_sub0 = None
                        opponent0_shoes_sub1 = None
                        opponent0_shoes_sub2 = None
                else:
                    opponent0_splatnet_id = None
                    opponent0_name = None
                    opponent0_level_star = None
                    opponent0_level = None
                    opponent0_rank = None
                    opponent0_weapon = None
                    opponent0_gender = None
                    opponent0_species = None
                    opponent0_kills = None
                    opponent0_deaths = None
                    opponent0_assists = None
                    opponent0_game_paint_point = None
                    opponent0_specials = None
                    opponent0_headgear = None
                    opponent0_headgear_main = None
                    opponent0_headgear_sub0 = None
                    opponent0_headgear_sub1 = None
                    opponent0_headgear_sub2 = None
                    opponent0_clothes = None
                    opponent0_clothes_main = None
                    opponent0_clothes_sub0 = None
                    opponent0_clothes_sub1 = None
                    opponent0_clothes_sub2 = None
                    opponent0_shoes = None
                    opponent0_shoes_main = None
                    opponent0_shoes_sub0 = None
                    opponent0_shoes_sub1 = None
                    opponent0_shoes_sub2 = None

                # opponent 1
                if len(splatnet_json["other_team_members"]) > 1:
                    # basic stats
                    player = splatnet_json["other_team_members"][1]
                    opponent1_splatnet_id = player["player"]["principal_id"]
                    opponent1_name = player["player"]["nickname"]
                    opponent1_level_star = player["player"]["star_rank"]
                    opponent1_level = player["player"]["player_rank"]
                    if "udemae" in player["player"]:
                        opponent1_rank = splatnet_json["udemae"]["number"]
                    else:
                        opponent1_rank = None
                    opponent1_weapon = player["player"]["weapon"]["id"]
                    opponent1_gender = player["player"]["player_type"]["style"]
                    opponent1_species = player["player"]["player_type"]["species"]
                    opponent1_kills = player["kill_count"]
                    opponent1_deaths = player["death_count"]
                    opponent1_assists = player["assist_count"]
                    opponent1_game_paint_point = player["game_paint_point"]
                    opponent1_specials = player["special_count"]
                    # headgear
                    opponent1_headgear = player["player"]["head"]["id"]
                    opponent1_headgear_main = player["player"]["head_skills"]["main"][
                        "id"
                    ]
                    subs = player["player"]["head_skills"]["subs"]
                    if subs[0] is not None:
                        opponent1_headgear_sub0 = subs[0]["id"]
                        if subs[1] is not None:
                            opponent1_headgear_sub1 = subs[1]["id"]
                            if subs[2] is not None:
                                opponent1_headgear_sub2 = subs[2]["id"]
                            else:
                                opponent1_headgear_sub2 = None
                        else:
                            opponent1_headgear_sub1 = None
                            opponent1_headgear_sub2 = None
                    else:
                        opponent1_headgear_sub0 = None
                        opponent1_headgear_sub1 = None
                        opponent1_headgear_sub2 = None
                    # clothes
                    opponent1_clothes = player["player"]["clothes"]["id"]
                    opponent1_clothes_main = player["player"]["clothes_skills"]["main"][
                        "id"
                    ]
                    subs = player["player"]["clothes_skills"]["subs"]
                    if subs[0] is not None:
                        opponent1_clothes_sub0 = subs[0]["id"]
                        if subs[1] is not None:
                            opponent1_clothes_sub1 = subs[1]["id"]
                            if subs[2] is not None:
                                opponent1_clothes_sub2 = subs[2]["id"]
                            else:
                                opponent1_clothes_sub2 = None
                        else:
                            opponent1_clothes_sub1 = None
                            opponent1_clothes_sub2 = None
                    else:
                        opponent1_clothes_sub0 = None
                        opponent1_clothes_sub1 = None
                        opponent1_clothes_sub2 = None
                    # shoes
                    opponent1_shoes = player["player"]["shoes"]["id"]
                    opponent1_shoes_main = player["player"]["shoes_skills"]["main"][
                        "id"
                    ]
                    subs = player["player"]["shoes_skills"]["subs"]
                    if subs[0] is not None:
                        opponent1_shoes_sub0 = subs[0]["id"]
                        if subs[1] is not None:
                            opponent1_shoes_sub1 = subs[1]["id"]
                            if subs[2] is not None:
                                opponent1_shoes_sub2 = subs[2]["id"]
                            else:
                                opponent1_shoes_sub2 = None
                        else:
                            opponent1_shoes_sub1 = None
                            opponent1_shoes_sub2 = None
                    else:
                        opponent1_shoes_sub0 = None
                        opponent1_shoes_sub1 = None
                        opponent1_shoes_sub2 = None
                else:
                    opponent1_splatnet_id = None
                    opponent1_name = None
                    opponent1_level_star = None
                    opponent1_level = None
                    opponent1_rank = None
                    opponent1_weapon = None
                    opponent1_gender = None
                    opponent1_species = None
                    opponent1_kills = None
                    opponent1_deaths = None
                    opponent1_assists = None
                    opponent1_game_paint_point = None
                    opponent1_specials = None
                    opponent1_headgear = None
                    opponent1_headgear_main = None
                    opponent1_headgear_sub0 = None
                    opponent1_headgear_sub1 = None
                    opponent1_headgear_sub2 = None
                    opponent1_clothes = None
                    opponent1_clothes_main = None
                    opponent1_clothes_sub0 = None
                    opponent1_clothes_sub1 = None
                    opponent1_clothes_sub2 = None
                    opponent1_shoes = None
                    opponent1_shoes_main = None
                    opponent1_shoes_sub0 = None
                    opponent1_shoes_sub1 = None
                    opponent1_shoes_sub2 = None

                # opponent 2
                if len(splatnet_json["other_team_members"]) > 2:
                    # basic stats
                    player = splatnet_json["other_team_members"][2]
                    opponent2_splatnet_id = player["player"]["principal_id"]
                    opponent2_name = player["player"]["nickname"]
                    opponent2_level_star = player["player"]["star_rank"]
                    opponent2_level = player["player"]["player_rank"]
                    if "udemae" in player["player"]:
                        opponent2_rank = splatnet_json["udemae"]["number"]
                    else:
                        opponent2_rank = None
                    opponent2_weapon = player["player"]["weapon"]["id"]
                    opponent2_gender = player["player"]["player_type"]["style"]
                    opponent2_species = player["player"]["player_type"]["species"]
                    opponent2_kills = player["kill_count"]
                    opponent2_deaths = player["death_count"]
                    opponent2_assists = player["assist_count"]
                    opponent2_game_paint_point = player["game_paint_point"]
                    opponent2_specials = player["special_count"]
                    # headgear
                    opponent2_headgear = player["player"]["head"]["id"]
                    opponent2_headgear_main = player["player"]["head_skills"]["main"][
                        "id"
                    ]
                    subs = player["player"]["head_skills"]["subs"]
                    if subs[0] is not None:
                        opponent2_headgear_sub0 = subs[0]["id"]
                        if subs[1] is not None:
                            opponent2_headgear_sub1 = subs[1]["id"]
                            if subs[2] is not None:
                                opponent2_headgear_sub2 = subs[2]["id"]
                            else:
                                opponent2_headgear_sub2 = None
                        else:
                            opponent2_headgear_sub1 = None
                            opponent2_headgear_sub2 = None
                    else:
                        opponent2_headgear_sub0 = None
                        opponent2_headgear_sub1 = None
                        opponent2_headgear_sub2 = None
                    # clothes
                    opponent2_clothes = player["player"]["clothes"]["id"]
                    opponent2_clothes_main = player["player"]["clothes_skills"]["main"][
                        "id"
                    ]
                    subs = player["player"]["clothes_skills"]["subs"]
                    if subs[0] is not None:
                        opponent2_clothes_sub0 = subs[0]["id"]
                        if subs[1] is not None:
                            opponent2_clothes_sub1 = subs[1]["id"]
                            if subs[2] is not None:
                                opponent2_clothes_sub2 = subs[2]["id"]
                            else:
                                opponent2_clothes_sub2 = None
                        else:
                            opponent2_clothes_sub1 = None
                            opponent2_clothes_sub2 = None
                    else:
                        opponent2_clothes_sub0 = None
                        opponent2_clothes_sub1 = None
                        opponent2_clothes_sub2 = None
                    # shoes
                    opponent2_shoes = player["player"]["shoes"]["id"]
                    opponent2_shoes_main = player["player"]["shoes_skills"]["main"][
                        "id"
                    ]
                    subs = player["player"]["shoes_skills"]["subs"]
                    if subs[0] is not None:
                        opponent2_shoes_sub0 = subs[0]["id"]
                        if subs[1] is not None:
                            opponent2_shoes_sub1 = subs[1]["id"]
                            if subs[2] is not None:
                                opponent2_shoes_sub2 = subs[2]["id"]
                            else:
                                opponent2_shoes_sub2 = None
                        else:
                            opponent2_shoes_sub1 = None
                            opponent2_shoes_sub2 = None
                    else:
                        opponent2_shoes_sub0 = None
                        opponent2_shoes_sub1 = None
                        opponent2_shoes_sub2 = None
                else:
                    opponent2_splatnet_id = None
                    opponent2_name = None
                    opponent2_level_star = None
                    opponent2_level = None
                    opponent2_rank = None
                    opponent2_weapon = None
                    opponent2_gender = None
                    opponent2_species = None
                    opponent2_kills = None
                    opponent2_deaths = None
                    opponent2_assists = None
                    opponent2_game_paint_point = None
                    opponent2_specials = None
                    opponent2_headgear = None
                    opponent2_headgear_main = None
                    opponent2_headgear_sub0 = None
                    opponent2_headgear_sub1 = None
                    opponent2_headgear_sub2 = None
                    opponent2_clothes = None
                    opponent2_clothes_main = None
                    opponent2_clothes_sub0 = None
                    opponent2_clothes_sub1 = None
                    opponent2_clothes_sub2 = None
                    opponent2_shoes = None
                    opponent2_shoes_main = None
                    opponent2_shoes_sub0 = None
                    opponent2_shoes_sub1 = None
                    opponent2_shoes_sub2 = None

                # opponent 3
                if len(splatnet_json["other_team_members"]) > 3:
                    # basic stats
                    player = splatnet_json["other_team_members"][3]
                    opponent3_splatnet_id = player["player"]["principal_id"]
                    opponent3_name = player["player"]["nickname"]
                    opponent3_level_star = player["player"]["star_rank"]
                    opponent3_level = player["player"]["player_rank"]
                    if "udemae" in player["player"]:
                        opponent3_rank = splatnet_json["udemae"]["number"]
                    else:
                        opponent3_rank = None
                    opponent3_weapon = player["player"]["weapon"]["id"]
                    opponent3_gender = player["player"]["player_type"]["style"]
                    opponent3_species = player["player"]["player_type"]["species"]
                    opponent3_kills = player["kill_count"]
                    opponent3_deaths = player["death_count"]
                    opponent3_assists = player["assist_count"]
                    opponent3_game_paint_point = player["game_paint_point"]
                    opponent3_specials = player["special_count"]
                    # headgear
                    opponent3_headgear = player["player"]["head"]["id"]
                    opponent3_headgear_main = player["player"]["head_skills"]["main"][
                        "id"
                    ]
                    subs = player["player"]["head_skills"]["subs"]
                    if len(subs) > 0:
                        opponent3_headgear_sub0 = subs[0]["id"]
                    else:
                        opponent3_headgear_sub0 = None
                    if len(subs) > 1 and subs[1] is not None:
                        opponent3_headgear_sub1 = subs[1]["id"]
                    else:
                        opponent3_headgear_sub1 = None
                    if len(subs) > 2 and subs[2] is not None:
                        opponent3_headgear_sub2 = subs[2]["id"]
                    else:
                        opponent3_headgear_sub2 = None
                    # clothes
                    opponent3_clothes = player["player"]["clothes"]["id"]
                    opponent3_clothes_main = player["player"]["clothes_skills"]["main"][
                        "id"
                    ]
                    subs = player["player"]["clothes_skills"]["subs"]
                    if len(subs) > 0:
                        opponent3_clothes_sub0 = subs[0]["id"]
                    else:
                        opponent3_clothes_sub0 = None
                    if len(subs) > 1:
                        opponent3_clothes_sub1 = subs[1]["id"]
                    else:
                        opponent3_clothes_sub1 = None
                    if len(subs) > 2 and subs[2] is not None:
                        opponent3_clothes_sub2 = subs[2]["id"]
                    else:
                        opponent3_clothes_sub2 = None
                    # shoes
                    opponent3_shoes = player["player"]["shoes"]["id"]
                    opponent3_shoes_main = player["player"]["shoes_skills"]["main"][
                        "id"
                    ]
                    subs = player["player"]["shoes_skills"]["subs"]
                    if subs[0] is not None:
                        opponent3_shoes_sub0 = subs[0]["id"]
                        if subs[1] is not None:
                            opponent3_shoes_sub1 = subs[1]["id"]
                            if subs[2] is not None:
                                opponent3_shoes_sub2 = subs[2]["id"]
                            else:
                                opponent3_shoes_sub2 = None
                        else:
                            opponent3_shoes_sub1 = None
                            opponent3_shoes_sub2 = None
                    else:
                        opponent3_shoes_sub0 = None
                        opponent3_shoes_sub1 = None
                        opponent3_shoes_sub2 = None
                else:
                    opponent3_splatnet_id = None
                    opponent3_name = None
                    opponent3_level_star = None
                    opponent3_level = None
                    opponent3_rank = None
                    opponent3_weapon = None
                    opponent3_gender = None
                    opponent3_species = None
                    opponent3_kills = None
                    opponent3_deaths = None
                    opponent3_assists = None
                    opponent3_game_paint_point = None
                    opponent3_specials = None
                    opponent3_headgear = None
                    opponent3_headgear_main = None
                    opponent3_headgear_sub0 = None
                    opponent3_headgear_sub1 = None
                    opponent3_headgear_sub2 = None
                    opponent3_clothes = None
                    opponent3_clothes_main = None
                    opponent3_clothes_sub0 = None
                    opponent3_clothes_sub1 = None
                    opponent3_clothes_sub2 = None
                    opponent3_shoes = None
                    opponent3_shoes_main = None
                    opponent3_shoes_sub0 = None
                    opponent3_shoes_sub1 = None
                    opponent3_shoes_sub2 = None
            else:
                opponent0_splatnet_id = None
                opponent0_name = None
                opponent0_level_star = None
                opponent0_level = None
                opponent0_rank = None
                opponent0_weapon = None
                opponent0_gender = None
                opponent0_species = None
                opponent0_kills = None
                opponent0_deaths = None
                opponent0_assists = None
                opponent0_game_paint_point = None
                opponent0_specials = None
                opponent0_headgear = None
                opponent0_headgear_main = None
                opponent0_headgear_sub0 = None
                opponent0_headgear_sub1 = None
                opponent0_headgear_sub2 = None
                opponent0_clothes = None
                opponent0_clothes_main = None
                opponent0_clothes_sub0 = None
                opponent0_clothes_sub1 = None
                opponent0_clothes_sub2 = None
                opponent0_shoes = None
                opponent0_shoes_main = None
                opponent0_shoes_sub0 = None
                opponent0_shoes_sub1 = None
                opponent0_shoes_sub2 = None
                opponent1_splatnet_id = None
                opponent1_name = None
                opponent1_level_star = None
                opponent1_level = None
                opponent1_rank = None
                opponent1_weapon = None
                opponent1_gender = None
                opponent1_species = None
                opponent1_kills = None
                opponent1_deaths = None
                opponent1_assists = None
                opponent1_game_paint_point = None
                opponent1_specials = None
                opponent1_headgear = None
                opponent1_headgear_main = None
                opponent1_headgear_sub0 = None
                opponent1_headgear_sub1 = None
                opponent1_headgear_sub2 = None
                opponent1_clothes = None
                opponent1_clothes_main = None
                opponent1_clothes_sub0 = None
                opponent1_clothes_sub1 = None
                opponent1_clothes_sub2 = None
                opponent1_shoes = None
                opponent1_shoes_main = None
                opponent1_shoes_sub0 = None
                opponent1_shoes_sub1 = None
                opponent1_shoes_sub2 = None
                opponent2_splatnet_id = None
                opponent2_name = None
                opponent2_level_star = None
                opponent2_level = None
                opponent2_rank = None
                opponent2_weapon = None
                opponent2_gender = None
                opponent2_species = None
                opponent2_kills = None
                opponent2_deaths = None
                opponent2_assists = None
                opponent2_game_paint_point = None
                opponent2_specials = None
                opponent2_headgear = None
                opponent2_headgear_main = None
                opponent2_headgear_sub0 = None
                opponent2_headgear_sub1 = None
                opponent2_headgear_sub2 = None
                opponent2_clothes = None
                opponent2_clothes_main = None
                opponent2_clothes_sub0 = None
                opponent2_clothes_sub1 = None
                opponent2_clothes_sub2 = None
                opponent2_shoes = None
                opponent2_shoes_main = None
                opponent2_shoes_sub0 = None
                opponent2_shoes_sub1 = None
                opponent2_shoes_sub2 = None
                opponent3_splatnet_id = None
                opponent3_name = None
                opponent3_level_star = None
                opponent3_level = None
                opponent3_rank = None
                opponent3_weapon = None
                opponent3_gender = None
                opponent3_species = None
                opponent3_kills = None
                opponent3_deaths = None
                opponent3_assists = None
                opponent3_game_paint_point = None
                opponent3_specials = None
                opponent3_headgear = None
                opponent3_headgear_main = None
                opponent3_headgear_sub0 = None
                opponent3_headgear_sub1 = None
                opponent3_headgear_sub2 = None
                opponent3_clothes = None
                opponent3_clothes_main = None
                opponent3_clothes_sub0 = None
                opponent3_clothes_sub1 = None
                opponent3_clothes_sub2 = None
                opponent3_shoes = None
                opponent3_shoes_main = None
                opponent3_shoes_sub0 = None
                opponent3_shoes_sub1 = None
                opponent3_shoes_sub2 = None

        if "stat_ink_json" in kwargs:
            stat_ink_json = kwargs["stat_ink_json"]

        if kwargs["image_result"] is not None:
            img_temp0 = NamedTemporaryFile()
            img_temp0.write(kwargs["image_result"])
            img_temp0.flush()

        if kwargs["image_gear"] is not None:
            img_temp1 = NamedTemporaryFile()
            img_temp1.write(kwargs["image_gear"])
            img_temp1.flush()

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
            player_splatnet_id=player_splatnet_id,
            player_name=player_name,
            player_level_star=player_level_star,
            elapsed_time=elapsed_time,
            player_user=player_user,
            player_gender=player_gender,
            player_species=player_species,
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
            teammate1_splatnet_id=teammate1_splatnet_id,
            teammate1_name=teammate1_name,
            teammate1_level_star=teammate1_level_star,
            teammate1_level=teammate1_level,
            teammate1_rank=teammate1_rank,
            teammate1_weapon=teammate1_weapon,
            teammate1_gender=teammate1_gender,
            teammate1_species=teammate1_species,
            teammate1_kills=teammate1_kills,
            teammate1_deaths=teammate1_deaths,
            teammate1_assists=teammate1_assists,
            teammate1_game_paint_point=teammate1_game_paint_point,
            teammate1_specials=teammate1_specials,
            teammate1_headgear=teammate1_headgear,
            teammate1_headgear_main=teammate1_headgear_main,
            teammate1_headgear_sub0=teammate1_headgear_sub0,
            teammate1_headgear_sub1=teammate1_headgear_sub1,
            teammate1_headgear_sub2=teammate1_headgear_sub2,
            teammate1_clothes=teammate1_clothes,
            teammate1_clothes_main=teammate1_clothes_main,
            teammate1_clothes_sub0=teammate1_clothes_sub0,
            teammate1_clothes_sub1=teammate1_clothes_sub1,
            teammate1_clothes_sub2=teammate1_clothes_sub2,
            teammate1_shoes=teammate1_shoes,
            teammate1_shoes_main=teammate1_shoes_main,
            teammate1_shoes_sub0=teammate1_shoes_sub0,
            teammate1_shoes_sub1=teammate1_shoes_sub1,
            teammate1_shoes_sub2=teammate1_shoes_sub2,
            teammate2_splatnet_id=teammate2_splatnet_id,
            teammate2_name=teammate2_name,
            teammate2_level_star=teammate2_level_star,
            teammate2_level=teammate2_level,
            teammate2_rank=teammate2_rank,
            teammate2_weapon=teammate2_weapon,
            teammate2_gender=teammate2_gender,
            teammate2_species=teammate2_species,
            teammate2_kills=teammate2_kills,
            teammate2_deaths=teammate2_deaths,
            teammate2_assists=teammate2_assists,
            teammate2_game_paint_point=teammate2_game_paint_point,
            teammate2_specials=teammate2_specials,
            teammate2_headgear=teammate2_headgear,
            teammate2_headgear_main=teammate2_headgear_main,
            teammate2_headgear_sub0=teammate2_headgear_sub0,
            teammate2_headgear_sub1=teammate2_headgear_sub1,
            teammate2_headgear_sub2=teammate2_headgear_sub2,
            teammate2_clothes=teammate2_clothes,
            teammate2_clothes_main=teammate2_clothes_main,
            teammate2_clothes_sub0=teammate2_clothes_sub0,
            teammate2_clothes_sub1=teammate2_clothes_sub1,
            teammate2_clothes_sub2=teammate2_clothes_sub2,
            teammate2_shoes=teammate2_shoes,
            teammate2_shoes_main=teammate2_shoes_main,
            teammate2_shoes_sub0=teammate2_shoes_sub0,
            teammate2_shoes_sub1=teammate2_shoes_sub1,
            teammate2_shoes_sub2=teammate2_shoes_sub2,
            teammate3_splatnet_id=teammate3_splatnet_id,
            teammate3_name=teammate3_name,
            teammate3_level_star=teammate3_level_star,
            teammate3_level=teammate3_level,
            teammate3_rank=teammate3_rank,
            teammate3_weapon=teammate3_weapon,
            teammate3_gender=teammate3_gender,
            teammate3_species=teammate3_species,
            teammate3_kills=teammate3_kills,
            teammate3_deaths=teammate3_deaths,
            teammate3_assists=teammate3_assists,
            teammate3_game_paint_point=teammate3_game_paint_point,
            teammate3_specials=teammate3_specials,
            teammate3_headgear=teammate3_headgear,
            teammate3_headgear_main=teammate3_headgear_main,
            teammate3_headgear_sub0=teammate3_headgear_sub0,
            teammate3_headgear_sub1=teammate3_headgear_sub1,
            teammate3_headgear_sub2=teammate3_headgear_sub2,
            teammate3_clothes=teammate3_clothes,
            teammate3_clothes_main=teammate3_clothes_main,
            teammate3_clothes_sub0=teammate3_clothes_sub0,
            teammate3_clothes_sub1=teammate3_clothes_sub1,
            teammate3_clothes_sub2=teammate3_clothes_sub2,
            teammate3_shoes=teammate3_shoes,
            teammate3_shoes_main=teammate3_shoes_main,
            teammate3_shoes_sub0=teammate3_shoes_sub0,
            teammate3_shoes_sub1=teammate3_shoes_sub1,
            teammate3_shoes_sub2=teammate3_shoes_sub2,
            opponent0_splatnet_id=opponent0_splatnet_id,
            opponent0_name=opponent0_name,
            opponent0_level_star=opponent0_level_star,
            opponent0_level=opponent0_level,
            opponent0_rank=opponent0_rank,
            opponent0_weapon=opponent0_weapon,
            opponent0_gender=opponent0_gender,
            opponent0_species=opponent0_species,
            opponent0_kills=opponent0_kills,
            opponent0_deaths=opponent0_deaths,
            opponent0_assists=opponent0_assists,
            opponent0_game_paint_point=opponent0_game_paint_point,
            opponent0_specials=opponent0_specials,
            opponent0_headgear=opponent0_headgear,
            opponent0_headgear_main=opponent0_headgear_main,
            opponent0_headgear_sub0=opponent0_headgear_sub0,
            opponent0_headgear_sub1=opponent0_headgear_sub1,
            opponent0_headgear_sub2=opponent0_headgear_sub2,
            opponent0_clothes=opponent0_clothes,
            opponent0_clothes_main=opponent0_clothes_main,
            opponent0_clothes_sub0=opponent0_clothes_sub0,
            opponent0_clothes_sub1=opponent0_clothes_sub1,
            opponent0_clothes_sub2=opponent0_clothes_sub2,
            opponent0_shoes=opponent0_shoes,
            opponent0_shoes_main=opponent0_shoes_main,
            opponent0_shoes_sub0=opponent0_shoes_sub0,
            opponent0_shoes_sub1=opponent0_shoes_sub1,
            opponent0_shoes_sub2=opponent0_shoes_sub2,
            opponent1_splatnet_id=opponent1_splatnet_id,
            opponent1_name=opponent1_name,
            opponent1_level_star=opponent1_level_star,
            opponent1_level=opponent1_level,
            opponent1_rank=opponent1_rank,
            opponent1_weapon=opponent1_weapon,
            opponent1_gender=opponent1_gender,
            opponent1_species=opponent1_species,
            opponent1_kills=opponent1_kills,
            opponent1_deaths=opponent1_deaths,
            opponent1_assists=opponent1_assists,
            opponent1_game_paint_point=opponent1_game_paint_point,
            opponent1_specials=opponent1_specials,
            opponent1_headgear=opponent1_headgear,
            opponent1_headgear_main=opponent1_headgear_main,
            opponent1_headgear_sub0=opponent1_headgear_sub0,
            opponent1_headgear_sub1=opponent1_headgear_sub1,
            opponent1_headgear_sub2=opponent1_headgear_sub2,
            opponent1_clothes=opponent1_clothes,
            opponent1_clothes_main=opponent1_clothes_main,
            opponent1_clothes_sub0=opponent1_clothes_sub0,
            opponent1_clothes_sub1=opponent1_clothes_sub1,
            opponent1_clothes_sub2=opponent1_clothes_sub2,
            opponent1_shoes=opponent1_shoes,
            opponent1_shoes_main=opponent1_shoes_main,
            opponent1_shoes_sub0=opponent1_shoes_sub0,
            opponent1_shoes_sub1=opponent1_shoes_sub1,
            opponent1_shoes_sub2=opponent1_shoes_sub2,
            opponent2_splatnet_id=opponent2_splatnet_id,
            opponent2_name=opponent2_name,
            opponent2_level_star=opponent2_level_star,
            opponent2_level=opponent2_level,
            opponent2_rank=opponent2_rank,
            opponent2_weapon=opponent2_weapon,
            opponent2_gender=opponent2_gender,
            opponent2_species=opponent2_species,
            opponent2_kills=opponent2_kills,
            opponent2_deaths=opponent2_deaths,
            opponent2_assists=opponent2_assists,
            opponent2_game_paint_point=opponent2_game_paint_point,
            opponent2_specials=opponent2_specials,
            opponent2_headgear=opponent2_headgear,
            opponent2_headgear_main=opponent2_headgear_main,
            opponent2_headgear_sub0=opponent2_headgear_sub0,
            opponent2_headgear_sub1=opponent2_headgear_sub1,
            opponent2_headgear_sub2=opponent2_headgear_sub2,
            opponent2_clothes=opponent2_clothes,
            opponent2_clothes_main=opponent2_clothes_main,
            opponent2_clothes_sub0=opponent2_clothes_sub0,
            opponent2_clothes_sub1=opponent2_clothes_sub1,
            opponent2_clothes_sub2=opponent2_clothes_sub2,
            opponent2_shoes=opponent2_shoes,
            opponent2_shoes_main=opponent2_shoes_main,
            opponent2_shoes_sub0=opponent2_shoes_sub0,
            opponent2_shoes_sub1=opponent2_shoes_sub1,
            opponent2_shoes_sub2=opponent2_shoes_sub2,
            opponent3_splatnet_id=opponent3_splatnet_id,
            opponent3_name=opponent3_name,
            opponent3_level_star=opponent3_level_star,
            opponent3_level=opponent3_level,
            opponent3_rank=opponent3_rank,
            opponent3_weapon=opponent3_weapon,
            opponent3_gender=opponent3_gender,
            opponent3_species=opponent3_species,
            opponent3_kills=opponent3_kills,
            opponent3_deaths=opponent3_deaths,
            opponent3_assists=opponent3_assists,
            opponent3_game_paint_point=opponent3_game_paint_point,
            opponent3_specials=opponent3_specials,
            opponent3_headgear=opponent3_headgear,
            opponent3_headgear_main=opponent3_headgear_main,
            opponent3_headgear_sub0=opponent3_headgear_sub0,
            opponent3_headgear_sub1=opponent3_headgear_sub1,
            opponent3_headgear_sub2=opponent3_headgear_sub2,
            opponent3_clothes=opponent3_clothes,
            opponent3_clothes_main=opponent3_clothes_main,
            opponent3_clothes_sub0=opponent3_clothes_sub0,
            opponent3_clothes_sub1=opponent3_clothes_sub1,
            opponent3_clothes_sub2=opponent3_clothes_sub2,
            opponent3_shoes=opponent3_shoes,
            opponent3_shoes_main=opponent3_shoes_main,
            opponent3_shoes_sub0=opponent3_shoes_sub0,
            opponent3_shoes_sub1=opponent3_shoes_sub1,
            opponent3_shoes_sub2=opponent3_shoes_sub2,
        )
        battle.save()
        if kwargs["image_result"] is not None:
            battle.image_result.save(
                "data/{}_image_result.png".format(battle.id), File(img_temp0), save=True
            )
        if kwargs["image_gear"] is not None:
            battle.image_gear.save(
                "data/{}_image_gear.png".format(battle.id), File(img_temp1), save=True
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
