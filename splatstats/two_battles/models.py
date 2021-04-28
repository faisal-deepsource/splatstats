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
        nautilus47 = "4040", _("Nautilus 47")
        nautilus79 = "4041", _("Nautilus 79")
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
    teammate0_splatnet_id = models.CharField(null=True, max_length=16)
    teammate0_name = models.CharField(null=True, max_length=10)
    teammate0_level_star = models.PositiveSmallIntegerField(null=True)
    teammate0_level = models.PositiveSmallIntegerField(null=True)
    teammate0_rank = models.PositiveSmallIntegerField(null=True, choices=Ranks.choices)
    teammate0_weapon = models.CharField(
        null=True, max_length=4, choices=Weapons.choices
    )
    teammate0_gender = models.CharField(max_length=4, null=True, choices=Gender.choices)
    teammate0_species = models.CharField(
        max_length=9, null=True, choices=Species.choices
    )
    teammate0_kills = models.PositiveSmallIntegerField(null=True)
    teammate0_deaths = models.PositiveSmallIntegerField(null=True)
    teammate0_assists = models.PositiveSmallIntegerField(null=True)
    teammate0_game_paint_point = models.PositiveSmallIntegerField(null=True)
    teammate0_specials = models.PositiveSmallIntegerField(null=True)
    # headgear
    teammate0_headgear = models.CharField(null=True, max_length=5)
    teammate0_headgear_main = models.CharField(
        null=True, max_length=3, choices=MainAbilities.choices
    )
    teammate0_headgear_sub0 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    teammate0_headgear_sub1 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    teammate0_headgear_sub2 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    # clothes
    teammate0_clothes = models.CharField(null=True, max_length=5)
    teammate0_clothes_main = models.CharField(
        null=True, max_length=3, choices=MainAbilities.choices
    )
    teammate0_clothes_sub0 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    teammate0_clothes_sub1 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    teammate0_clothes_sub2 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    # shoes
    teammate0_shoes = models.CharField(null=True, max_length=5)
    teammate0_shoes_main = models.CharField(
        null=True, max_length=3, choices=MainAbilities.choices
    )
    teammate0_shoes_sub0 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    teammate0_shoes_sub1 = models.CharField(
        null=True, max_length=3, choices=SubAbilities.choices
    )
    teammate0_shoes_sub2 = models.CharField(
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
        teammate_dict = {}
        opponent_dict = {}

        if "stat_ink_json" in kwargs:
            stat_ink_json = kwargs["stat_ink_json"]
            rules = {
                "area": "splat_zones",
                "hoko": "rainmaker",
                "asari": "clam_blitz",
                "yagura": "tower_control",
                "nawabari": "turf_War",
            }
            rule = rules.get(stat_ink_json["rule"]["key"], None)
            match_type = stat_ink_json["mode"]["key"]
            stage = str(stat_ink_json["map"]["splatnet"])
            win = stat_ink_json["result"] == "win"
            has_disconnected_player = False
            for player in stat_ink_json["players"]:
                has_disconnected_player = (
                    has_disconnected_player or player["point"] == 0
                )
            time = stat_ink_json["start_at"]["time"]
            battle_number = stat_ink_json["splatnet_number"]
            win_meter = stat_ink_json["freshness"]["freshness"]
            my_team_count = stat_ink_json["my_team_percent"]
            other_team_count = stat_ink_json["his_team_percent"]
            elapsed_time = (
                stat_ink_json["start_at"]["time"] - stat_ink_json["end_at"]["time"]
            )
            tag_id = stat_ink_json["my_team_id"]
            league_point = stat_ink_json["league_point"]
            splatfest_point = stat_ink_json["fest_power"]
            splatfest_title_after = stat_ink_json["fest_title_after"]

            player_x_power = stat_ink_json["x_power"]
            player_weapon = str(stat_ink_json["weapon"]["splatnet"])
            player_rank = stat_ink_json["rank"]
            player_level = stat_ink_json["level"]
            player_level_star = stat_ink_json["star_rank"]
            player_kills = stat_ink_json["kill"]
            player_deaths = stat_ink_json["death"]
            player_assists = stat_ink_json["kill_or_assist"] - player_kills
            player_specials = stat_ink_json["special"]
            player_game_paint_point = stat_ink_json["my_point"]
            player_splatfest_title = stat_ink_json["fest_title"]
            processed_players = []
            for player in stat_ink_json["players"]:
                if player["is_me"]:
                    processed_players.append(stat_ink_json["players"].index(player))
                    player_splatnet_id = player["splatnet_id"]
                    player_name = player["name"]
            player_gender = stat_ink_json["gender"]["key"]
            species = {
                "inkling": "inklings",
                "octoling": "octolings",
            }
            player_species = species.get(stat_ink_json["species"]["key"], None)
            player_headgear = str(
                stat_ink_json["gears"]["headgear"]["gear"]["splatnet"]
            )
            player_clothes = str(stat_ink_json["gears"]["clothing"]["gear"]["splatnet"])
            player_shoes = str(stat_ink_json["gears"]["shoes"]["gear"]["splatnet"])
            main_abilities = {
                "ink_saver_main": "0",
                "ink_saver_sub": "1",
                "ink_recovery_up": "2",
                "run_speed_up": "3",
                "swim_speed_up": "4",
                "special_charge_up": "5",
                "special_saver": "6",
                "special_power_up": "7",
                "quick_respawn": "8",
                "quick_super_jump": "9",
                "sub_power_up": "10",
                "ink_resistance_up": "11",
                "opening_gambit": "100",
                "last_ditch_effort": "101",
                "tenacity": "102",
                "comeback": "103",
                "ninja_squid": "104",
                "haunt": "105",
                "thermal_ink": "106",
                "respawn_punisher": "107",
                "ability_doubler": "108",
                "stealth_jump": "109",
                "object_shredder": "110",
                "drop_roller": "111",
                "bomb_defense_up_dx": "200",
                "main_power_up": "201",
            }
            player_headgear_main = main_abilities.get(
                stat_ink_json["gears"]["headgear"]["primary_ability"]["key"], None
            )
            player_clothes_main = main_abilities.get(
                stat_ink_json["gears"]["clothing"]["primary_ability"]["key"], None
            )
            player_shoes_main = main_abilities.get(
                stat_ink_json["gears"]["shoes"]["primary_ability"]["key"], None
            )
            sub_abilities = {
                "ink_saver_main": "0",
                "ink_saver_sub": "1",
                "ink_recovery_up": "2",
                "run_speed_up": "3",
                "swim_speed_up": "4",
                "special_charge_up": "5",
                "special_saver": "6",
                "special_power_up": "7",
                "quick_respawn": "8",
                "quick_super_jump": "9",
                "sub_power_up": "10",
                "ink_resistance_up": "11",
                "bomb_defense_up_dx": "200",
                "main_power_up": "201",
            }
            player_headgear_sub0 = sub_abilities.get(
                stat_ink_json["gears"]["headgear"]["secondary_abilities"][0]["key"],
                None,
            )
            player_headgear_sub1 = sub_abilities.get(
                stat_ink_json["gears"]["headgear"]["secondary_abilities"][1]["key"],
                None,
            )
            player_headgear_sub2 = sub_abilities.get(
                stat_ink_json["gears"]["headgear"]["secondary_abilities"][2]["key"],
                None,
            )
            player_clothes_sub0 = sub_abilities.get(
                stat_ink_json["gears"]["clothing"]["secondary_abilities"][0]["key"],
                None,
            )
            player_clothes_sub1 = sub_abilities.get(
                stat_ink_json["gears"]["clothing"]["secondary_abilities"][1]["key"],
                None,
            )
            player_clothes_sub2 = sub_abilities.get(
                stat_ink_json["gears"]["clothing"]["secondary_abilities"][2]["key"],
                None,
            )
            player_shoes_sub0 = sub_abilities.get(
                stat_ink_json["gears"]["shoes"]["secondary_abilities"][0]["key"],
                None,
            )
            player_shoes_sub1 = sub_abilities.get(
                stat_ink_json["gears"]["shoes"]["secondary_abilities"][1]["key"],
                None,
            )
            player_shoes_sub2 = sub_abilities.get(
                stat_ink_json["gears"]["shoes"]["secondary_abilities"][2]["key"],
                None,
            )
            players = stat_ink_json["players"]
            processed_fields = []
            # for player in players:
            #    if players.index(player) not in processed_players:

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
                for player in splatnet_json["my_team_members"]:
                    i = splatnet_json["my_team_members"].index(player) + 1
                    # basic stats
                    teammate_dict["teammate{}_splatnet_id".format(i)] = player[
                        "player"
                    ]["principal_id"]
                    teammate_dict["teammate{}_name".format(i)] = player["player"][
                        "nickname"
                    ]
                    teammate_dict["teammate{}_level_star".format(i)] = player["player"][
                        "star_rank"
                    ]
                    teammate_dict["teammate{}_level".format(i)] = player["player"][
                        "player_rank"
                    ]
                    if "udemae" in player["player"]:
                        teammate_dict["teammate{}_rank".format(i)] = splatnet_json[
                            "udemae"
                        ]["number"]
                    else:
                        teammate_dict["teammate{}_rank".format(i)] = None
                    teammate_dict["teammate{}__weapon".format(i)] = player["player"][
                        "weapon"
                    ]["id"]
                    teammate_dict["teammate{}__gender".format(i)] = player["player"][
                        "player_type"
                    ]["style"]
                    teammate_dict["teammate{}__species".format(i)] = player["player"][
                        "player_type"
                    ]["species"]
                    teammate_dict["teammate{}__kills".format(i)] = player["kill_count"]
                    teammate_dict["teammate{}__deaths".format(i)] = player[
                        "death_count"
                    ]
                    teammate_dict["teammate{}__assists".format(i)] = player[
                        "assist_count"
                    ]
                    teammate_dict["teammate{}__game_paint_point".format(i)] = player[
                        "game_paint_point"
                    ]
                    teammate_dict["teammate{}__specials".format(i)] = player[
                        "special_count"
                    ]
                    # headgear
                    teammate_dict["teammate{}__headgear".format(i)] = player["player"][
                        "head"
                    ]["id"]
                    teammate_dict["teammate{}__headgear_main".format(i)] = player[
                        "player"
                    ]["head_skills"]["main"]["id"]
                    subs = player["player"]["head_skills"]["subs"]
                    if subs[0] is not None:
                        teammate_dict["teammate{}__headgear_sub0".format(i)] = subs[0][
                            "id"
                        ]
                        if subs[1] is not None:
                            teammate_dict["teammate{}__headgear_sub1".format(i)] = subs[
                                1
                            ]["id"]
                            if subs[2] is not None:
                                teammate_dict[
                                    "teammate{}__headgear_sub2".format(i)
                                ] = subs[2]["id"]
                            else:
                                teammate_dict[
                                    "teammate{}__headgear_sub2".format(i)
                                ] = None
                        else:
                            teammate_dict["teammate{}__headgear_sub1".format(i)] = None
                            teammate_dict["teammate{}__headgear_sub2".format(i)] = None
                    else:
                        teammate_dict["teammate{}__headgear_sub0".format(i)] = None
                        teammate_dict["teammate{}__headgear_sub1".format(i)] = None
                        teammate_dict["teammate{}__headgear_sub2".format(i)] = None
                    # clothes
                    teammate_dict["teammate{}__clothes".format(i)] = player["player"][
                        "clothes"
                    ]["id"]
                    teammate_dict["teammate{}__clothes_main".format(i)] = player[
                        "player"
                    ]["clothes_skills"]["main"]["id"]
                    subs = player["player"]["clothes_skills"]["subs"]
                    if subs[1] is not None:
                        teammate_dict["teammate{}__clothes_sub0".format(i)] = subs[0][
                            "id"
                        ]
                        if subs[1] is not None:
                            teammate_dict["teammate{}__clothes_sub1".format(i)] = subs[
                                1
                            ]["id"]
                            if subs[2] is not None:
                                teammate_dict[
                                    "teammate{}__clothes_sub2".format(i)
                                ] = subs[2]["id"]
                            else:
                                teammate_dict[
                                    "teammate{}__clothes_sub2".format(i)
                                ] = None
                        else:
                            teammate_dict["teammate{}__clothes_sub1".format(i)] = None
                            teammate_dict["teammate{}__clothes_sub2".format(i)] = None
                    else:
                        teammate_dict["teammate{}__clothes_sub0".format(i)] = None
                        teammate_dict["teammate{}__clothes_sub1".format(i)] = None
                        teammate_dict["teammate{}__clothes_sub2".format(i)] = None
                    # shoes
                    teammate_dict["teammate{}__shoes".format(i)] = player["player"][
                        "shoes"
                    ]["id"]
                    teammate_dict["teammate{}__shoes_main".format(i)] = player[
                        "player"
                    ]["shoes_skills"]["main"]["id"]
                    subs = player["player"]["shoes_skills"]["subs"]
                    if subs[0] is not None:
                        teammate_dict["teammate{}__shoes_sub0".format(i)] = subs[0][
                            "id"
                        ]
                        if subs[1] is not None:
                            teammate_dict["teammate{}__shoes_sub1".format(i)] = subs[1][
                                "id"
                            ]
                            if subs[2] is not None:
                                teammate_dict[
                                    "teammate{}__shoes_sub2".format(i)
                                ] = subs[2]["id"]
                            else:
                                teammate_dict["teammate{}__shoes_sub2".format(i)] = None
                        else:
                            teammate_dict["teammate{}__shoes_sub1".format(i)] = None
                            teammate_dict["teammate{}__shoes_sub2".format(i)] = None
                    else:
                        teammate_dict["teammate{}__shoes_sub0".format(i)] = None
                        teammate_dict["teammate{}__shoes_sub1".format(i)] = None
                        teammate_dict["teammate{}__shoes_sub2".format(i)] = None
                while i < 3:
                    teammate_dict["teammate{}_splatnet_id".format(i)] = None
                    teammate_dict["teammate{}_name".format(i)] = None
                    teammate_dict["teammate{}_level_star".format(i)] = None
                    teammate_dict["teammate{}_level".format(i)] = None
                    teammate_dict["teammate{}_rank".format(i)] = None
                    teammate_dict["teammate{}_weapon".format(i)] = None
                    teammate_dict["teammate{}_gender".format(i)] = None
                    teammate_dict["teammate{}_species".format(i)] = None
                    teammate_dict["teammate{}_kills".format(i)] = None
                    teammate_dict["teammate{}_deaths".format(i)] = None
                    teammate_dict["teammate{}_assists".format(i)] = None
                    teammate_dict["teammate{}_game_paint_point".format(i)] = None
                    teammate_dict["teammate{}_specials".format(i)] = None
                    teammate_dict["teammate{}_headgear".format(i)] = None
                    teammate_dict["teammate{}_headgear_main".format(i)] = None
                    teammate_dict["teammate{}_headgear_sub0".format(i)] = None
                    teammate_dict["teammate{}_headgear_sub1".format(i)] = None
                    teammate_dict["teammate{}_headgear_sub2".format(i)] = None
                    teammate_dict["teammate{}_clothes".format(i)] = None
                    teammate_dict["teammate{}_clothes_main".format(i)] = None
                    teammate_dict["teammate{}_clothes_sub0".format(i)] = None
                    teammate_dict["teammate{}_clothes_sub1".format(i)] = None
                    teammate_dict["teammate{}_clothes_sub2".format(i)] = None
                    teammate_dict["teammate{}_shoes".format(i)] = None
                    teammate_dict["teammate{}_shoes_main".format(i)] = None
                    teammate_dict["teammate{}_shoes_sub0".format(i)] = None
                    teammate_dict["teammate{}_shoes_sub1".format(i)] = None
                    teammate_dict["teammate{}_shoes_sub2".format(i)] = None
                    i += 1
            else:
                teammate_dict["teammate0_splatnet_id"] = None
                teammate_dict["teammate0_name"] = None
                teammate_dict["teammate0_level_star"] = None
                teammate_dict["teammate0_level"] = None
                teammate_dict["teammate0_rank"] = None
                teammate_dict["teammate0_weapon"] = None
                teammate_dict["teammate0_gender"] = None
                teammate_dict["teammate0_species"] = None
                teammate_dict["teammate0_kills"] = None
                teammate_dict["teammate0_deaths"] = None
                teammate_dict["teammate0_assists"] = None
                teammate_dict["teammate0_game_paint_point"] = None
                teammate_dict["teammate0_specials"] = None
                teammate_dict["teammate0_headgear"] = None
                teammate_dict["teammate0_headgear_main"] = None
                teammate_dict["teammate0_headgear_sub0"] = None
                teammate_dict["teammate0_headgear_sub1"] = None
                teammate_dict["teammate0_headgear_sub2"] = None
                teammate_dict["teammate0_clothes"] = None
                teammate_dict["teammate0_clothes_main"] = None
                teammate_dict["teammate0_clothes_sub0"] = None
                teammate_dict["teammate0_clothes_sub1"] = None
                teammate_dict["teammate0_clothes_sub2"] = None
                teammate_dict["teammate0_shoes"] = None
                teammate_dict["teammate0_shoes_main"] = None
                teammate_dict["teammate0_shoes_sub0"] = None
                teammate_dict["teammate0_shoes_sub1"] = None
                teammate_dict["teammate0_shoes_sub2"] = None
                teammate_dict["teammate1_splatnet_id"] = None
                teammate_dict["teammate1_name"] = None
                teammate_dict["teammate1_level_star"] = None
                teammate_dict["teammate1_level"] = None
                teammate_dict["teammate1_rank"] = None
                teammate_dict["teammate1_weapon"] = None
                teammate_dict["teammate1_gender"] = None
                teammate_dict["teammate1_species"] = None
                teammate_dict["teammate1_kills"] = None
                teammate_dict["teammate1_deaths"] = None
                teammate_dict["teammate1_assists"] = None
                teammate_dict["teammate1_game_paint_point"] = None
                teammate_dict["teammate1_specials"] = None
                teammate_dict["teammate1_headgear"] = None
                teammate_dict["teammate1_headgear_main"] = None
                teammate_dict["teammate1_headgear_sub0"] = None
                teammate_dict["teammate1_headgear_sub1"] = None
                teammate_dict["teammate1_headgear_sub2"] = None
                teammate_dict["teammate1_clothes"] = None
                teammate_dict["teammate1_clothes_main"] = None
                teammate_dict["teammate1_clothes_sub0"] = None
                teammate_dict["teammate1_clothes_sub1"] = None
                teammate_dict["teammate1_clothes_sub2"] = None
                teammate_dict["teammate1_shoes"] = None
                teammate_dict["teammate1_shoes_main"] = None
                teammate_dict["teammate1_shoes_sub0"] = None
                teammate_dict["teammate1_shoes_sub1"] = None
                teammate_dict["teammate1_shoes_sub2"] = None
                teammate_dict["teammate2_splatnet_id"] = None
                teammate_dict["teammate2_name"] = None
                teammate_dict["teammate2_level_star"] = None
                teammate_dict["teammate2_level"] = None
                teammate_dict["teammate2_rank"] = None
                teammate_dict["teammate2_weapon"] = None
                teammate_dict["teammate2_gender"] = None
                teammate_dict["teammate2_species"] = None
                teammate_dict["teammate2_kills"] = None
                teammate_dict["teammate2_deaths"] = None
                teammate_dict["teammate2_assists"] = None
                teammate_dict["teammate2_game_paint_point"] = None
                teammate_dict["teammate2_specials"] = None
                teammate_dict["teammate2_headgear"] = None
                teammate_dict["teammate2_headgear_main"] = None
                teammate_dict["teammate2_headgear_sub0"] = None
                teammate_dict["teammate2_headgear_sub1"] = None
                teammate_dict["teammate2_headgear_sub2"] = None
                teammate_dict["teammate2_clothes"] = None
                teammate_dict["teammate2_clothes_main"] = None
                teammate_dict["teammate2_clothes_sub0"] = None
                teammate_dict["teammate2_clothes_sub1"] = None
                teammate_dict["teammate2_clothes_sub2"] = None
                teammate_dict["teammate2_shoes"] = None
                teammate_dict["teammate2_shoes_main"] = None
                teammate_dict["teammate2_shoes_sub0"] = None
                teammate_dict["teammate2_shoes_sub1"] = None
                teammate_dict["teammate2_shoes_sub2"] = None

            if "other_team_members" in splatnet_json:
                for player in splatnet_json["other_team_members"]:
                    i = splatnet_json["other_team_members"].index(player) + 1
                    # basic stats
                    opponent_dict["opponent{}__splatnet_id".format(i)] = player[
                        "player"
                    ]["principal_id"]
                    opponent_dict["opponent{}__name".format(i)] = player["player"][
                        "nickname"
                    ]
                    opponent_dict["opponent{}__level_star".format(i)] = player[
                        "player"
                    ]["star_rank"]
                    opponent_dict["opponent{}__level".format(i)] = player["player"][
                        "player_rank"
                    ]
                    if "udemae" in player["player"]:
                        opponent_dict["opponent{}__rank".format(i)] = splatnet_json[
                            "udemae"
                        ]["number"]
                    else:
                        opponent_dict["opponent{}__rank".format(i)] = None
                    opponent_dict["opponent{}__weapon".format(i)] = player["player"][
                        "weapon"
                    ]["id"]
                    opponent_dict["opponent{}__gender".format(i)] = player["player"][
                        "player_type"
                    ]["style"]
                    opponent_dict["opponent{}__species".format(i)] = player["player"][
                        "player_type"
                    ]["species"]
                    opponent_dict["opponent{}__kills".format(i)] = player["kill_count"]
                    opponent_dict["opponent{}__deaths".format(i)] = player[
                        "death_count"
                    ]
                    opponent_dict["opponent{}__assists".format(i)] = player[
                        "assist_count"
                    ]
                    opponent_dict["opponent{}__game_paint_point".format(i)] = player[
                        "game_paint_point"
                    ]
                    opponent_dict["opponent{}__specials".format(i)] = player[
                        "special_count"
                    ]
                    # headgear
                    opponent_dict["opponent{}__headgear".format(i)] = player["player"][
                        "head"
                    ]["id"]
                    opponent_dict["opponent{}__headgear_main".format(i)] = player[
                        "player"
                    ]["head_skills"]["main"]["id"]
                    subs = player["player"]["head_skills"]["subs"]
                    if subs[0] is not None:
                        opponent_dict["opponent{}__headgear_sub0".format(i)] = subs[0][
                            "id"
                        ]
                        if subs[1] is not None:
                            opponent_dict["opponent{}__headgear_sub1".format(i)] = subs[
                                1
                            ]["id"]
                            if subs[2] is not None:
                                opponent_dict[
                                    "opponent{}__headgear_sub2".format(i)
                                ] = subs[2]["id"]
                            else:
                                opponent_dict[
                                    "opponent{}__headgear_sub2".format(i)
                                ] = None
                        else:
                            opponent_dict["opponent{}__headgear_sub1".format(i)] = None
                            opponent_dict["opponent{}__headgear_sub2".format(i)] = None
                    else:
                        opponent_dict["opponent{}__headgear_sub0".format(i)] = None
                        opponent_dict["opponent{}__headgear_sub1".format(i)] = None
                        opponent_dict["opponent{}__headgear_sub2".format(i)] = None
                    # clothes
                    opponent_dict["opponent{}__clothes".format(i)] = player["player"][
                        "clothes"
                    ]["id"]
                    opponent_dict["opponent{}__clothes_main".format(i)] = player[
                        "player"
                    ]["clothes_skills"]["main"]["id"]
                    subs = player["player"]["clothes_skills"]["subs"]
                    if subs[0] is not None:
                        opponent_dict["opponent{}__clothes_sub0".format(i)] = subs[0][
                            "id"
                        ]
                        if subs[1] is not None:
                            opponent_dict["opponent{}__clothes_sub1".format(i)] = subs[
                                1
                            ]["id"]
                            if subs[2] is not None:
                                opponent_dict[
                                    "opponent{}__clothes_sub2".format(i)
                                ] = subs[2]["id"]
                            else:
                                opponent_dict[
                                    "opponent{}__clothes_sub2".format(i)
                                ] = None
                        else:
                            opponent_dict["opponent{}__clothes_sub1".format(i)] = None
                            opponent_dict["opponent{}__clothes_sub2".format(i)] = None
                    else:
                        opponent_dict["opponent{}__clothes_sub0".format(i)] = None
                        opponent_dict["opponent{}__clothes_sub1".format(i)] = None
                        opponent_dict["opponent{}__clothes_sub2".format(i)] = None
                    # shoes
                    opponent_dict["opponent{}__shoes".format(i)] = player["player"][
                        "shoes"
                    ]["id"]
                    opponent_dict["opponent{}__shoes_main".format(i)] = player[
                        "player"
                    ]["shoes_skills"]["main"]["id"]
                    subs = player["player"]["shoes_skills"]["subs"]
                    if subs[0] is not None:
                        opponent_dict["opponent{}__shoes_sub0".format(i)] = subs[0][
                            "id"
                        ]
                        if subs[1] is not None:
                            opponent_dict["opponent{}__shoes_sub1".format(i)] = subs[1][
                                "id"
                            ]
                            if subs[2] is not None:
                                opponent_dict[
                                    "opponent{}__shoes_sub2".format(i)
                                ] = subs[2]["id"]
                            else:
                                opponent_dict["opponent{}__shoes_sub2".format(i)] = None
                        else:
                            opponent_dict["opponent{}__shoes_sub1".format(i)] = None
                            opponent_dict["opponent{}__shoes_sub2".format(i)] = None
                    else:
                        opponent_dict["opponent{}__shoes_sub0".format(i)] = None
                        opponent_dict["opponent{}__shoes_sub1".format(i)] = None
                        opponent_dict["opponent{}__shoes_sub2".format(i)] = None
                while i < 4:
                    opponent_dict["opponent{}__splatnet_id".format(i)] = None
                    opponent_dict["opponent{}__name".format(i)] = None
                    opponent_dict["opponent{}__level_star".format(i)] = None
                    opponent_dict["opponent{}__level".format(i)] = None
                    opponent_dict["opponent{}__rank".format(i)] = None
                    opponent_dict["opponent{}__weapon".format(i)] = None
                    opponent_dict["opponent{}__gender".format(i)] = None
                    opponent_dict["opponent{}__species".format(i)] = None
                    opponent_dict["opponent{}__kills".format(i)] = None
                    opponent_dict["opponent{}__deaths".format(i)] = None
                    opponent_dict["opponent{}__assists".format(i)] = None
                    opponent_dict["opponent{}__game_paint_point".format(i)] = None
                    opponent_dict["opponent{}__specials".format(i)] = None
                    opponent_dict["opponent{}__headgear".format(i)] = None
                    opponent_dict["opponent{}__headgear_main".format(i)] = None
                    opponent_dict["opponent{}__headgear_sub0".format(i)] = None
                    opponent_dict["opponent{}__headgear_sub1".format(i)] = None
                    opponent_dict["opponent{}__headgear_sub2".format(i)] = None
                    opponent_dict["opponent{}__clothes".format(i)] = None
                    opponent_dict["opponent{}__clothes_main".format(i)] = None
                    opponent_dict["opponent{}__clothes_sub0".format(i)] = None
                    opponent_dict["opponent{}__clothes_sub1".format(i)] = None
                    opponent_dict["opponent{}__clothes_sub2".format(i)] = None
                    opponent_dict["opponent{}__shoes".format(i)] = None
                    opponent_dict["opponent{}__shoes_main".format(i)] = None
                    opponent_dict["opponent{}__shoes_sub0".format(i)] = None
                    opponent_dict["opponent{}__shoes_sub1".format(i)] = None
                    opponent_dict["opponent{}__shoes_sub2".format(i)] = None
                    i += 1
            else:
                opponent_dict["opponent0_splatnet_id"] = None
                opponent_dict["opponent0_name"] = None
                opponent_dict["opponent0_level_star"] = None
                opponent_dict["opponent0_level"] = None
                opponent_dict["opponent0_rank"] = None
                opponent_dict["opponent0_weapon"] = None
                opponent_dict["opponent0_gender"] = None
                opponent_dict["opponent0_species"] = None
                opponent_dict["opponent0_kills"] = None
                opponent_dict["opponent0_deaths"] = None
                opponent_dict["opponent0_assists"] = None
                opponent_dict["opponent0_game_paint_point"] = None
                opponent_dict["opponent0_specials"] = None
                opponent_dict["opponent0_headgear"] = None
                opponent_dict["opponent0_headgear_main"] = None
                opponent_dict["opponent0_headgear_sub0"] = None
                opponent_dict["opponent0_headgear_sub1"] = None
                opponent_dict["opponent0_headgear_sub2"] = None
                opponent_dict["opponent0_clothes"] = None
                opponent_dict["opponent0_clothes_main"] = None
                opponent_dict["opponent0_clothes_sub0"] = None
                opponent_dict["opponent0_clothes_sub1"] = None
                opponent_dict["opponent0_clothes_sub2"] = None
                opponent_dict["opponent0_shoes"] = None
                opponent_dict["opponent0_shoes_main"] = None
                opponent_dict["opponent0_shoes_sub0"] = None
                opponent_dict["opponent0_shoes_sub1"] = None
                opponent_dict["opponent0_shoes_sub2"] = None
                opponent_dict["opponent1_splatnet_id"] = None
                opponent_dict["opponent1_name"] = None
                opponent_dict["opponent1_level_star"] = None
                opponent_dict["opponent1_level"] = None
                opponent_dict["opponent1_rank"] = None
                opponent_dict["opponent1_weapon"] = None
                opponent_dict["opponent1_gender"] = None
                opponent_dict["opponent1_species"] = None
                opponent_dict["opponent1_kills"] = None
                opponent_dict["opponent1_deaths"] = None
                opponent_dict["opponent1_assists"] = None
                opponent_dict["opponent1_game_paint_point"] = None
                opponent_dict["opponent1_specials"] = None
                opponent_dict["opponent1_headgear"] = None
                opponent_dict["opponent1_headgear_main"] = None
                opponent_dict["opponent1_headgear_sub0"] = None
                opponent_dict["opponent1_headgear_sub1"] = None
                opponent_dict["opponent1_headgear_sub2"] = None
                opponent_dict["opponent1_clothes"] = None
                opponent_dict["opponent1_clothes_main"] = None
                opponent_dict["opponent1_clothes_sub0"] = None
                opponent_dict["opponent1_clothes_sub1"] = None
                opponent_dict["opponent1_clothes_sub2"] = None
                opponent_dict["opponent1_shoes"] = None
                opponent_dict["opponent1_shoes_main"] = None
                opponent_dict["opponent1_shoes_sub0"] = None
                opponent_dict["opponent1_shoes_sub1"] = None
                opponent_dict["opponent1_shoes_sub2"] = None
                opponent_dict["opponent2_splatnet_id"] = None
                opponent_dict["opponent2_name"] = None
                opponent_dict["opponent2_level_star"] = None
                opponent_dict["opponent2_level"] = None
                opponent_dict["opponent2_rank"] = None
                opponent_dict["opponent2_weapon"] = None
                opponent_dict["opponent2_gender"] = None
                opponent_dict["opponent2_species"] = None
                opponent_dict["opponent2_kills"] = None
                opponent_dict["opponent2_deaths"] = None
                opponent_dict["opponent2_assists"] = None
                opponent_dict["opponent2_game_paint_point"] = None
                opponent_dict["opponent2_specials"] = None
                opponent_dict["opponent2_headgear"] = None
                opponent_dict["opponent2_headgear_main"] = None
                opponent_dict["opponent2_headgear_sub0"] = None
                opponent_dict["opponent2_headgear_sub1"] = None
                opponent_dict["opponent2_headgear_sub2"] = None
                opponent_dict["opponent2_clothes"] = None
                opponent_dict["opponent2_clothes_main"] = None
                opponent_dict["opponent2_clothes_sub0"] = None
                opponent_dict["opponent2_clothes_sub1"] = None
                opponent_dict["opponent2_clothes_sub2"] = None
                opponent_dict["opponent2_shoes"] = None
                opponent_dict["opponent2_shoes_main"] = None
                opponent_dict["opponent2_shoes_sub0"] = None
                opponent_dict["opponent2_shoes_sub1"] = None
                opponent_dict["opponent2_shoes_sub2"] = None
                opponent_dict["opponent3_splatnet_id"] = None
                opponent_dict["opponent3_name"] = None
                opponent_dict["opponent3_level_star"] = None
                opponent_dict["opponent3_level"] = None
                opponent_dict["opponent3_rank"] = None
                opponent_dict["opponent3_weapon"] = None
                opponent_dict["opponent3_gender"] = None
                opponent_dict["opponent3_species"] = None
                opponent_dict["opponent3_kills"] = None
                opponent_dict["opponent3_deaths"] = None
                opponent_dict["opponent3_assists"] = None
                opponent_dict["opponent3_game_paint_point"] = None
                opponent_dict["opponent3_specials"] = None
                opponent_dict["opponent3_headgear"] = None
                opponent_dict["opponent3_headgear_main"] = None
                opponent_dict["opponent3_headgear_sub0"] = None
                opponent_dict["opponent3_headgear_sub1"] = None
                opponent_dict["opponent3_headgear_sub2"] = None
                opponent_dict["opponent3_clothes"] = None
                opponent_dict["opponent3_clothes_main"] = None
                opponent_dict["opponent3_clothes_sub0"] = None
                opponent_dict["opponent3_clothes_sub1"] = None
                opponent_dict["opponent3_clothes_sub2"] = None
                opponent_dict["opponent3_shoes"] = None
                opponent_dict["opponent3_shoes_main"] = None
                opponent_dict["opponent3_shoes_sub0"] = None
                opponent_dict["opponent3_shoes_sub1"] = None
                opponent_dict["opponent3_shoes_sub2"] = None

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
            teammate0_splatnet_id=teammate_dict["teammate0_splatnet_id"],
            teammate0_name=teammate_dict["teammate0_name"],
            teammate0_level_star=teammate_dict["teammate0_level_star"],
            teammate0_level=teammate_dict["teammate0_level"],
            teammate0_rank=teammate_dict["teammate0_rank"],
            teammate0_weapon=teammate_dict["teammate0_weapon"],
            teammate0_gender=teammate_dict["teammate0_gender"],
            teammate0_species=teammate_dict["teammate0_species"],
            teammate0_kills=teammate_dict["teammate0_kills"],
            teammate0_deaths=teammate_dict["teammate0_deaths"],
            teammate0_assists=teammate_dict["teammate0_assists"],
            teammate0_game_paint_point=teammate_dict["teammate0_game_paint_point"],
            teammate0_specials=teammate_dict["teammate0_specials"],
            teammate0_headgear=teammate_dict["teammate0_headgear"],
            teammate0_headgear_main=teammate_dict["teammate0_headgear_main"],
            teammate0_headgear_sub0=teammate_dict["teammate0_headgear_sub0"],
            teammate0_headgear_sub1=teammate_dict["teammate0_headgear_sub1"],
            teammate0_headgear_sub2=teammate_dict["teammate0_headgear_sub2"],
            teammate0_clothes=teammate_dict["teammate0_clothes"],
            teammate0_clothes_main=teammate_dict["teammate0_clothes_main"],
            teammate0_clothes_sub0=teammate_dict["teammate0_clothes_sub0"],
            teammate0_clothes_sub1=teammate_dict["teammate0_clothes_sub1"],
            teammate0_clothes_sub2=teammate_dict["teammate0_clothes_sub2"],
            teammate0_shoes=teammate_dict["teammate0_shoes"],
            teammate0_shoes_main=teammate_dict["teammate0_shoes_main"],
            teammate0_shoes_sub0=teammate_dict["teammate0_shoes_sub0"],
            teammate0_shoes_sub1=teammate_dict["teammate0_shoes_sub1"],
            teammate0_shoes_sub2=teammate_dict["teammate0_shoes_sub2"],
            teammate1_splatnet_id=teammate_dict["teammate1_splatnet_id"],
            teammate1_name=teammate_dict["teammate1_name"],
            teammate1_level_star=teammate_dict["teammate1_level_star"],
            teammate1_level=teammate_dict["teammate1_level"],
            teammate1_rank=teammate_dict["teammate1_rank"],
            teammate1_weapon=teammate_dict["teammate1_weapon"],
            teammate1_gender=teammate_dict["teammate1_gender"],
            teammate1_species=teammate_dict["teammate1_species"],
            teammate1_kills=teammate_dict["teammate1_kills"],
            teammate1_deaths=teammate_dict["teammate1_deaths"],
            teammate1_assists=teammate_dict["teammate1_assists"],
            teammate1_game_paint_point=teammate_dict["teammate1_game_paint_point"],
            teammate1_specials=teammate_dict["teammate1_specials"],
            teammate1_headgear=teammate_dict["teammate1_headgear"],
            teammate1_headgear_main=teammate_dict["teammate1_headgear_main"],
            teammate1_headgear_sub0=teammate_dict["teammate1_headgear_sub0"],
            teammate1_headgear_sub1=teammate_dict["teammate1_headgear_sub1"],
            teammate1_headgear_sub2=teammate_dict["teammate1_headgear_sub2"],
            teammate1_clothes=teammate_dict["teammate1_clothes"],
            teammate1_clothes_main=teammate_dict["teammate1_clothes_main"],
            teammate1_clothes_sub0=teammate_dict["teammate1_clothes_sub0"],
            teammate1_clothes_sub1=teammate_dict["teammate1_clothes_sub1"],
            teammate1_clothes_sub2=teammate_dict["teammate1_clothes_sub2"],
            teammate1_shoes=teammate_dict["teammate1_shoes"],
            teammate1_shoes_main=teammate_dict["teammate1_shoes_main"],
            teammate1_shoes_sub0=teammate_dict["teammate1_shoes_sub0"],
            teammate1_shoes_sub1=teammate_dict["teammate1_shoes_sub1"],
            teammate1_shoes_sub2=teammate_dict["teammate1_shoes_sub2"],
            teammate2_splatnet_id=teammate_dict["teammate2_splatnet_id"],
            teammate2_name=teammate_dict["teammate2_name"],
            teammate2_level_star=teammate_dict["teammate2_level_star"],
            teammate2_level=teammate_dict["teammate2_level"],
            teammate2_rank=teammate_dict["teammate2_rank"],
            teammate2_weapon=teammate_dict["teammate2_weapon"],
            teammate2_gender=teammate_dict["teammate2_gender"],
            teammate2_species=teammate_dict["teammate2_species"],
            teammate2_kills=teammate_dict["teammate2_kills"],
            teammate2_deaths=teammate_dict["teammate2_deaths"],
            teammate2_assists=teammate_dict["teammate2_assists"],
            teammate2_game_paint_point=teammate_dict["teammate2_game_paint_point"],
            teammate2_specials=teammate_dict["teammate2_specials"],
            teammate2_headgear=teammate_dict["teammate2_headgear"],
            teammate2_headgear_main=teammate_dict["teammate2_headgear_main"],
            teammate2_headgear_sub0=teammate_dict["teammate2_headgear_sub0"],
            teammate2_headgear_sub1=teammate_dict["teammate2_headgear_sub1"],
            teammate2_headgear_sub2=teammate_dict["teammate2_headgear_sub2"],
            teammate2_clothes=teammate_dict["teammate2_clothes"],
            teammate2_clothes_main=teammate_dict["teammate2_clothes_main"],
            teammate2_clothes_sub0=teammate_dict["teammate2_clothes_sub0"],
            teammate2_clothes_sub1=teammate_dict["teammate2_clothes_sub1"],
            teammate2_clothes_sub2=teammate_dict["teammate2_clothes_sub2"],
            teammate2_shoes=teammate_dict["teammate2_shoes"],
            teammate2_shoes_main=teammate_dict["teammate2_shoes_main"],
            teammate2_shoes_sub0=teammate_dict["teammate2_shoes_sub0"],
            teammate2_shoes_sub1=teammate_dict["teammate2_shoes_sub1"],
            teammate2_shoes_sub2=teammate_dict["teammate2_shoes_sub2"],
            opponent0_splatnet_id=opponent_dict["opponent0_splatnet_id"],
            opponent0_name=opponent_dict["opponent0_name"],
            opponent0_level_star=opponent_dict["opponent0_level_star"],
            opponent0_level=opponent_dict["opponent0_level"],
            opponent0_rank=opponent_dict["opponent0_rank"],
            opponent0_weapon=opponent_dict["opponent0_weapon"],
            opponent0_gender=opponent_dict["opponent0_gender"],
            opponent0_species=opponent_dict["opponent0_species"],
            opponent0_kills=opponent_dict["opponent0_kills"],
            opponent0_deaths=opponent_dict["opponent0_deaths"],
            opponent0_assists=opponent_dict["opponent0_assists"],
            opponent0_game_paint_point=opponent_dict["opponent0_game_paint_point"],
            opponent0_specials=opponent_dict["opponent0_specials"],
            opponent0_headgear=opponent_dict["opponent0_headgear"],
            opponent0_headgear_main=opponent_dict["opponent0_headgear_main"],
            opponent0_headgear_sub0=opponent_dict["opponent0_headgear_sub0"],
            opponent0_headgear_sub1=opponent_dict["opponent0_headgear_sub1"],
            opponent0_headgear_sub2=opponent_dict["opponent0_headgear_sub2"],
            opponent0_clothes=opponent_dict["opponent0_clothes"],
            opponent0_clothes_main=opponent_dict["opponent0_clothes_main"],
            opponent0_clothes_sub0=opponent_dict["opponent0_clothes_sub0"],
            opponent0_clothes_sub1=opponent_dict["opponent0_clothes_sub1"],
            opponent0_clothes_sub2=opponent_dict["opponent0_clothes_sub2"],
            opponent0_shoes=opponent_dict["opponent0_shoes"],
            opponent0_shoes_main=opponent_dict["opponent0_shoes_main"],
            opponent0_shoes_sub0=opponent_dict["opponent0_shoes_sub0"],
            opponent0_shoes_sub1=opponent_dict["opponent0_shoes_sub1"],
            opponent0_shoes_sub2=opponent_dict["opponent0_shoes_sub2"],
            opponent1_splatnet_id=opponent_dict["opponent1_splatnet_id"],
            opponent1_name=opponent_dict["opponent1_name"],
            opponent1_level_star=opponent_dict["opponent1_level_star"],
            opponent1_level=opponent_dict["opponent1_level"],
            opponent1_rank=opponent_dict["opponent1_rank"],
            opponent1_weapon=opponent_dict["opponent1_weapon"],
            opponent1_gender=opponent_dict["opponent1_gender"],
            opponent1_species=opponent_dict["opponent1_species"],
            opponent1_kills=opponent_dict["opponent1_kills"],
            opponent1_deaths=opponent_dict["opponent1_deaths"],
            opponent1_assists=opponent_dict["opponent1_assists"],
            opponent1_game_paint_point=opponent_dict["opponent1_game_paint_point"],
            opponent1_specials=opponent_dict["opponent1_specials"],
            opponent1_headgear=opponent_dict["opponent1_headgear"],
            opponent1_headgear_main=opponent_dict["opponent1_headgear_main"],
            opponent1_headgear_sub0=opponent_dict["opponent1_headgear_sub0"],
            opponent1_headgear_sub1=opponent_dict["opponent1_headgear_sub1"],
            opponent1_headgear_sub2=opponent_dict["opponent1_headgear_sub2"],
            opponent1_clothes=opponent_dict["opponent1_clothes"],
            opponent1_clothes_main=opponent_dict["opponent1_clothes_main"],
            opponent1_clothes_sub0=opponent_dict["opponent1_clothes_sub0"],
            opponent1_clothes_sub1=opponent_dict["opponent1_clothes_sub1"],
            opponent1_clothes_sub2=opponent_dict["opponent1_clothes_sub2"],
            opponent1_shoes=opponent_dict["opponent1_shoes"],
            opponent1_shoes_main=opponent_dict["opponent1_shoes_main"],
            opponent1_shoes_sub0=opponent_dict["opponent1_shoes_sub0"],
            opponent1_shoes_sub1=opponent_dict["opponent1_shoes_sub1"],
            opponent1_shoes_sub2=opponent_dict["opponent1_shoes_sub2"],
            opponent2_splatnet_id=opponent_dict["opponent2_splatnet_id"],
            opponent2_name=opponent_dict["opponent2_name"],
            opponent2_level_star=opponent_dict["opponent2_level_star"],
            opponent2_level=opponent_dict["opponent2_level"],
            opponent2_rank=opponent_dict["opponent2_rank"],
            opponent2_weapon=opponent_dict["opponent2_weapon"],
            opponent2_gender=opponent_dict["opponent2_gender"],
            opponent2_species=opponent_dict["opponent2_species"],
            opponent2_kills=opponent_dict["opponent2_kills"],
            opponent2_deaths=opponent_dict["opponent2_deaths"],
            opponent2_assists=opponent_dict["opponent2_assists"],
            opponent2_game_paint_point=opponent_dict["opponent2_game_paint_point"],
            opponent2_specials=opponent_dict["opponent2_specials"],
            opponent2_headgear=opponent_dict["opponent2_headgear"],
            opponent2_headgear_main=opponent_dict["opponent2_headgear_main"],
            opponent2_headgear_sub0=opponent_dict["opponent2_headgear_sub0"],
            opponent2_headgear_sub1=opponent_dict["opponent2_headgear_sub1"],
            opponent2_headgear_sub2=opponent_dict["opponent2_headgear_sub2"],
            opponent2_clothes=opponent_dict["opponent2_clothes"],
            opponent2_clothes_main=opponent_dict["opponent2_clothes_main"],
            opponent2_clothes_sub0=opponent_dict["opponent2_clothes_sub0"],
            opponent2_clothes_sub1=opponent_dict["opponent2_clothes_sub1"],
            opponent2_clothes_sub2=opponent_dict["opponent2_clothes_sub2"],
            opponent2_shoes=opponent_dict["opponent2_shoes"],
            opponent2_shoes_main=opponent_dict["opponent2_shoes_main"],
            opponent2_shoes_sub0=opponent_dict["opponent2_shoes_sub0"],
            opponent2_shoes_sub1=opponent_dict["opponent2_shoes_sub1"],
            opponent2_shoes_sub2=opponent_dict["opponent2_shoes_sub2"],
            opponent3_splatnet_id=opponent_dict["opponent3_splatnet_id"],
            opponent3_name=opponent_dict["opponent3_name"],
            opponent3_level_star=opponent_dict["opponent3_level_star"],
            opponent3_level=opponent_dict["opponent3_level"],
            opponent3_rank=opponent_dict["opponent3_rank"],
            opponent3_weapon=opponent_dict["opponent3_weapon"],
            opponent3_gender=opponent_dict["opponent3_gender"],
            opponent3_species=opponent_dict["opponent3_species"],
            opponent3_kills=opponent_dict["opponent3_kills"],
            opponent3_deaths=opponent_dict["opponent3_deaths"],
            opponent3_assists=opponent_dict["opponent3_assists"],
            opponent3_game_paint_point=opponent_dict["opponent3_game_paint_point"],
            opponent3_specials=opponent_dict["opponent3_specials"],
            opponent3_headgear=opponent_dict["opponent3_headgear"],
            opponent3_headgear_main=opponent_dict["opponent3_headgear_main"],
            opponent3_headgear_sub0=opponent_dict["opponent3_headgear_sub0"],
            opponent3_headgear_sub1=opponent_dict["opponent3_headgear_sub1"],
            opponent3_headgear_sub2=opponent_dict["opponent3_headgear_sub2"],
            opponent3_clothes=opponent_dict["opponent3_clothes"],
            opponent3_clothes_main=opponent_dict["opponent3_clothes_main"],
            opponent3_clothes_sub0=opponent_dict["opponent3_clothes_sub0"],
            opponent3_clothes_sub1=opponent_dict["opponent3_clothes_sub1"],
            opponent3_clothes_sub2=opponent_dict["opponent3_clothes_sub2"],
            opponent3_shoes=opponent_dict["opponent3_shoes"],
            opponent3_shoes_main=opponent_dict["opponent3_shoes_main"],
            opponent3_shoes_sub0=opponent_dict["opponent3_shoes_sub0"],
            opponent3_shoes_sub1=opponent_dict["opponent3_shoes_sub1"],
            opponent3_shoes_sub2=opponent_dict["opponent3_shoes_sub2"],
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
