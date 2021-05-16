from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from ...models import species, gender

# Create your models here.


class Rule(models.TextChoices):
    all_rules = "all", _("All Modes")
    sz = "splat_zones", _("Splat Zones")
    rm = "rainmaker", _("Rainmaker")
    cb = "clam_blitz", _("Clam Blitz")
    tc = "tower_control", _("Tower Control")
    tw = "turf_war", _("Turf War")


class Match_Type(models.TextChoices):
    all_types = "all", _("All Types")
    lp = "league_pair", _("League Pair")
    lt = "league_team", _("League Team")
    rk = "gachi", _("Ranked")
    pv = "private", _("Private")
    tw = "turf_war", _("Turf War")
    fs = "fes_solo", _("Splatfest Solo/Pro")
    ft = "fes_team", _("Splatfest Team/Normal")
    fest = "fest", _("Splatfest")
    rg = "regular", _("Turf War")


class Ranks(models.IntegerChoices):
    all_ranks = 21, _("All Ranks")
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
    s_plus3 = 13, _("S+3")
    s_plus4 = 14, _("S+4")
    s_plus5 = 15, _("S+5")
    s_plus6 = 16, _("S+6")
    s_plus7 = 17, _("S+7")
    s_plus8 = 18, _("S+8")
    s_plus9 = 19, _("S+9")
    x_rank = 20, _("X")


Weapons = (
    ("all", _("All Weapons")),
    ("0", _("Sploosh-o-matic")),
    ("1", _("Neo Sploosh-o-matic")),
    ("2", _("Sploosh-o-matic 7")),
    ("10", _("Splattershot Jr.")),
    ("11", _("Custom Splattershot Jr.")),
    ("12", _("Kensa Splattershot Jr.")),
    ("20", _("Splash-o-matic")),
    ("21", _("Neo Splash-o-matic")),
    ("30", _("Aerospray MG")),
    ("31", _("Aerospray RG")),
    ("32", _("Aerospray PG")),
    ("40", _("Splattershot")),
    ("41", _("Tentatek Splattershot")),
    ("42", _("Kensa Splattershot")),
    ("45", _("Hero Shot Replica")),
    ("46", _("Octo Shot Replica")),
    ("50", _(".52 Gal")),
    ("51", _(".52 Gal Deco")),
    ("52", _("Kensa .52 Gal")),
    ("60", _("N-ZAP '85")),
    ("61", _("N-ZAP '89")),
    ("62", _("N-ZAP '83")),
    ("70", _("Splattershot Pro")),
    ("71", _("Forge Splattershot Pro")),
    ("72", _("Kensa Splattershot Pro")),
    ("80", _(".96 Gal")),
    ("81", _(".96 Gal Deco")),
    ("90", _("Jet Squelcher")),
    ("91", _("Custom Jet Squelcher")),
    ("200", _("Luna Blaster")),
    ("201", _("Luna Blaster Neo")),
    ("202", _("Kensa Luna Blaster")),
    ("210", _("Blaster")),
    ("211", _("Custom Blaster")),
    ("215", _("Hero Blaster Replica")),
    ("220", _("Range Blaster")),
    ("221", _("Custom Range Blaster")),
    ("222", _("Grim Range Blaster")),
    ("230", _("Clash Blaster")),
    ("231", _("Clash Blaster Neo")),
    ("240", _("Rapid Blaster")),
    ("241", _("Rapid Blaster Deco")),
    ("242", _("Kensa Rapid Blaster")),
    ("250", _("Rapid Blaster Pro")),
    ("251", _("Rapid Blaster Pro Deco")),
    ("300", _("L-3 Nozzlenose")),
    ("301", _("L-3 Nozzlenose D")),
    ("302", _("Kensa L-3 Nozzlenose")),
    ("310", _("H-3 Nozzlenose")),
    ("311", _("H-3 Nozzlenose D")),
    ("312", _("Cherry H-3 Nozzlenose")),
    ("400", _("Squeezer")),
    ("401", _("Foil Squeezer")),
    ("1000", _("Carbon Roller")),
    ("1001", _("Carbon Roller Deco")),
    ("1010", _("Splat Roller")),
    ("1011", _("Krak-On Splat Roller")),
    ("1012", _("Kensa Splat Roller")),
    ("1015", _("Hero Roller Replica")),
    ("1020", _("Dynamo Roller")),
    ("1021", _("Gold Dynamo Roller")),
    ("1022", _("Kensa Dynamo Roller")),
    ("1030", _("Flingza Roller")),
    ("1031", _("Foil Flingza Roller")),
    ("1100", _("Inkbrush")),
    ("1101", _("Inkbrush Nouveau")),
    ("1102", _("Permanent Inkbrush")),
    ("1110", _("Octobrush")),
    ("1111", _("Octobrush Nouveau")),
    ("1112", _("Kensa Octobrush")),
    ("1115", _("Herobrush Replica")),
    ("2000", _("Classic Squiffer")),
    ("2001", _("New Squiffer")),
    ("2002", _("Fresh Squiffer")),
    ("2010", _("Splat Charger")),
    ("2011", _("Firefin Splat Charger")),
    ("2012", _("Kensa Charger")),
    ("2015", _("Hero Charger Replica")),
    ("2020", _("Splatterscope")),
    ("2021", _("Firefin Splatterscope")),
    ("2022", _("Kensa Splatterscope")),
    ("2030", _("E-liter 4K")),
    ("2031", _("Custom E-liter 4K")),
    ("2040", _("E-liter 4K Scope")),
    ("2041", _("Custom E-liter 4K Scope")),
    ("2050", _("Bamboozler 14 Mk I")),
    ("2051", _("Bamboozler 14 Mk II")),
    ("2052", _("Bamboozler 14 Mk III")),
    ("2060", _("Goo Tuber")),
    ("2061", _("Custom Goo Tuber")),
    ("3000", _("Slosher")),
    ("3001", _("Slosher Deco")),
    ("3002", _("Soda Slosher")),
    ("3005", _("Hero Slosher Replica")),
    ("3010", _("Tri-Slosher")),
    ("3011", _("Tri-Slosher Nouveau")),
    ("3020", _("Sloshing Machine")),
    ("3021", _("Sloshing Machine Neo")),
    ("3022", _("Kensa Sloshing Machine")),
    ("3030", _("Bloblobber")),
    ("3031", _("Bloblobber Deco")),
    ("3040", _("Explosher")),
    ("3041", _("Custom Explosher")),
    ("4000", _("Mini Splatling")),
    ("4001", _("Zink Mini Splatling")),
    ("4002", _("Kensa Mini Splatling")),
    ("4010", _("Heavy Splatling")),
    ("4011", _("Heavy Splating Deco")),
    ("4012", _("Heavy Splatling Remix")),
    ("4015", _("Hero Splatling Replica")),
    ("4020", _("Hydra Splatling")),
    ("4021", _("Custom Hydra Splatling")),
    ("4030", _("Ballpoint Splatling")),
    ("4031", _("Ballpoint Splatling Nouveau")),
    ("4040", _("Nautilus 47")),
    ("4041", _("Nautilus 79")),
    ("5000", _("Dapple Dualies")),
    ("5001", _("Daple Dualies Nouveau")),
    ("5002", _("Clear Dapple Dualies")),
    ("5010", _("Splat Dualies")),
    ("5011", _("Enperry Splat Dualies")),
    ("5012", _("Kensa Splat Dualies")),
    ("5015", _("Hero Dualie Replicas")),
    ("5020", _("Glooga Dualies")),
    ("5021", _("Glooga Dualies Deco")),
    ("5022", _("Kensa Glooga Dualies")),
    ("5030", _("Dualie Squelchers")),
    ("5031", _("Custom Dualie Squelchers")),
    ("5040", _("Dark Tetra Dualies")),
    ("5041", _("Light Tetra Dualies")),
    ("6000", _("Splat Brella")),
    ("6001", _("Sorella Brella")),
    ("6005", _("Hero Brella Replica")),
    ("6010", _("Tenta Brella")),
    ("6011", _("Tenta Sorella Brella")),
    ("6012", _("Tenta Camo Brella")),
    ("6020", _("Undercover Brella")),
    ("6021", _("Undercover Sorella Brella")),
    ("6022", _("Kensa Undercover Brella")),
)


WeaponFamily = (
    (("0", "1", "2"), _("Sploosh-o-matic")),
    (("10", "11", "12"), _("Splattershot Jr.")),
    (("20", "21"), _("Splash-o-matic")),
    (("30", "31", "32"), _("Aerospray MG")),
    (("40", "41", "42", "45", "46"), _("Splattershot")),
    (("50", "51", "52"), _(".52 Gal")),
    (("60", "61", "62"), _("N-ZAP '85")),
    (("70", "71", "72"), _("Splattershot Pro")),
    (("80", "81"), _(".96 Gal")),
    (("90", "91"), _("Jet Squelcher")),
    (("200", "201", "202"), _("Luna Blaster")),
    (("210", "211", "215"), _("Blaster")),
    (("220", "221", "222"), _("Range Blaster")),
    (("230", "231"), _("Clash Blaster")),
    (("240", "241", "242"), _("Rapid Blaster")),
    (("250", "251"), _("Rapid Blaster Pro")),
    (("300", "301", "302"), _("L-3 Nozzlenose")),
    (("310", "311", "312"), _("H-3 Nozzlenose")),
    (("400", "401"), _("Squeezer")),
    (("1000", "1001"), _("Carbon Roller")),
    (("1010", "1011", "1012", "1015"), _("Splat Roller")),
    (("1020", "1021", "1022"), _("Dynamo Roller")),
    (("1030", "1031"), _("Flingza Roller")),
    (("1100", "1101", "1102"), _("Inkbrush")),
    (("1110", "1111", "1112", "1115"), _("Octobrush")),
    (("2000", "2001", "2002"), _("Classic Squiffer")),
    (("2010", "2011", "2012", "2015"), _("Splat Charger")),
    (("2020", "2021", "2022"), _("Splatterscope")),
    (("2030", "2031"), _("E-liter 4K")),
    (("2040", "2041"), _("E-liter 4K Scope")),
    (("2050", "2051", "2052"), _("Bamboozler 14 Mk I")),
    (("2060", "2061"), _("Goo Tuber")),
    (("3000", "3001", "3002", "3005"), _("Slosher")),
    (("3010", "3011"), _("Tri-Slosher")),
    (("3020", "3021", "3022"), _("Sloshing Machine")),
    (("3030", "3031"), _("Bloblobber")),
    (("3040", "3041"), _("Explosher")),
    (("4000", "40041", "4002"), _("Mini Splatling")),
    (("4010", "4011", "4012", "4015"), _("Heavy Splatling")),
    (("4020", "4021"), _("Hydra Splatling")),
    (("4030", "4031"), _("Ballpoint Splatling")),
    (("4040", "4041"), _("Nautilus 47")),
    (("5000", "5001", "5002"), _("Dapple Dualies")),
    (("5010", "5011", "5012", "5015"), _("Splat Dualies")),
    (("5020", "5021", "5022"), _("Glooga Dualies")),
    (("5030", "5031"), _("Dualie Squelchers")),
    (("5040", "5041"), _("Dark Tetra Dualies")),
    (("6000", "6001", "6005"), _("Splat Brella")),
    (("6010", "6011", "6012"), _("Tenta Brella")),
    (("6020", "6021", "6022"), _("Undercover Brella")),
)

WeaponClass = (
    (
        (
            "0",
            "1",
            "2",
            "10",
            "11",
            "12",
            "20",
            "21",
            "30",
            "31",
            "32",
            "40",
            "41",
            "42",
            "45",
            "46",
            "50",
            "51",
            "52",
            "60",
            "61",
            "62",
            "70",
            "71",
            "72",
            "80",
            "81",
            "90",
            "91",
            "400",
            "401",
        ),
        _("Shooters"),
    ),
    (
        (
            "200",
            "201",
            "202",
            "210",
            "211",
            "215",
            "220",
            "221",
            "222",
            "230",
            "231",
            "240",
            "241",
            "242",
            "250",
            "251",
        ),
        _("Blasters"),
    ),
    (("300", "301", "302", "310", "311", "312"), _("Nozzlenose")),
    (
        (
            "1000",
            "1001",
            "1010",
            "1011",
            "1012",
            "1015",
            "1020",
            "1021",
            "1030",
            "1031",
        ),
        _("Rollers"),
    ),
    (("1100", "1101", "1102", "1110", "1111", "1112", "1115"), _("Brushes")),
    (
        (
            "2000",
            "2001",
            "2002",
            "2010",
            "2011",
            "2012",
            "2015",
            "2020",
            "2021",
            "2022",
            "2030",
            "2031",
            "2040",
            "2041",
            "2050",
            "2051",
            "2052",
            "2060",
            "2061",
        ),
        _("Chargers"),
    ),
    (
        (
            "3000",
            "3001",
            "3002",
            "3005",
            "3010",
            "3011",
            "3020",
            "3021",
            "3022",
            "3030",
            "3031",
            "3040",
            "3041",
        ),
        _("Sloshers"),
    ),
    (
        (
            "4000",
            "4001",
            "4002",
            "4010",
            "4011",
            "4012",
            "4015",
            "4020",
            "4021",
            "4030",
            "4031",
            "4040",
            "4041",
        ),
        _("Splatlings"),
    ),
    (
        (
            "5000",
            "5001",
            "5002",
            "5010",
            "5011",
            "5012",
            "5015",
            "5020",
            "5021",
            "5022",
            "5030",
            "5031",
            "5040",
            "5041",
        ),
        _("Dualies"),
    ),
    (
        ("6000", "6001", "6005", "6010", "6011", "6012", "6020", "6021", "6022"),
        _("Brellas"),
    ),
)

WeaponSubs = (
    (
        (
            "0",
            "51",
            "300",
            "221",
            "231",
            "1010",
            "1015",
            "2050",
            "2061",
            "4001",
            "5011",
        ),
        _("Curling Bomb"),
    ),
    (("1", "1011", "1111", "2031", "2041", "4031", "5000", "6010"), _("Squid Beakon")),
    (
        (
            "2",
            "10",
            "41",
            "46",
            "72",
            "401",
            "200",
            "230",
            "1012",
            "1021",
            "1100",
            "2010",
            "2015",
            "2020",
            "3002",
            "3011",
            "5031",
            "6021",
        ),
        _("Splat Bomb"),
    ),
    (
        (
            "11",
            "61",
            "211",
            "1000",
            "1110",
            "1115",
            "2001",
            "3020",
            "4020",
            "5040",
            "6001",
        ),
        _("Autobomb"),
    ),
    (("12", "242", "5002", "6022"), _("Torpedo")),
    (
        ("20", "90", "210", "215", "250", "2051", "4002", "4030", "5001"),
        _("Toxic Mist"),
    ),
    (
        (
            "21",
            "32",
            "40",
            "45",
            "91",
            "301",
            "222",
            "1001",
            "3010",
            "4000",
            "5010",
            "5015",
        ),
        _("Burst Bomb"),
    ),
    (
        (
            "30",
            "42",
            "60",
            "71",
            "311",
            "220",
            "241",
            "1031",
            "1112",
            "2002",
            "2060",
            "3000",
            "3005",
            "4041",
            "5012",
        ),
        _("Suction Bomb"),
    ),
    (
        (
            "31",
            "62",
            "80",
            "1022",
            "1102",
            "2012",
            "2022",
            "3001",
            "3031",
            "3040",
            "4010",
            "4015",
            "5041",
            "6000",
            "6005",
        ),
        _("Sprinkler"),
    ),
    (
        ("50", "70", "310", "2000", "3021", "3041", "4012", "4040", "5030"),
        _("Point Sensor"),
    ),
    (
        (
            "52",
            "81",
            "302",
            "312",
            "400",
            "251",
            "1030",
            "2011",
            "2021",
            "3030",
            "4011",
            "5021",
            "6011",
        ),
        _("Splash Wall"),
    ),
    (
        ("201", "240", "1020", "1101", "2030", "2040", "4021", "5020", "6012", "6020"),
        _("Ink Mine"),
    ),
    (("202", "2052", "3022", "5022"), _("Fizzy Bomb")),
)

WeaponSpecials = (
    (("1001", "5041"), _("Autobomb Launcher")),
    (
        (
            "31",
            "50",
            "300",
            "200",
            "242",
            "1011",
            "1101",
            "2001",
            "2012",
            "2022",
            "3001",
            "3041",
            "4040",
            "5012",
            "5021",
            "6021",
        ),
        _("Baller"),
    ),
    (("32", "52", "72", "1022", "4012"), _("Booyah Bomb")),
    (
        (
            "12",
            "71",
            "312",
            "401",
            "221",
            "1012",
            "2031",
            "2041",
            "2052",
            "3040",
            "4011",
            "6010",
        ),
        _("Bubble Blower"),
    ),
    (("2051", "3002"), _("Burst-Bomb Launcher")),
    (("30", "6011"), _("Curling-Bomb Launcher")),
    (
        (
            "10",
            "60",
            "80",
            "311",
            "251",
            "1021",
            "1102",
            "2000",
            "3010",
            "4021",
            "5022",
            "6022",
        ),
        _("Ink Armor"),
    ),
    (
        (
            "11",
            "62",
            "70",
            "202",
            "220",
            "250",
            "1000",
            "2030",
            "2040",
            "3011",
            "3030",
            "4001",
            "4031",
            "5001",
            "5031",
            "6000",
            "6005",
        ),
        _("Ink Storm"),
    ),
    (
        (
            "20",
            "41",
            "46",
            "301",
            "211",
            "241",
            "1110",
            "1115",
            "2002",
            "2061",
            "4030",
            "4041",
            "5011",
            "5020",
        ),
        _("Inkjet"),
    ),
    (
        (
            "0",
            "40",
            "45",
            "81",
            "210",
            "215",
            "1010",
            "1015",
            "1100",
            "2060",
            "3022",
            "4020",
            "5002",
            "5040",
            "6020",
        ),
        _("Splashdown"),
    ),
    (("240", "1030", "3021", "6001"), _("Splat-Bomb Launcher")),
    (
        (
            "51",
            "91",
            "400",
            "230",
            "1020",
            "2010",
            "2015",
            "2020",
            "3020",
            "4010",
            "4015",
        ),
        _("Sting Ray"),
    ),
    (("21", "201", "2011", "2021", "3031", "5000"), _("Suction-Bomb Launcher")),
    (
        (
            "1",
            "42",
            "61",
            "90",
            "310",
            "222",
            "231",
            "1031",
            "1111",
            "2050",
            "3000",
            "3005",
            "4000",
            "5010",
            "5015",
            "5030",
        ),
        _("Tenta Missiles"),
    ),
    (("2", "302", "1112", "4002", "6012"), _("Ultra Stamp")),
)

Stage = (
    ("all", _("All Stages")),
    ("0", _("The Reef")),
    ("1", _("Musselforge Fitness")),
    ("2", _("Starfish Mainstage")),
    ("3", _("Sturgeon Shipyard")),
    ("4", _("Inkblot Art Academy")),
    ("5", _("Humpback Pump Track")),
    ("6", _("Manta Maria")),
    ("7", _("Port Mackerel")),
    ("8", _("Moray Towers")),
    ("9", _("Snapper Canal")),
    ("10", _("Kelp Dome")),
    ("11", _("Blackbelly Skatepark")),
    ("12", _("Shellendorf Institute")),
    ("13", _("MakoMart")),
    ("14", _("Walleye Warehouse")),
    ("15", _("Arowana Mall")),
    ("16", _("Camp Triggerfish")),
    ("17", _("Piranha Pit")),
    ("18", _("Goby Arena")),
    ("19", _("New Albacore Hotel")),
    ("20", _("Wahoo World")),
    ("21", _("Ancho-V Games")),
    ("22", _("Skipper Pavillion")),
    ("109", _("Zappy Longshocking")),
    ("112", _("The Switches")),
    ("113", _("Sweet Valley Tentacles")),
    ("115", _("Railway Chillin'")),
    ("118", _("Flooders in the Attic")),
    ("119", _("The Splat in Our Zones")),
    ("120", _("The Ink is Spreading")),
    ("121", _("Bridge to Tentaswitchia")),
    ("122", _("The Chronicles of Rolonium")),
    ("9999", _("Shifty Station")),
)

MainAbilities = (
    ("0", _("Ink Saver (Main)")),
    ("1", _("Ink Saver (Sub)")),
    ("2", _("Ink Recovery Up")),
    ("3", _("Run Speed Up")),
    ("4", _("Swim Speed Up")),
    ("5", _("Special Charge Up")),
    ("6", _("Special Saver")),
    ("7", _("Special Power Up")),
    ("8", _("Quick Respawn")),
    ("9", _("Quick Super Jump")),
    ("10", _("Sub Power Up")),
    ("11", _("Ink Resistance Up")),
    ("100", _("Opening Gambit")),
    ("101", _("Last Ditch Effort")),
    ("102", _("Tenacity")),
    ("103", _("Comeback")),
    ("104", _("Ninja Squid")),
    ("105", _("Haunt")),
    ("106", _("Thermal Ink")),
    ("107", _("Respawn Punisher")),
    ("108", _("Ability Doubler")),
    ("109", _("Stealth Jump")),
    ("110", _("Object Shredder")),
    ("111", _("Drop Roller")),
    ("200", _("Bomb Defense Up DX")),
    ("201", _("Main Power Up")),
)

SubAbilities = (
    ("0", _("Ink Saver (Main)")),
    ("1", _("Ink Saver (Sub)")),
    ("2", _("Ink Recovery Up")),
    ("3", _("Run Speed Up")),
    ("4", _("Swim Speed Up")),
    ("5", _("Special Charge Up")),
    ("6", _("Special Saver")),
    ("7", _("Special Power Up")),
    ("8", _("Quick Respawn")),
    ("9", _("Quick Super Jump")),
    ("10", _("Sub Power Up")),
    ("11", _("Ink Resistance Up")),
    ("200", _("Bomb Defense Up DX")),
    ("201", _("Main Power Up")),
    ("255", _("Question Mark")),
)

Headgear = (
    ("1", _("White Headband")),
    ("1000", _("Urchins Cap")),
    ("1001", _("Lightweight Cap")),
    ("1002", _("Takoroka Mesh")),
    ("1003", _("Streetstyle Cap")),
    ("1004", _("Squid-Stitch Cap")),
    ("1005", _("Squidvader Cap")),
    ("1006", _("Camo Mesh")),
    ("1007", _("Five-Panel Cap")),
    ("1008", _("Zekko Mesh")),
    ("1009", _("Backwards Cap")),
    ("1010", _("Two-Stripe Mesh")),
    ("1011", _("Jet Cap")),
    ("1012", _("Cycling Cap")),
    ("1014", _("Cycle King Cap")),
    ("1018", _("Long-Billed Cap")),
    ("1019", _("King Flip Mesh")),
    ("1020", _("Hickory Work Cap")),
    ("1021", _("Wooly Urchins Classic")),
    ("1023", _("Jellyvader Cap")),
    ("1024", _("House-Tag Denim Cap")),
    ("1025", _("Blowfish Newsie")),
    ("1026", _("Do-Rag, Cap, and Glasses")),
    ("1027", _("Pilot Hat")),
    ("2000", _("Bobble Hat")),
    ("2001", _("Short Beanie")),
    ("2002", _("Striped Beanie")),
    ("2003", _("Sporty Bobble Hat")),
    ("2004", _("Special Forces Beret")),
    ("2005", _("Squid Nordic")),
    ("2006", _("Sennyu Bon Bon Beanie")),
    ("2008", _("Knitted Hat")),
    ("2009", _("Annaki Beret")),
    ("2010", _("Yamagiri Beanie")),
    ("2011", _("Sneaky Beanie")),
    ("3000", _("Retro Specs")),
    ("3001", _("Splash Goggles")),
    ("3002", _("Pilot Goggles")),
    ("3003", _("Tinted Shades")),
    ("3004", _("Black Arrowbands")),
    ("3005", _("Snorkel Mask")),
    ("3006", _("White Arrowbands")),
    ("3007", _("Fake Contacts")),
    ("3008", _("18K Aviators")),
    ("3009", _("Full Moon Glasses")),
    ("3010", _("Octoglasses")),
    ("3011", _("Half-Rim Glasses")),
    ("3012", _("Double Egg Shades")),
    ("3013", _("Zekko Cap")),
    ("3014", _("SV925 Circle Shades")),
    ("3015", _("Annaki Beret and Glasses")),
    ("3016", _("Swim Goggles")),
    ("3017", _("Ink-Guard Goggles")),
    ("3018", _("Toni Kensa Goggles")),
    ("3019", _("Sennyu Goggles")),
    ("3020", _("Sennyu Specs")),
    ("4000", _("Safari Hat")),
    ("4001", _("Jungle Hat")),
    ("4002", _("Camping Hat")),
    ("4003", _("Blowfish Bell Hat")),
    ("4004", _("Bamboo Hat")),
    ("4005", _("Straw Boater")),
    ("4006", _("Classic Straw Boater")),
    ("4007", _("Treasure Hunter")),
    ("4008", _("Bucket Hat")),
    ("4009", _("Patched Hat")),
    ("4010", _("Tulip Parasol")),
    ("4011", _("Fugu Bell Hat")),
    ("4012", _("Seashell Bamboo Hat")),
    ("4013", _("Hothouse Hat")),
    ("4014", _("Mountie Hat")),
    ("5000", _("Studio Headphones")),
    ("5001", _("Designer Headphones")),
    ("5002", _("Noise Cancelers")),
    ("5003", _("Squidfin Hook Cans")),
    ("5004", _("Squidlife Headphones")),
    ("5005", _("Studio Octophones")),
    ("5006", _("Sennyu Headphones")),
    ("6000", _("Golf Visor")),
    ("6001", _("FishFry Visor")),
    ("6002", _("Sun Visor")),
    ("6003", _("Takoroka Visor")),
    ("6004", _("Face Visor")),
    ("7000", _("Bike Helmet")),
    ("7002", _("Stealth Goggles")),
    ("7004", _("Skate Helmet")),
    ("7005", _("Visor Skate Helmet")),
    ("7006", _("MTB Helmet")),
    ("7007", _("Hockey Helmet")),
    ("7008", _("Matte Bike Helmet")),
    ("7009", _("Octo Tackle Helmet Deco")),
    ("7010", _("Moist Ghillie Helmet")),
    ("7011", _("Deca Tackle Visor Helmet")),
    ("8000", _("Gas Mask")),
    ("8001", _("Paintball Mask")),
    ("8002", _("Paisley Bandana")),
    ("8003", _("Skull Bandana")),
    ("8004", _("Painter's Mask")),
    ("8005", _("Annaki Mask")),
    ("8006", _("Octoking Facemask")),
    ("8007", _("Squid Facemask")),
    ("8008", _("Firefin Facemask")),
    ("8009", _("King Facemask")),
    ("8010", _("Motocross Nose Guard")),
    ("8011", _("Forge Mask")),
    ("8012", _("Digi-Camo Forge Mask")),
    ("8013", _("Koshien Bandana")),
    ("9001", _("B-ball Headband")),
    ("9002", _("Squash Headband")),
    ("9003", _("Tennis Headband")),
    ("9004", _("Jogging Headband")),
    ("9005", _("Soccer Headband")),
    ("9007", _("FishFry Biscuit Bandana")),
    ("9008", _("Black FishFry Bandana")),
    ("10000", _("Eminence Cuff")),
    ("21000", _("Headlamp Helmet")),
    ("21001", _("Dust Blocker 2000")),
    ("21002", _("Welding Mask")),
    ("21003", _("Beekeeper Hat")),
    ("21004", _("Octoleet Goggles")),
    ("21005", _("Cap of Legend")),
    ("21006", _("Oceanic Hard Hat")),
    ("21007", _("Worker's Head Towel")),
    ("21008", _("Worker's Cap")),
    ("21009", _("Sailor Cap")),
    ("22000", _("Mecha Head - HTR")),
    ("24000", _("Kyonshi Hat")),
    ("24001", _("Li'l Devil Horns")),
    ("24002", _("Hockey Mask")),
    ("24003", _("Anglerfish Mask")),
    ("24004", _("Festive Party Cone")),
    ("24005", _("New Year's Glasses DX")),
    ("24006", _("Twisty Headband")),
    ("24007", _("Eel-Cake Hat")),
    ("24008", ("Purple Novelty Visor")),
    ("24009", _("Green Novelty Visor")),
    ("24010", _("Orange Novelty Visor")),
    ("24011", _("Pink Novelty Visor")),
    ("24012", _("Jetflame Crest")),
    ("24013", _("Fierce Fishskull")),
    ("24014", _("Hivemind Antenna")),
    ("24015", _("Eye of Justice")),
    ("25000", _("Squid Hairclip")),
    ("25001", _("Samurai Helmet")),
    ("25002", _("Power Mask")),
    ("25003", _("Squid Clip-Ons")),
    ("25004", _("Squinja Mask")),
    ("25005", _("Power Mask Mk I")),
    ("25006", _("Pearlescent Crown")),
    ("25007", _("Marinated Headphones")),
    ("25008", _("Enchanted Hat")),
    ("25009", _("Steel Helm")),
    ("25010", _("Fresh Fish Head")),
    ("27000", _("Hero Headset Replica")),
    ("27004", _("Armor Helmet Replica")),
    ("27101", _("Hero Headphones Replica")),
    ("27104", _("Octoling Shades")),
    ("27105", _("Null Visor Replica")),
    ("27106", _("Old-Timey Hat")),
    ("27107", _("Conductor Cap")),
    ("27108", _("Golden Toothpick")),
)

Clothes = (
    ("2", _("Basic Tee")),
    ("3", _("Fresh Octo Tee")),
    ("1000", _("White Tee")),
    ("1001", _("Black Squideye")),
    ("1003", _("Sky Blue Squideye")),
    ("1004", _("Rockenberg White")),
    ("1005", _("Rockenberg Black")),
    ("1006", _("Black Tee")),
    ("1007", _("Sunny-Day Tee")),
    ("1008", _("Rainy-Day Tee")),
    ("1009", _("Reggae Tee")),
    ("1010", _("Fugu Tee")),
    ("1011", _("Mint Tee")),
    ("1012", _("Grape Tee")),
    ("1013", _("Red Vector Tee")),
    ("1014", _("Gray Vector Tee")),
    ("1015", _("Blue Peaks Tee")),
    ("1016", _("Ivory Peaks Tee")),
    ("1017", _("Squid-Stitch Tee")),
    ("1018", _("Pirate-Stripe Tee")),
    ("1019", _("Sailor-Stripe Tee")),
    ("1020", _("White 8-Bit FishFry")),
    ("1021", _("Black 8-Bit FishFry")),
    ("1022", _("White Anchor Tee")),
    ("1023", _("Black Anchor Tee")),
    ("1026", _("Carnivore Tee")),
    ("1027", _("Pearl Tee")),
    ("1028", _("Octo Tee")),
    ("1029", _("Herbivore Tee")),
    ("1030", _("Black V-Neck Tee")),
    ("1031", _("White Deca Logo Tee")),
    ("1032", _("Half-Sleeve Sweater")),
    ("1033", _("King Jersey")),
    ("1034", _("Gray 8-Bit FishFry")),
    ("1035", _("White V-Neck Tee")),
    ("1036", _("White Urchin Rock Tee")),
    ("1037", _("Black Urchin Rock Tee")),
    ("1038", _("Wet Floor Band Tee")),
    ("1039", _("Squid Squad Band Tee")),
    ("1040", _("Navy Deca Logo Tee")),
    ("1041", _("Mister Shrug Tee")),
    ("1042", _("Chirpy Chips Band Tee")),
    ("1043", _("Hightide Era Band Tee")),
    ("1044", _("Red V-Neck Limited Tee")),
    ("1045", _("Green V-Neck Limited Tee")),
    ("1046", _("ω-3 Tee")),
    ("1047", _("Annaki Polpo-Pic Tee")),
    ("1048", _("Firewave Tee")),
    ("1049", _("Takoroka Galactic Tie Dye")),
    ("1050", _("Takoroka Rainbow Tie Dye")),
    ("1051", _("Missus Shrug Tee")),
    ("1052", _("League Tee")),
    ("1053", _("Friend Tee")),
    ("1054", _("Tentatek Slogan Tee")),
    ("1055", _("Icewave Tee")),
    ("1056", _("Octoking HK Jersey")),
    ("1057", _("Dakro Nana Tee")),
    ("1058", _("Dakro Golden Tee")),
    ("1059", ("Black Velour Octoking Tee")),
    ("1060", _("Green Velour Octoking Tee")),
    ("1061", _("SWC Logo Tee")),
    ("2000", _("White Striped LS")),
    ("2001", _("Black LS")),
    ("2002", _("Purple Camo LS")),
    ("2003", _("Navy Striped LS")),
    ("2004", _("Zekko Baseball LS")),
    ("2005", _("Varsity Baseball LS")),
    ("2006", _("Black Baseball LS")),
    ("2007", _("White Baseball LS")),
    ("2008", _("White LS")),
    ("2009", _("Green Striped LS")),
    ("2010", _("Squidmark LS")),
    ("2011", _("Zink LS")),
    ("2012", _("Striped Peaks LS")),
    ("2013", _("Pink Easy-Stripe Shirt")),
    ("2014", _("Inkopolis Squaps Jersey")),
    ("2015", _("Annaki Drive Tee")),
    ("2016", _("Lime Easy-Stripe Shirt")),
    ("2017", _("Annaki Evolution Tee")),
    ("2018", _("Zekko Long Carrot Tee")),
    ("2019", _("Zekko Long Radish Tee")),
    ("2020", _("Black Cuttlegear LS")),
    ("2021", _("Takoroka Crazy Baseball LS")),
    ("2022", _("Red Cuttlegear LS")),
    ("2023", _("Khaki 16-Bit FishFry")),
    ("2024", _("Blue 16-Bit FishFry")),
    ("3000", _("White Layered LS")),
    ("3001", _("Yellow Layered LS")),
    ("3002", _("Camo Layered LS")),
    ("3003", _("Black Layered LS")),
    ("3004", _("Zink Layered LS")),
    ("3005", _("Layered Anchor LS")),
    ("3006", _("Choco Layered LS")),
    ("3007", _("Part-Time Pirate")),
    ("3008", _("Layered Vector LS")),
    ("3009", _("Green Tee")),
    ("3010", _("Red Tentatek Tee")),
    ("3011", _("Blue Tentatek Tee")),
    ("3012", _("Octo Layered LS")),
    ("3013", _("Squid Yellow Layered LS")),
    ("4000", _("Shrimp-Pink Polo")),
    ("4001", _("Striped Rugby")),
    ("4002", _("Tricolor Rugby")),
    ("4003", _("Sage Polo")),
    ("4004", _("Black Polo")),
    ("4005", _("Cycling Shirt")),
    ("4006", _("Cycle King Jersey")),
    ("4007", _("Slipstream United")),
    ("4008", _("FC Albacore")),
    ("5000", _("Olive Ski Jacket")),
    ("5001", _("Takoroka Nylon Vintage")),
    ("5002", _("Berry Ski Jacket")),
    ("5003", _("Varsity Jacket")),
    ("5004", _("School Jersey")),
    ("5005", _("Green Cardigan")),
    ("5006", _("Black Inky Rider")),
    ("5007", _("White Inky Rider")),
    ("5008", _("Retro Gamer Jersey")),
    ("5009", _("Orange Cardigan")),
    ("5010", _("Forge Inkling Parka")),
    ("5011", _("Forge Octarian Jacket")),
    ("5012", _("Blue Sailor Suit")),
    ("5013", _("White Sailor Suit")),
    ("5014", _("Squid Satin Jacket")),
    ("5015", _("Zapfish Satin Jacket")),
    ("5016", _("Krak-On 528")),
    ("5017", _("Chilly Mountain Coat")),
    ("5018", _("Takoroka Windcrusher")),
    ("5019", _("Matcha Down Jacket")),
    ("5020", _("FA-01 Jacket")),
    ("5021", _("FA-01 Reversed")),
    ("5022", _("Pullover Coat")),
    ("5023", _("Kensa Coat")),
    ("5024", _("Birded Corduroy Jacket")),
    ("5025", _("Deep-Octo Satin Jacket")),
    ("5026", _("Zekko Redleaf Coat")),
    ("5027", _("Eggplant Mountain Coat")),
    ("5028", _("Zekko Jade Coat")),
    ("5029", _("Light Bomber Jacket")),
    ("5030", _("Brown FA-11 Bomber")),
    ("5031", _("Gray FA-11 Bomber")),
    ("5032", _("Milky Eminence Jacket")),
    ("5033", _("Navy Eminence Jacket")),
    ("5034", _("Tumeric Zekko Coat")),
    ("5035", _("Custom Painted F-3")),
    ("5036", _("Dark Bomber Jacket")),
    ("5037", _("Moist Ghillie Suit")),
    ("5038", _("White Leather F-3")),
    ("5039", _("Chili-Pepper Ski Jacket")),
    ("5040", _("Whale-Knit Sweater")),
    ("5041", _("Rockin' Leather Jacket")),
    ("5042", _("Kung-Fu Zip-Up")),
    ("5043", _("Panda Kung-Fu Zip-Up")),
    ("5044", _("Sennyu Suit")),
    ("6000", _("B-ball Jersey (Home)")),
    ("6001", _("B-ball Jersey (Away)")),
    ("6003", _("White King Tank")),
    ("6004", _("Slash King Tank")),
    ("6005", _("Navy King Tank")),
    ("6006", _("Lob-Stars Jersey")),
    ("7000", _("Gray College Sweat")),
    ("7001", _("Squidmark Sweat")),
    ("7002", _("Retro Sweat")),
    ("7003", _("Firefin Navy Sweat")),
    ("7004", _("Navy College Sweat")),
    ("7005", _("Reel Sweat")),
    ("7006", _("Anchor Sweat")),
    ("7007", _("Negative Longcuff Sweater")),
    ("7008", _("Short Knit Layers")),
    ("7009", _("Positive Longcuff Sweater")),
    ("7010", _("Annaki Blue Cuff")),
    ("7011", _("Annaki Yellow Cuff")),
    ("7012", _("Annaki Red Cuff")),
    ("7013", _("N-Pacer Sweat")),
    ("7014", _("Octarian Retro")),
    ("7015", _("Takoroka Jersey")),
    ("8000", _("Lumberjack Shirt")),
    ("8001", _("Rodeo Shirt")),
    ("8002", _("Green-Check Shirt")),
    ("8003", _("White Shirt")),
    ("8004", _("Urchins Jersey")),
    ("8005", _("Aloha Shirt")),
    ("8006", _("Red-Check Shirt")),
    ("8007", _("Baby-Jelly Shirt")),
    ("8008", _("Baseball Jersey")),
    ("8009", _("Gray Mixed Shirt")),
    ("8010", _("Vintage Check Shirt")),
    ("8011", _("Round-Collar Shirt")),
    ("8012", _("Logo Aloha Shirt")),
    ("8013", _("Striped Shirt")),
    ("8014", _("Linen Shirt")),
    ("8015", _("Shirt and Tie")),
    ("8017", _("Hula Punk Shirt")),
    ("8018", _("Octobowler Shirt")),
    ("8019", _("Inkfall Shirt")),
    ("8020", _("Crimson Parashooter")),
    ("8021", _("Baby-Jelly Shirt and Tie")),
    ("8022", _("Prune Parashooter")),
    ("8023", _("Red Hula Punk with Tie")),
    ("8024", _("Chili Octo Aloha")),
    ("8025", _("Annaki Flannel Hoodie")),
    ("8026", _("Ink-Wash Shirt")),
    ("8027", _("Dots-On-Dots Shirt")),
    ("8028", _("Toni K. Baseball Jersey")),
    ("8029", _("Online Jersey")),
    ("9000", _("Mountain Vest")),
    ("9001", _("Forest Vest")),
    ("9002", _("Dark Urban Vest")),
    ("9003", _("Yellow Urban Vest")),
    ("9004", _("Squid-Pattern Waistcoat")),
    ("9005", _("Squidstar Waistcoat")),
    ("9007", _("Fishing Vest")),
    ("9008", _("Front Zip Vest")),
    ("9009", _("Silver Tentatek Vest")),
    ("10000", _("Camo Zip Hoodie")),
    ("10001", _("Green Zip Hoodie")),
    ("10002", _("Zekko Hoodie")),
    ("10004", _("Shirt with Blue Hoodie")),
    ("10005", _("Grape Hoodie")),
    ("10006", _("Gray Hoodie")),
    ("10007", _("Hothouse Hoodie")),
    ("10008", _("Pink Hoodie")),
    ("10009", _("Olive Zekko Parka")),
    ("10010", _("Black Hoodie")),
    ("10011", _("Octo Support Hoodie")),
    ("21000", _("Squiddor Polo")),
    ("21001", _("Anchor Life Vest")),
    ("21002", _("Juice Parka")),
    ("21003", _("Garden Gear")),
    ("21004", _("Crustwear XXL")),
    ("21005", _("North-Country Parka")),
    ("21006", _("Octoleet Armor")),
    ("21007", _("Record Shop Look EP")),
    ("21008", _("Dev Uniform")),
    ("21009", _("Office Attire")),
    ("21010", _("SRL Coat")),
    ("22000", _("Mecha Body - AKM")),
    ("23000", _("Splatfest Tee Replica")),
    ("25000", _("School Uniform")),
    ("25001", _("Samurai Jacket")),
    ("25002", _("Power Armor")),
    ("25003", _("School Cardigan")),
    ("25004", _("Squinja Suit")),
    ("25005", _("Power Armor Mk I")),
    ("25006", _("Pearlescent Hoodie")),
    ("25007", _("Marinated Top")),
    ("25008", _("Enchanted Robe")),
    ("25009", _("Steel Platemail")),
    ("25010", _("Fresh Fish Gloves")),
    ("26000", _("Splatfest Tee")),
    ("27000", _("Hero Jacket Replica")),
    ("27004", _("Armor Jacket Replica")),
    ("27101", _("Hero Hoodie Replica")),
    ("27104", _("Neo Octoling Armor")),
    ("27105", _("Null Armor Replica")),
    ("27015", _("Null Armor Replica")),
    ("27106", _("Old-Timey Clothes")),
)

Shoes = (
    ("1", _("Cream Basics")),
    ("1000", _("Blue Lo-Tops")),
    ("1001", _("Banana Basics")),
    ("1002", _("LE Lo-Tops")),
    ("1003", _("White Seahorses")),
    ("1004", _("Orange Lo-Tops")),
    ("1005", _("Black Seahorses")),
    ("1006", _("Clownfish Basics")),
    ("1007", _("Yellow Seahorses")),
    ("1008", _("Strapping Whites")),
    ("1009", _("Strapping Reds")),
    ("1010", _("Soccer Shoes")),
    ("1011", _("LE Soccer Shoes")),
    ("1012", _("Sunny Climbing Shoes")),
    ("1013", _("Birch Climbing Shoes")),
    ("1014", _("Green Laceups")),
    ("1015", _("White Laceless Dakroniks")),
    ("1016", _("Blue Laceless Dakroniks")),
    ("1017", _("Suede Gray Lace-Ups")),
    ("1018", ("Suede Nation Lace-Ups")),
    ("1019", _("Suede Marine Lace-Ups")),
    ("1020", _("Toni Kensa Soccer Shoes")),
    ("2000", _("Red Hi-Horses")),
    ("2001", _("Zombie Hi-Horses")),
    ("2002", _("Cream Hi-Tops")),
    ("2003", _("Purple Hi-Horses")),
    ("2004", _("Hunter Hi-Tops")),
    ("2005", _("Red Hi-Tops")),
    ("2006", _("Gold Hi-Horses")),
    ("2008", _("Shark Moccasins")),
    ("2009", _("Mawcasins")),
    ("2010", _("Chocolate Dakroniks")),
    ("2011", _("Mint Dakroniks")),
    ("2012", _("Black Dakroniks")),
    ("2013", _("Piranha Moccasins")),
    ("2014", _("White Norimaki 750s")),
    ("2015", _("Black Norimaki 750s")),
    ("2016", _("Sunset Orca Hi-Tops")),
    ("2017", _("Red and Black Squidkid IV")),
    ("2018", _("Blue and Black Squidkd IV")),
    ("2019", _("Gray Sea-Slug Hi-Tops")),
    ("2020", _("Orca Hi-Tops")),
    ("2021", _("Milky Enperrials")),
    ("2022", _("Navy Enperrials")),
    ("2023", _("Amber Sea Slug Hi-Tops")),
    ("2024", _("Yellow Iromaki 750s")),
    ("2025", _("Red and White Squidkid V")),
    ("2026", _("Honey and Orange Squidkid V")),
    ("2027", _("Sun and Shade Squidkid IV")),
    ("2028", _("Orca Woven Hi-Tops")),
    ("2029", _("Green Iromaki 750s")),
    ("2030", _("Purple Iromaki 750s")),
    ("2031", _("Red Iromaki 750s")),
    ("2032", _("Blue Iromaki 750s")),
    ("2033", _("Orange Iromaki 750s")),
    ("2034", _("Red Power Stripes")),
    ("2035", _("Blue Power Stripes")),
    ("2036", _("Toni Kensa Black Hi-Tops")),
    ("2037", _("Sesame Salt 270s")),
    ("2038", _("Black and Blue Squidkid V")),
    ("2039", _("Orca Passion Hi-Tops")),
    ("2040", _("Truffle Canvas Hi-Tops")),
    ("2041", _("Online Squidkid V")),
    ("3000", _("Pink Trainers")),
    ("3001", _("Orange Arrows")),
    ("3002", _("Neon Sea Slugs")),
    ("3003", _("White Arrows")),
    ("3004", _("Cyan Trainers")),
    ("3005", _("Blue Sea Slugs")),
    ("3006", _("Red Sea Slugs")),
    ("3007", _("Purple Sea Slugs")),
    ("3008", _("Crazy Arrows")),
    ("3009", _("Black Trainers")),
    ("3010", _("Violet Trainers")),
    ("3011", _("Canary Trainers")),
    ("3012", _("Yellow-Mesh Sneakers")),
    ("3013", _("Arrow Pull-Ons")),
    ("3014", _("Red-Mesh Sneakers")),
    ("3015", _("N-Pacer CaO")),
    ("3016", _("N-Pacer Ag")),
    ("3017", _("N-Pacer Au")),
    ("3018", _("Sea Slug Volt 95s")),
    ("3019", _("Athletic Arrows")),
    ("4000", _("Oyster Clogs")),
    ("4001", _("Choco Clogs")),
    ("4002", _("Blueberry Casuals")),
    ("4003", _("Plum Casuals")),
    ("4007", _("Neon Delta Straps")),
    ("4008", _("Black Flip-Flops")),
    ("4009", _("Snow Delta Straps")),
    ("4010", _("Luminous Delta Straps")),
    ("4011", _("Red FishFry Sandals")),
    ("4012", _("Yellow FishFry Sandals")),
    ("4013", _("Musselforge Flip-Flops")),
    ("5000", _("Trail Boots")),
    ("5001", _("Custom Trail Boots")),
    ("5002", _("Pro Trail Boots")),
    ("6000", _("Moto Boots")),
    ("6001", _("Tan Work Boots")),
    ("6002", _("Red Work Boots")),
    ("6003", _("Blue Moto Boots")),
    ("6004", _("Green Rain Boots")),
    ("6005", _("Acerola Rain Boots")),
    ("6006", _("Punk Whites")),
    ("6007", _("Punk Cherries")),
    ("6008", _("Punk Yellows")),
    ("6009", _("Bubble Rain Boots")),
    ("6010", _("Snowy Down Boots")),
    ("6011", _("Icy Down Boots")),
    ("6012", _("Hunting Boots")),
    ("6013", _("Punk Blacks")),
    ("6014", _("Deepsea Leather Boots")),
    ("6015", _("Moist Ghillie Boots")),
    ("6016", _("Annaki Arachno Boots")),
    ("6017", _("New-Leaf Leather Boots")),
    ("6018", _("Tea-Green Hunting Boots")),
    ("7000", _("Blue Slip-Ons")),
    ("7001", _("Red Slip-Ons")),
    ("7002", _("Squid-Stitch Slip-Ons")),
    ("7003", _("Polka-dot Slip-Ons")),
    ("8000", _("White Kicks")),
    ("8001", _("Cherry Kicks")),
    ("8002", _("Turquois Kicks")),
    ("8003", _("Squink Wingtips")),
    ("8004", _("Roasted Brogues")),
    ("8005", _("Kid Clams")),
    ("8006", _("Smoky Wingtips")),
    ("8007", _("Navy Red-Soled Wingtips")),
    ("8008", _("Gray Yellow-Soled Wingtips")),
    ("8009", _("Inky Kid Clams")),
    ("8010", _("Annaki Habaneros")),
    ("8011", _("Annaki Tigers")),
    ("8012", _("Sennyu Inksoles")),
    ("21001", _("Angry Rain Boots")),
    ("21002", _("Non-slip Senseis")),
    ("21003", _("Octoleet Boots")),
    ("21004", _("Friendship Bracelet")),
    ("21005", _("Flipper Floppers")),
    ("21006", _("Wooden Sandals")),
    ("22000", _("Mecha Legs - LBS")),
    ("23000", _("Pearl-Scout Lace-Ups")),
    ("23001", _("Pearlescent Squidkid IV")),
    ("23002", _("Pearl Punk Crowns")),
    ("23003", _("New-Day Arrows")),
    ("23004", _("Marination Lace-Ups")),
    ("23005", _("Rina Squidkid IV")),
    ("23006", _("Trooper Power Stripes")),
    ("23007", _("Midnight Slip-Ons")),
    ("25000", _("School Shoes")),
    ("25001", _("Samurai Shoes")),
    ("25002", _("Power Boots")),
    ("25003", _("Fringed Loafers")),
    ("25004", _("Squinja Boots")),
    ("25005", _("Power Boots Mk I")),
    ("25006", _("Pearlescent Kicks")),
    ("25007", _("Marinated Slip-Ons")),
    ("25008", _("Enchanted Boots")),
    ("25009", _("Steel Greaves")),
    ("25010", _("Fresh Fish Feet")),
    ("27000", _("Hero Runner Replicas")),
    ("27004", _("Armor Boot Replicas")),
    ("27101", _("Hero Snowboots Replicas")),
    ("27104", _("Neo Octoling Boots")),
    ("27105", _("Null Boots Replica")),
    ("27106", _("Old-Timey Shoes")),
)


class Battle(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["player_splatnet_id", "battle_number"], name="unique-two-match"
            ),
        ]

    # general match stats
    splatnet_upload = models.BooleanField()
    splatnet_json = models.JSONField(null=True, blank=True)
    stat_ink_upload = models.BooleanField()
    stat_ink_json = models.JSONField(null=True, blank=True)
    rule = models.CharField(max_length=13, choices=Rule.choices)
    match_type = models.CharField(max_length=11, choices=Match_Type.choices)
    stage = models.CharField(max_length=4, choices=Stage)
    win = models.BooleanField(null=True)
    has_disconnected_player = models.BooleanField(null=True)
    time = models.PositiveIntegerField(null=True)
    battle_number = models.CharField(
        "SplatNet Battle Number", max_length=255, null=True
    )
    win_meter = models.DecimalField(
        "Freshness", blank=True, null=True, decimal_places=1, max_digits=3
    )
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
    player_user = models.ForeignKey(
        User, related_name="two_battles", on_delete=models.CASCADE, null=True
    )
    player_weapon = models.CharField(max_length=4, choices=Weapons)
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
    player_gender = models.CharField(max_length=4, null=True, choices=gender)
    player_species = models.CharField(max_length=9, null=True, choices=species)
    # headgear
    player_headgear = models.CharField(null=True, max_length=5, choices=Headgear)
    player_headgear_main = models.CharField(
        null=True, max_length=3, choices=MainAbilities
    )
    player_headgear_sub0 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    player_headgear_sub1 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    player_headgear_sub2 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    # clothes
    player_clothes = models.CharField(null=True, max_length=5, choices=Clothes)
    player_clothes_main = models.CharField(
        null=True, max_length=3, choices=MainAbilities
    )
    player_clothes_sub0 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    player_clothes_sub1 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    player_clothes_sub2 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    # shoes
    player_shoes = models.CharField(null=True, max_length=5, choices=Shoes)
    player_shoes_main = models.CharField(null=True, max_length=3, choices=MainAbilities)
    player_shoes_sub0 = models.CharField(null=True, max_length=3, choices=SubAbilities)
    player_shoes_sub1 = models.CharField(null=True, max_length=3, choices=SubAbilities)
    player_shoes_sub2 = models.CharField(null=True, max_length=3, choices=SubAbilities)

    # teammate 1
    # basic stats
    teammate1_splatnet_id = models.CharField(null=True, max_length=16)
    teammate1_name = models.CharField(null=True, max_length=10)
    teammate1_level_star = models.PositiveSmallIntegerField(null=True)
    teammate1_level = models.PositiveSmallIntegerField(null=True)
    teammate1_rank = models.PositiveSmallIntegerField(null=True, choices=Ranks.choices)
    teammate1_weapon = models.CharField(null=True, max_length=4, choices=Weapons)
    teammate1_gender = models.CharField(max_length=4, null=True, choices=gender)
    teammate1_species = models.CharField(max_length=9, null=True, choices=species)
    teammate1_kills = models.PositiveSmallIntegerField(null=True)
    teammate1_deaths = models.PositiveSmallIntegerField(null=True)
    teammate1_assists = models.PositiveSmallIntegerField(null=True)
    teammate1_game_paint_point = models.PositiveSmallIntegerField(null=True)
    teammate1_specials = models.PositiveSmallIntegerField(null=True)
    # headgear
    teammate1_headgear = models.CharField(null=True, max_length=5, choices=Headgear)
    teammate1_headgear_main = models.CharField(
        null=True, max_length=3, choices=MainAbilities
    )
    teammate1_headgear_sub0 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    teammate1_headgear_sub1 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    teammate1_headgear_sub2 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    # clothes
    teammate1_clothes = models.CharField(null=True, max_length=5, choices=Clothes)
    teammate1_clothes_main = models.CharField(
        null=True, max_length=3, choices=MainAbilities
    )
    teammate1_clothes_sub0 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    teammate1_clothes_sub1 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    teammate1_clothes_sub2 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    # shoes
    teammate1_shoes = models.CharField(null=True, max_length=5, choices=Shoes)
    teammate1_shoes_main = models.CharField(
        null=True, max_length=3, choices=MainAbilities
    )
    teammate1_shoes_sub0 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    teammate1_shoes_sub1 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    teammate1_shoes_sub2 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )

    # teammate 2
    # basic stats
    teammate2_splatnet_id = models.CharField(null=True, max_length=16)
    teammate2_name = models.CharField(null=True, max_length=10)
    teammate2_level_star = models.PositiveSmallIntegerField(null=True)
    teammate2_level = models.PositiveSmallIntegerField(null=True)
    teammate2_rank = models.PositiveSmallIntegerField(null=True, choices=Ranks.choices)
    teammate2_weapon = models.CharField(null=True, max_length=4, choices=Weapons)
    teammate2_gender = models.CharField(max_length=4, null=True, choices=gender)
    teammate2_species = models.CharField(max_length=9, null=True, choices=species)
    teammate2_kills = models.PositiveSmallIntegerField(null=True)
    teammate2_deaths = models.PositiveSmallIntegerField(null=True)
    teammate2_assists = models.PositiveSmallIntegerField(null=True)
    teammate2_game_paint_point = models.PositiveSmallIntegerField(null=True)
    teammate2_specials = models.PositiveSmallIntegerField(null=True)
    # headgear
    teammate2_headgear = models.CharField(null=True, max_length=5, choices=Headgear)
    teammate2_headgear_main = models.CharField(
        null=True, max_length=3, choices=MainAbilities
    )
    teammate2_headgear_sub0 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    teammate2_headgear_sub1 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    teammate2_headgear_sub2 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    # clothes
    teammate2_clothes = models.CharField(null=True, max_length=5, choices=Clothes)
    teammate2_clothes_main = models.CharField(
        null=True, max_length=3, choices=MainAbilities
    )
    teammate2_clothes_sub0 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    teammate2_clothes_sub1 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    teammate2_clothes_sub2 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    # shoes
    teammate2_shoes = models.CharField(null=True, max_length=5, choices=Shoes)
    teammate2_shoes_main = models.CharField(
        null=True, max_length=3, choices=MainAbilities
    )
    teammate2_shoes_sub0 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    teammate2_shoes_sub1 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    teammate2_shoes_sub2 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )

    # teammate 0
    # basic stats
    teammate0_splatnet_id = models.CharField(null=True, max_length=16)
    teammate0_name = models.CharField(null=True, max_length=10)
    teammate0_level_star = models.PositiveSmallIntegerField(null=True)
    teammate0_level = models.PositiveSmallIntegerField(null=True)
    teammate0_rank = models.PositiveSmallIntegerField(null=True, choices=Ranks.choices)
    teammate0_weapon = models.CharField(null=True, max_length=4, choices=Weapons)
    teammate0_gender = models.CharField(max_length=4, null=True, choices=gender)
    teammate0_species = models.CharField(max_length=9, null=True, choices=species)
    teammate0_kills = models.PositiveSmallIntegerField(null=True)
    teammate0_deaths = models.PositiveSmallIntegerField(null=True)
    teammate0_assists = models.PositiveSmallIntegerField(null=True)
    teammate0_game_paint_point = models.PositiveSmallIntegerField(null=True)
    teammate0_specials = models.PositiveSmallIntegerField(null=True)
    # headgear
    teammate0_headgear = models.CharField(null=True, max_length=5, choices=Headgear)
    teammate0_headgear_main = models.CharField(
        null=True, max_length=3, choices=MainAbilities
    )
    teammate0_headgear_sub0 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    teammate0_headgear_sub1 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    teammate0_headgear_sub2 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    # clothes
    teammate0_clothes = models.CharField(null=True, max_length=5, choices=Clothes)
    teammate0_clothes_main = models.CharField(
        null=True, max_length=3, choices=MainAbilities
    )
    teammate0_clothes_sub0 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    teammate0_clothes_sub1 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    teammate0_clothes_sub2 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    # shoes
    teammate0_shoes = models.CharField(null=True, max_length=5, choices=Shoes)
    teammate0_shoes_main = models.CharField(
        null=True, max_length=3, choices=MainAbilities
    )
    teammate0_shoes_sub0 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    teammate0_shoes_sub1 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    teammate0_shoes_sub2 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )

    # opponent 0
    # basic stats
    opponent0_splatnet_id = models.CharField(null=True, max_length=16)
    opponent0_name = models.CharField(null=True, max_length=10)
    opponent0_level_star = models.PositiveSmallIntegerField(null=True)
    opponent0_level = models.PositiveSmallIntegerField(null=True)
    opponent0_rank = models.PositiveSmallIntegerField(null=True, choices=Ranks.choices)
    opponent0_weapon = models.CharField(null=True, max_length=4, choices=Weapons)
    opponent0_gender = models.CharField(max_length=4, null=True, choices=gender)
    opponent0_species = models.CharField(max_length=9, null=True, choices=species)
    opponent0_kills = models.PositiveSmallIntegerField(null=True)
    opponent0_deaths = models.PositiveSmallIntegerField(null=True)
    opponent0_assists = models.PositiveSmallIntegerField(null=True)
    opponent0_game_paint_point = models.PositiveSmallIntegerField(null=True)
    opponent0_specials = models.PositiveSmallIntegerField(null=True)
    # headgear
    opponent0_headgear = models.CharField(null=True, max_length=5, choices=Headgear)
    opponent0_headgear_main = models.CharField(
        null=True, max_length=3, choices=MainAbilities
    )
    opponent0_headgear_sub0 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    opponent0_headgear_sub1 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    opponent0_headgear_sub2 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    # clothes
    opponent0_clothes = models.CharField(null=True, max_length=5, choices=Clothes)
    opponent0_clothes_main = models.CharField(
        null=True, max_length=3, choices=MainAbilities
    )
    opponent0_clothes_sub0 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    opponent0_clothes_sub1 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    opponent0_clothes_sub2 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    # shoes
    opponent0_shoes = models.CharField(null=True, max_length=5, choices=Shoes)
    opponent0_shoes_main = models.CharField(
        null=True, max_length=3, choices=MainAbilities
    )
    opponent0_shoes_sub0 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    opponent0_shoes_sub1 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    opponent0_shoes_sub2 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )

    # opponent 1
    # basic stats
    opponent1_splatnet_id = models.CharField(null=True, max_length=16)
    opponent1_name = models.CharField(null=True, max_length=10)
    opponent1_level_star = models.PositiveSmallIntegerField(null=True)
    opponent1_level = models.PositiveSmallIntegerField(null=True)
    opponent1_rank = models.PositiveSmallIntegerField(null=True, choices=Ranks.choices)
    opponent1_weapon = models.CharField(null=True, max_length=4, choices=Weapons)
    opponent1_gender = models.CharField(max_length=4, null=True, choices=gender)
    opponent1_species = models.CharField(max_length=9, null=True, choices=species)
    opponent1_kills = models.PositiveSmallIntegerField(null=True)
    opponent1_deaths = models.PositiveSmallIntegerField(null=True)
    opponent1_assists = models.PositiveSmallIntegerField(null=True)
    opponent1_game_paint_point = models.PositiveSmallIntegerField(null=True)
    opponent1_specials = models.PositiveSmallIntegerField(null=True)
    # headgear
    opponent1_headgear = models.CharField(null=True, max_length=5, choices=Headgear)
    opponent1_headgear_main = models.CharField(
        null=True, max_length=3, choices=MainAbilities
    )
    opponent1_headgear_sub0 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    opponent1_headgear_sub1 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    opponent1_headgear_sub2 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    # clothes
    opponent1_clothes = models.CharField(null=True, max_length=5, choices=Clothes)
    opponent1_clothes_main = models.CharField(
        null=True, max_length=3, choices=MainAbilities
    )
    opponent1_clothes_sub0 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    opponent1_clothes_sub1 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    opponent1_clothes_sub2 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    # shoes
    opponent1_shoes = models.CharField(null=True, max_length=5, choices=Shoes)
    opponent1_shoes_main = models.CharField(
        null=True, max_length=3, choices=MainAbilities
    )
    opponent1_shoes_sub0 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    opponent1_shoes_sub1 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    opponent1_shoes_sub2 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )

    # opponent 2
    # basic stats
    opponent2_splatnet_id = models.CharField(null=True, max_length=16)
    opponent2_name = models.CharField(null=True, max_length=10)
    opponent2_level_star = models.PositiveSmallIntegerField(null=True)
    opponent2_level = models.PositiveSmallIntegerField(null=True)
    opponent2_rank = models.PositiveSmallIntegerField(null=True, choices=Ranks.choices)
    opponent2_weapon = models.CharField(null=True, max_length=4, choices=Weapons)
    opponent2_gender = models.CharField(max_length=4, null=True, choices=gender)
    opponent2_species = models.CharField(max_length=9, null=True, choices=species)
    opponent2_kills = models.PositiveSmallIntegerField(null=True)
    opponent2_deaths = models.PositiveSmallIntegerField(null=True)
    opponent2_assists = models.PositiveSmallIntegerField(null=True)
    opponent2_game_paint_point = models.PositiveSmallIntegerField(null=True)
    opponent2_specials = models.PositiveSmallIntegerField(null=True)
    # headgear
    opponent2_headgear = models.CharField(null=True, max_length=5, choices=Headgear)
    opponent2_headgear_main = models.CharField(
        null=True, max_length=3, choices=MainAbilities
    )
    opponent2_headgear_sub0 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    opponent2_headgear_sub1 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    opponent2_headgear_sub2 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    # clothes
    opponent2_clothes = models.CharField(null=True, max_length=5, choices=Clothes)
    opponent2_clothes_main = models.CharField(
        null=True, max_length=3, choices=MainAbilities
    )
    opponent2_clothes_sub0 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    opponent2_clothes_sub1 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    opponent2_clothes_sub2 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    # shoes
    opponent2_shoes = models.CharField(null=True, max_length=5, choices=Shoes)
    opponent2_shoes_main = models.CharField(
        null=True, max_length=3, choices=MainAbilities
    )
    opponent2_shoes_sub0 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    opponent2_shoes_sub1 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    opponent2_shoes_sub2 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )

    # opponent 3
    # basic stats
    opponent3_splatnet_id = models.CharField(null=True, max_length=16)
    opponent3_name = models.CharField(null=True, max_length=10)
    opponent3_level_star = models.PositiveSmallIntegerField(null=True)
    opponent3_level = models.PositiveSmallIntegerField(null=True)
    opponent3_rank = models.PositiveSmallIntegerField(null=True, choices=Ranks.choices)
    opponent3_weapon = models.CharField(null=True, max_length=4, choices=Weapons)
    opponent3_gender = models.CharField(max_length=4, null=True, choices=gender)
    opponent3_species = models.CharField(max_length=9, null=True, choices=species)
    opponent3_kills = models.PositiveSmallIntegerField(null=True)
    opponent3_deaths = models.PositiveSmallIntegerField(null=True)
    opponent3_assists = models.PositiveSmallIntegerField(null=True)
    opponent3_game_paint_point = models.PositiveSmallIntegerField(null=True)
    opponent3_specials = models.PositiveSmallIntegerField(null=True)
    # headgear
    opponent3_headgear = models.CharField(null=True, max_length=5, choices=Headgear)
    opponent3_headgear_main = models.CharField(
        null=True, max_length=3, choices=MainAbilities
    )
    opponent3_headgear_sub0 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    opponent3_headgear_sub1 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    opponent3_headgear_sub2 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    # clothes
    opponent3_clothes = models.CharField(null=True, max_length=5, choices=Clothes)
    opponent3_clothes_main = models.CharField(
        null=True, max_length=3, choices=MainAbilities
    )
    opponent3_clothes_sub0 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    opponent3_clothes_sub1 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    opponent3_clothes_sub2 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    # shoes
    opponent3_shoes = models.CharField(null=True, max_length=5, choices=Shoes)
    opponent3_shoes_main = models.CharField(
        null=True, max_length=3, choices=MainAbilities
    )
    opponent3_shoes_sub0 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    opponent3_shoes_sub1 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )
    opponent3_shoes_sub2 = models.CharField(
        null=True, max_length=3, choices=SubAbilities
    )

    # @classmethod
    # def create(cls, **kwargs):
    #     data = kwargs["data"]
    #     player_user = kwargs["user"]

    #     if data.get("image_result") is not None:
    #         img_temp0 = NamedTemporaryFile()
    #         img_temp0.write(
    #             base64.b64decode(data.get("image_result").encode(encoding="ascii"))
    #         )
    #         img_temp0.flush()

    #     if data.get("image_gear") is not None:
    #         img_temp1 = NamedTemporaryFile()
    #         img_temp1.write(
    #             base64.b64decode(data.get("image_gear").encode(encoding="ascii"))
    #         )
    #         img_temp1.flush()

    #     if not Battle.objects.filter(
    #         battle_number=data.get("battle_number"), player_user=player_user
    #     ):
    #         battle = cls(
    #             splatnet_json=data.get("splatnet_json"),
    #             stat_ink_json=data.get("stat_ink_json"),
    #             splatnet_upload=data.get("splatnet_upload"),
    #             stat_ink_upload=data.get("stat_ink_upload"),
    #             rule=data.get("rule"),
    #             match_type=data.get("match_type"),
    #             stage=data.get("stage"),
    #             player_weapon=data.get("player_weapon"),
    #             player_rank=data.get("player_rank"),
    #             win=data.get("win"),
    #             has_disconnected_player=data.get("has_disconnected_player"),
    #             time=data.get("time"),
    #             battle_number=data.get("battle_number"),
    #             win_meter=data.get("win_meter"),
    #             tag_id=data.get("tag_id"),
    #             player_x_power=data.get("player_x_power"),
    #             league_point=data.get("league_point"),
    #             splatfest_point=data.get("splatfest_point"),
    #             player_splatfest_title=data.get("player_splatfest_title"),
    #             splatfest_title_after=data.get("splatfest_title_after"),
    #             player_level=data.get("player_level"),
    #             my_team_count=data.get("my_team_count"),
    #             other_team_count=data.get("other_team_count"),
    #             player_kills=data.get("player_kills"),
    #             player_deaths=data.get("player_deaths"),
    #             player_assists=data.get("player_assists"),
    #             player_specials=data.get("player_specials"),
    #             player_game_paint_point=data.get("player_game_paint_point"),
    #             player_splatnet_id=data.get("player_splatnet_id"),
    #             player_name=data.get("player_name"),
    #             player_level_star=data.get("player_level_star"),
    #             elapsed_time=data.get("elapsed_time"),
    #             player_user=player_user,
    #             player_gender=data.get("player_gender"),
    #             player_species=data.get("player_species"),
    #             player_headgear=data.get("player_headgear"),
    #             player_headgear_main=data.get("player_headgear_main"),
    #             player_headgear_sub0=data.get("player_headgear_sub0"),
    #             player_headgear_sub1=data.get("player_headgear_sub1"),
    #             player_headgear_sub2=data.get("player_headgear_sub2"),
    #             player_clothes=data.get("player_clothes"),
    #             player_clothes_main=data.get("player_clothes_main"),
    #             player_clothes_sub0=data.get("player_clothes_sub0"),
    #             player_clothes_sub1=data.get("player_clothes_sub1"),
    #             player_clothes_sub2=data.get("player_clothes_sub2"),
    #             player_shoes=data.get("player_shoes"),
    #             player_shoes_main=data.get("player_shoes_main"),
    #             player_shoes_sub0=data.get("player_shoes_sub0"),
    #             player_shoes_sub1=data.get("player_shoes_sub1"),
    #             player_shoes_sub2=data.get("player_shoes_sub2"),
    #             teammate0_splatnet_id=data.get("teammate0_splatnet_id"),
    #             teammate0_name=data.get("teammate0_name"),
    #             teammate0_level_star=data.get("teammate0_level_star"),
    #             teammate0_level=data.get("teammate0_level"),
    #             teammate0_rank=data.get("teammate0_rank"),
    #             teammate0_weapon=data.get("teammate0_weapon"),
    #             teammate0_gender=data.get("teammate0_gender"),
    #             teammate0_species=data.get("teammate0_species"),
    #             teammate0_kills=data.get("teammate0_kills"),
    #             teammate0_deaths=data.get("teammate0_deaths"),
    #             teammate0_assists=data.get("teammate0_assists"),
    #             teammate0_game_paint_point=data.get("teammate0_game_paint_point"),
    #             teammate0_specials=data.get("teammate0_specials"),
    #             teammate0_headgear=data.get("teammate0_headgear"),
    #             teammate0_headgear_main=data.get("teammate0_headgear_main"),
    #             teammate0_headgear_sub0=data.get("teammate0_headgear_sub0"),
    #             teammate0_headgear_sub1=data.get("teammate0_headgear_sub1"),
    #             teammate0_headgear_sub2=data.get("teammate0_headgear_sub2"),
    #             teammate0_clothes=data.get("teammate0_clothes"),
    #             teammate0_clothes_main=data.get("teammate0_clothes_main"),
    #             teammate0_clothes_sub0=data.get("teammate0_clothes_sub0"),
    #             teammate0_clothes_sub1=data.get("teammate0_clothes_sub1"),
    #             teammate0_clothes_sub2=data.get("teammate0_clothes_sub2"),
    #             teammate0_shoes=data.get("teammate0_shoes"),
    #             teammate0_shoes_main=data.get("teammate0_shoes_main"),
    #             teammate0_shoes_sub0=data.get("teammate0_shoes_sub0"),
    #             teammate0_shoes_sub1=data.get("teammate0_shoes_sub1"),
    #             teammate0_shoes_sub2=data.get("teammate0_shoes_sub2"),
    #             teammate1_splatnet_id=data.get("teammate1_splatnet_id"),
    #             teammate1_name=data.get("teammate1_name"),
    #             teammate1_level_star=data.get("teammate1_level_star"),
    #             teammate1_level=data.get("teammate1_level"),
    #             teammate1_rank=data.get("teammate1_rank"),
    #             teammate1_weapon=data.get("teammate1_weapon"),
    #             teammate1_gender=data.get("teammate1_gender"),
    #             teammate1_species=data.get("teammate1_species"),
    #             teammate1_kills=data.get("teammate1_kills"),
    #             teammate1_deaths=data.get("teammate1_deaths"),
    #             teammate1_assists=data.get("teammate1_assists"),
    #             teammate1_game_paint_point=data.get("teammate1_game_paint_point"),
    #             teammate1_specials=data.get("teammate1_specials"),
    #             teammate1_headgear=data.get("teammate1_headgear"),
    #             teammate1_headgear_main=data.get("teammate1_headgear_main"),
    #             teammate1_headgear_sub0=data.get("teammate1_headgear_sub0"),
    #             teammate1_headgear_sub1=data.get("teammate1_headgear_sub1"),
    #             teammate1_headgear_sub2=data.get("teammate1_headgear_sub2"),
    #             teammate1_clothes=data.get("teammate1_clothes"),
    #             teammate1_clothes_main=data.get("teammate1_clothes_main"),
    #             teammate1_clothes_sub0=data.get("teammate1_clothes_sub0"),
    #             teammate1_clothes_sub1=data.get("teammate1_clothes_sub1"),
    #             teammate1_clothes_sub2=data.get("teammate1_clothes_sub2"),
    #             teammate1_shoes=data.get("teammate1_shoes"),
    #             teammate1_shoes_main=data.get("teammate1_shoes_main"),
    #             teammate1_shoes_sub0=data.get("teammate1_shoes_sub0"),
    #             teammate1_shoes_sub1=data.get("teammate1_shoes_sub1"),
    #             teammate1_shoes_sub2=data.get("teammate1_shoes_sub2"),
    #             teammate2_splatnet_id=data.get("teammate2_splatnet_id"),
    #             teammate2_name=data.get("teammate2_name"),
    #             teammate2_level_star=data.get("teammate2_level_star"),
    #             teammate2_level=data.get("teammate2_level"),
    #             teammate2_rank=data.get("teammate2_rank"),
    #             teammate2_weapon=data.get("teammate2_weapon"),
    #             teammate2_gender=data.get("teammate2_gender"),
    #             teammate2_species=data.get("teammate2_species"),
    #             teammate2_kills=data.get("teammate2_kills"),
    #             teammate2_deaths=data.get("teammate2_deaths"),
    #             teammate2_assists=data.get("teammate2_assists"),
    #             teammate2_game_paint_point=data.get("teammate2_game_paint_point"),
    #             teammate2_specials=data.get("teammate2_specials"),
    #             teammate2_headgear=data.get("teammate2_headgear"),
    #             teammate2_headgear_main=data.get("teammate2_headgear_main"),
    #             teammate2_headgear_sub0=data.get("teammate2_headgear_sub0"),
    #             teammate2_headgear_sub1=data.get("teammate2_headgear_sub1"),
    #             teammate2_headgear_sub2=data.get("teammate2_headgear_sub2"),
    #             teammate2_clothes=data.get("teammate2_clothes"),
    #             teammate2_clothes_main=data.get("teammate2_clothes_main"),
    #             teammate2_clothes_sub0=data.get("teammate2_clothes_sub0"),
    #             teammate2_clothes_sub1=data.get("teammate2_clothes_sub1"),
    #             teammate2_clothes_sub2=data.get("teammate2_clothes_sub2"),
    #             teammate2_shoes=data.get("teammate2_shoes"),
    #             teammate2_shoes_main=data.get("teammate2_shoes_main"),
    #             teammate2_shoes_sub0=data.get("teammate2_shoes_sub0"),
    #             teammate2_shoes_sub1=data.get("teammate2_shoes_sub1"),
    #             teammate2_shoes_sub2=data.get("teammate2_shoes_sub2"),
    #             opponent0_splatnet_id=data.get("opponent0_splatnet_id"),
    #             opponent0_name=data.get("opponent0_name"),
    #             opponent0_level_star=data.get("opponent0_level_star"),
    #             opponent0_level=data.get("opponent0_level"),
    #             opponent0_rank=data.get("opponent0_rank"),
    #             opponent0_weapon=data.get("opponent0_weapon"),
    #             opponent0_gender=data.get("opponent0_gender"),
    #             opponent0_species=data.get("opponent0_species"),
    #             opponent0_kills=data.get("opponent0_kills"),
    #             opponent0_deaths=data.get("opponent0_deaths"),
    #             opponent0_assists=data.get("opponent0_assists"),
    #             opponent0_game_paint_point=data.get("opponent0_game_paint_point"),
    #             opponent0_specials=data.get("opponent0_specials"),
    #             opponent0_headgear=data.get("opponent0_headgear"),
    #             opponent0_headgear_main=data.get("opponent0_headgear_main"),
    #             opponent0_headgear_sub0=data.get("opponent0_headgear_sub0"),
    #             opponent0_headgear_sub1=data.get("opponent0_headgear_sub1"),
    #             opponent0_headgear_sub2=data.get("opponent0_headgear_sub2"),
    #             opponent0_clothes=data.get("opponent0_clothes"),
    #             opponent0_clothes_main=data.get("opponent0_clothes_main"),
    #             opponent0_clothes_sub0=data.get("opponent0_clothes_sub0"),
    #             opponent0_clothes_sub1=data.get("opponent0_clothes_sub1"),
    #             opponent0_clothes_sub2=data.get("opponent0_clothes_sub2"),
    #             opponent0_shoes=data.get("opponent0_shoes"),
    #             opponent0_shoes_main=data.get("opponent0_shoes_main"),
    #             opponent0_shoes_sub0=data.get("opponent0_shoes_sub0"),
    #             opponent0_shoes_sub1=data.get("opponent0_shoes_sub1"),
    #             opponent0_shoes_sub2=data.get("opponent0_shoes_sub2"),
    #             opponent1_splatnet_id=data.get("opponent1_splatnet_id"),
    #             opponent1_name=data.get("opponent1_name"),
    #             opponent1_level_star=data.get("opponent1_level_star"),
    #             opponent1_level=data.get("opponent1_level"),
    #             opponent1_rank=data.get("opponent1_rank"),
    #             opponent1_weapon=data.get("opponent1_weapon"),
    #             opponent1_gender=data.get("opponent1_gender"),
    #             opponent1_species=data.get("opponent1_species"),
    #             opponent1_kills=data.get("opponent1_kills"),
    #             opponent1_deaths=data.get("opponent1_deaths"),
    #             opponent1_assists=data.get("opponent1_assists"),
    #             opponent1_game_paint_point=data.get("opponent1_game_paint_point"),
    #             opponent1_specials=data.get("opponent1_specials"),
    #             opponent1_headgear=data.get("opponent1_headgear"),
    #             opponent1_headgear_main=data.get("opponent1_headgear_main"),
    #             opponent1_headgear_sub0=data.get("opponent1_headgear_sub0"),
    #             opponent1_headgear_sub1=data.get("opponent1_headgear_sub1"),
    #             opponent1_headgear_sub2=data.get("opponent1_headgear_sub2"),
    #             opponent1_clothes=data.get("opponent1_clothes"),
    #             opponent1_clothes_main=data.get("opponent1_clothes_main"),
    #             opponent1_clothes_sub0=data.get("opponent1_clothes_sub0"),
    #             opponent1_clothes_sub1=data.get("opponent1_clothes_sub1"),
    #             opponent1_clothes_sub2=data.get("opponent1_clothes_sub2"),
    #             opponent1_shoes=data.get("opponent1_shoes"),
    #             opponent1_shoes_main=data.get("opponent1_shoes_main"),
    #             opponent1_shoes_sub0=data.get("opponent1_shoes_sub0"),
    #             opponent1_shoes_sub1=data.get("opponent1_shoes_sub1"),
    #             opponent1_shoes_sub2=data.get("opponent1_shoes_sub2"),
    #             opponent2_splatnet_id=data.get("opponent2_splatnet_id"),
    #             opponent2_name=data.get("opponent2_name"),
    #             opponent2_level_star=data.get("opponent2_level_star"),
    #             opponent2_level=data.get("opponent2_level"),
    #             opponent2_rank=data.get("opponent2_rank"),
    #             opponent2_weapon=data.get("opponent2_weapon"),
    #             opponent2_gender=data.get("opponent2_gender"),
    #             opponent2_species=data.get("opponent2_species"),
    #             opponent2_kills=data.get("opponent2_kills"),
    #             opponent2_deaths=data.get("opponent2_deaths"),
    #             opponent2_assists=data.get("opponent2_assists"),
    #             opponent2_game_paint_point=data.get("opponent2_game_paint_point"),
    #             opponent2_specials=data.get("opponent2_specials"),
    #             opponent2_headgear=data.get("opponent2_headgear"),
    #             opponent2_headgear_main=data.get("opponent2_headgear_main"),
    #             opponent2_headgear_sub0=data.get("opponent2_headgear_sub0"),
    #             opponent2_headgear_sub1=data.get("opponent2_headgear_sub1"),
    #             opponent2_headgear_sub2=data.get("opponent2_headgear_sub2"),
    #             opponent2_clothes=data.get("opponent2_clothes"),
    #             opponent2_clothes_main=data.get("opponent2_clothes_main"),
    #             opponent2_clothes_sub0=data.get("opponent2_clothes_sub0"),
    #             opponent2_clothes_sub1=data.get("opponent2_clothes_sub1"),
    #             opponent2_clothes_sub2=data.get("opponent2_clothes_sub2"),
    #             opponent2_shoes=data.get("opponent2_shoes"),
    #             opponent2_shoes_main=data.get("opponent2_shoes_main"),
    #             opponent2_shoes_sub0=data.get("opponent2_shoes_sub0"),
    #             opponent2_shoes_sub1=data.get("opponent2_shoes_sub1"),
    #             opponent2_shoes_sub2=data.get("opponent2_shoes_sub2"),
    #             opponent3_splatnet_id=data.get("opponent3_splatnet_id"),
    #             opponent3_name=data.get("opponent3_name"),
    #             opponent3_level_star=data.get("opponent3_level_star"),
    #             opponent3_level=data.get("opponent3_level"),
    #             opponent3_rank=data.get("opponent3_rank"),
    #             opponent3_weapon=data.get("opponent3_weapon"),
    #             opponent3_gender=data.get("opponent3_gender"),
    #             opponent3_species=data.get("opponent3_species"),
    #             opponent3_kills=data.get("opponent3_kills"),
    #             opponent3_deaths=data.get("opponent3_deaths"),
    #             opponent3_assists=data.get("opponent3_assists"),
    #             opponent3_game_paint_point=data.get("opponent3_game_paint_point"),
    #             opponent3_specials=data.get("opponent3_specials"),
    #             opponent3_headgear=data.get("opponent3_headgear"),
    #             opponent3_headgear_main=data.get("opponent3_headgear_main"),
    #             opponent3_headgear_sub0=data.get("opponent3_headgear_sub0"),
    #             opponent3_headgear_sub1=data.get("opponent3_headgear_sub1"),
    #             opponent3_headgear_sub2=data.get("opponent3_headgear_sub2"),
    #             opponent3_clothes=data.get("opponent3_clothes"),
    #             opponent3_clothes_main=data.get("opponent3_clothes_main"),
    #             opponent3_clothes_sub0=data.get("opponent3_clothes_sub0"),
    #             opponent3_clothes_sub1=data.get("opponent3_clothes_sub1"),
    #             opponent3_clothes_sub2=data.get("opponent3_clothes_sub2"),
    #             opponent3_shoes=data.get("opponent3_shoes"),
    #             opponent3_shoes_main=data.get("opponent3_shoes_main"),
    #             opponent3_shoes_sub0=data.get("opponent3_shoes_sub0"),
    #             opponent3_shoes_sub1=data.get("opponent3_shoes_sub1"),
    #             opponent3_shoes_sub2=data.get("opponent3_shoes_sub2"),
    #         )
    #         battle.save()
    #         if data.get("image_result") is not None:
    #             battle.image_result.save(
    #                 "data/{}_image_result.png".format(battle.id),
    #                 File(img_temp0),
    #                 save=data.get("True"),
    #             )
    #         if data.get("image_gear") is not None:
    #             battle.image_gear.save(
    #                 "data/{}_image_gear.png".format(battle.id),
    #                 File(img_temp1),
    #                 save=data.get("True"),
    #             )
    #         return battle
    #     if Battle.objects.filter(
    #         battle_number=data.get("battle_number"), player_user=player_user
    #     )[0].splatnet_upload is None and data.get("splatnet_upload"):
    #         battle = Battle.objects.filter(
    #             battle_number=data.get("battle_number"), player_user=player_user
    #         )[0]
    #         battle.splatnet_upload = True
    #         battle.rule = data.get("rule")
    #         battle.match_type = data.get("match_type")
    #         battle.stage = data.get("stage")
    #         battle.win = data.get("win")
    #         battle.has_disconnected_player = data.get("has_disconnected_player")
    #         battle.time = data.get("time")
    #         battle.win_meter = data.get("win_meter")
    #         battle.my_team_count = data.get("my_team_count")
    #         battle.other_team_count = data.get("other_team_count")
    #         battle.elapsed_time = data.get("elapsed_time")

    #         # league battle stuff
    #         battle.tag_id = data.get("tag_id")
    #         battle.league_point = data.get("league_point")

    #         # splatfest
    #         battle.splatfest_point = data.get("splatfest_point")
    #         battle.splatfest_title_after = data.get("splatfest_title_after")

    #         # player
    #         # basic stats
    #         battle.player_splatnet_id = data.get("player_splatnet_id")
    #         battle.player_name = data.get("player_name")
    #         battle.player_weapon = data.get("player_weapon")
    #         battle.player_rank = data.get("player_rank")
    #         battle.player_splatfest_title = data.get("player_splatfest_title")
    #         battle.player_level_star = data.get("player_level_star")
    #         battle.player_level = data.get("player_level")
    #         battle.player_kills = data.get("player_kills")
    #         battle.player_deaths = data.get("player_deaths")
    #         battle.player_assists = data.get("player_assists")
    #         battle.player_specials = data.get("player_specials")
    #         battle.player_game_paint_point = data.get("player_game_paint_point")
    #         battle.player_gender = data.get("player_gender")
    #         battle.player_species = data.get("player_species")
    #         battle.player_x_power = data.get("player_x_power")
    #         # headgear
    #         battle.player_headgear = data.get("player_headgear")
    #         battle.player_headgear_main = data.get("player_headgear_main")
    #         battle.player_headgear_sub0 = data.get("player_headgear_sub0")
    #         battle.player_headgear_sub1 = data.get("player_headgear_sub1")
    #         battle.player_headgear_sub2 = data.get("player_headgear_sub2")
    #         # clothes
    #         battle.player_clothes = data.get("player_clothes")
    #         battle.player_clothes_main = data.get("player_clothes_main")
    #         battle.player_clothes_sub0 = data.get("player_clothes_sub0")
    #         battle.player_clothes_sub1 = data.get("player_clothes_sub1")
    #         battle.player_clothes_sub2 = data.get("player_clothes_sub2")
    #         # shoes
    #         battle.player_shoes = data.get("player_shoes")
    #         battle.player_shoes_main = data.get("player_shoes_main")
    #         battle.player_shoes_sub0 = data.get("player_shoes_sub0")
    #         battle.player_shoes_sub1 = data.get("player_shoes_sub1")
    #         battle.player_shoes_sub2 = data.get("player_shoes_sub2")

    #         # teammate0
    #         battle.teammate0_splatnet_id = data.get("teammate0_splatnet_id")
    #         battle.teammate0_name = data.get("teammate0_name")
    #         battle.teammate0_weapon = data.get("teammate0_weapon")
    #         battle.teammate0_rank = data.get("teammate0_rank")
    #         battle.teammate0_level_star = data.get("teammate0_level_star")
    #         battle.teammate0_level = data.get("teammate0_level")
    #         battle.teammate0_kills = data.get("teammate0_kills")
    #         battle.teammate0_deaths = data.get("teammate0_deaths")
    #         battle.teammate0_assists = data.get("teammate0_assists")
    #         battle.teammate0_specials = data.get("teammate0_specials")
    #         battle.teammate0_game_paint_point = data.get("teammate0_game_paint_point")
    #         battle.teammate0_gender = data.get("teammate0_gender")
    #         battle.teammate0_species = data.get("teammate0_species")
    #         # headgear
    #         battle.teammate0_headgear = data.get("teammate0_headgear")
    #         battle.teammate0_headgear_main = data.get("teammate0_headgear_main")
    #         battle.teammate0_headgear_sub0 = data.get("teammate0_headgear_sub0")
    #         battle.teammate0_headgear_sub1 = data.get("teammate0_headgear_sub1")
    #         battle.teammate0_headgear_sub2 = data.get("teammate0_headgear_sub2")
    #         # clothes
    #         battle.teammate0_clothes = data.get("teammate0_clothes")
    #         battle.teammate0_clothes_main = data.get("teammate0_clothes_main")
    #         battle.teammate0_clothes_sub0 = data.get("teammate0_clothes_sub0")
    #         battle.teammate0_clothes_sub1 = data.get("teammate0_clothes_sub1")
    #         battle.teammate0_clothes_sub2 = data.get("teammate0_clothes_sub2")
    #         # shoes
    #         battle.teammate0_shoes = data.get("teammate0_shoes")
    #         battle.teammate0_shoes_main = data.get("teammate0_shoes_main")
    #         battle.teammate0_shoes_sub0 = data.get("teammate0_shoes_sub0")
    #         battle.teammate0_shoes_sub1 = data.get("teammate0_shoes_sub1")
    #         battle.teammate0_shoes_sub2 = data.get("teammate0_shoes_sub2")

    #         # teammate1
    #         battle.teammate1_splatnet_id = data.get("teammate1_splatnet_id")
    #         battle.teammate1_name = data.get("teammate1_name")
    #         battle.teammate1_weapon = data.get("teammate1_weapon")
    #         battle.teammate1_rank = data.get("teammate1_rank")
    #         battle.teammate1_level_star = data.get("teammate1_level_star")
    #         battle.teammate1_level = data.get("teammate1_level")
    #         battle.teammate1_kills = data.get("teammate1_kills")
    #         battle.teammate1_deaths = data.get("teammate1_deaths")
    #         battle.teammate1_assists = data.get("teammate1_assists")
    #         battle.teammate1_specials = data.get("teammate1_specials")
    #         battle.teammate1_game_paint_point = data.get("teammate1_game_paint_point")
    #         battle.teammate1_gender = data.get("teammate1_gender")
    #         battle.teammate1_species = data.get("teammate1_species")
    #         # headgear
    #         battle.teammate1_headgear = data.get("teammate1_headgear")
    #         battle.teammate1_headgear_main = data.get("teammate1_headgear_main")
    #         battle.teammate1_headgear_sub0 = data.get("teammate1_headgear_sub0")
    #         battle.teammate1_headgear_sub1 = data.get("teammate1_headgear_sub1")
    #         battle.teammate1_headgear_sub2 = data.get("teammate1_headgear_sub2")
    #         # clothes
    #         battle.teammate1_clothes = data.get("teammate1_clothes")
    #         battle.teammate1_clothes_main = data.get("teammate1_clothes_main")
    #         battle.teammate1_clothes_sub0 = data.get("teammate1_clothes_sub0")
    #         battle.teammate1_clothes_sub1 = data.get("teammate1_clothes_sub1")
    #         battle.teammate1_clothes_sub2 = data.get("teammate1_clothes_sub2")
    #         # shoes
    #         battle.teammate1_shoes = data.get("teammate1_shoes")
    #         battle.teammate1_shoes_main = data.get("teammate1_shoes_main")
    #         battle.teammate1_shoes_sub0 = data.get("teammate1_shoes_sub0")
    #         battle.teammate1_shoes_sub1 = data.get("teammate1_shoes_sub1")
    #         battle.teammate1_shoes_sub2 = data.get("teammate1_shoes_sub2")

    #         # teammate2
    #         battle.teammate2_splatnet_id = data.get("teammate2_splatnet_id")
    #         battle.teammate2_name = data.get("teammate2_name")
    #         battle.teammate2_weapon = data.get("teammate2_weapon")
    #         battle.teammate2_rank = data.get("teammate2_rank")
    #         battle.teammate2_level_star = data.get("teammate2_level_star")
    #         battle.teammate2_level = data.get("teammate2_level")
    #         battle.teammate2_kills = data.get("teammate2_kills")
    #         battle.teammate2_deaths = data.get("teammate2_deaths")
    #         battle.teammate2_assists = data.get("teammate2_assists")
    #         battle.teammate2_specials = data.get("teammate2_specials")
    #         battle.teammate2_game_paint_point = data.get("teammate2_game_paint_point")
    #         battle.teammate2_gender = data.get("teammate2_gender")
    #         battle.teammate2_species = data.get("teammate2_species")
    #         # headgear
    #         battle.teammate2_headgear = data.get("teammate2_headgear")
    #         battle.teammate2_headgear_main = data.get("teammate2_headgear_main")
    #         battle.teammate2_headgear_sub0 = data.get("teammate2_headgear_sub0")
    #         battle.teammate2_headgear_sub1 = data.get("teammate2_headgear_sub1")
    #         battle.teammate2_headgear_sub2 = data.get("teammate2_headgear_sub2")
    #         # clothes
    #         battle.teammate2_clothes = data.get("teammate2_clothes")
    #         battle.teammate2_clothes_main = data.get("teammate2_clothes_main")
    #         battle.teammate2_clothes_sub0 = data.get("teammate2_clothes_sub0")
    #         battle.teammate2_clothes_sub1 = data.get("teammate2_clothes_sub1")
    #         battle.teammate2_clothes_sub2 = data.get("teammate2_clothes_sub2")
    #         # shoes
    #         battle.teammate2_shoes = data.get("teammate2_shoes")
    #         battle.teammate2_shoes_main = data.get("teammate2_shoes_main")
    #         battle.teammate2_shoes_sub0 = data.get("teammate2_shoes_sub0")
    #         battle.teammate2_shoes_sub1 = data.get("teammate2_shoes_sub1")
    #         battle.teammate2_shoes_sub2 = data.get("teammate2_shoes_sub2")

    #         # opponent0
    #         battle.opponent0_splatnet_id = data.get("opponent0_splatnet_id")
    #         battle.opponent0_name = data.get("opponent0_name")
    #         battle.opponent0_weapon = data.get("opponent0_weapon")
    #         battle.opponent0_rank = data.get("opponent0_rank")
    #         battle.opponent0_level_star = data.get("opponent0_level_star")
    #         battle.opponent0_level = data.get("opponent0_level")
    #         battle.opponent0_kills = data.get("opponent0_kills")
    #         battle.opponent0_deaths = data.get("opponent0_deaths")
    #         battle.opponent0_assists = data.get("opponent0_assists")
    #         battle.opponent0_specials = data.get("opponent0_specials")
    #         battle.opponent0_game_paint_point = data.get("opponent0_game_paint_point")
    #         battle.opponent0_gender = data.get("opponent0_gender")
    #         battle.opponent0_species = data.get("opponent0_species")
    #         # headgear
    #         battle.opponent0_headgear = data.get("opponent0_headgear")
    #         battle.opponent0_headgear_main = data.get("opponent0_headgear_main")
    #         battle.opponent0_headgear_sub0 = data.get("opponent0_headgear_sub0")
    #         battle.opponent0_headgear_sub1 = data.get("opponent0_headgear_sub1")
    #         battle.opponent0_headgear_sub2 = data.get("opponent0_headgear_sub2")
    #         # clothes
    #         battle.opponent0_clothes = data.get("opponent0_clothes")
    #         battle.opponent0_clothes_main = data.get("opponent0_clothes_main")
    #         battle.opponent0_clothes_sub0 = data.get("opponent0_clothes_sub0")
    #         battle.opponent0_clothes_sub1 = data.get("opponent0_clothes_sub1")
    #         battle.opponent0_clothes_sub2 = data.get("opponent0_clothes_sub2")
    #         # shoes
    #         battle.opponent0_shoes = data.get("opponent0_shoes")
    #         battle.opponent0_shoes_main = data.get("opponent0_shoes_main")
    #         battle.opponent0_shoes_sub0 = data.get("opponent0_shoes_sub0")
    #         battle.opponent0_shoes_sub1 = data.get("opponent0_shoes_sub1")
    #         battle.opponent0_shoes_sub2 = data.get("opponent0_shoes_sub2")

    #         # opponent1
    #         battle.opponent1_splatnet_id = data.get("opponent1_splatnet_id")
    #         battle.opponent1_name = data.get("opponent1_name")
    #         battle.opponent1_weapon = data.get("opponent1_weapon")
    #         battle.opponent1_rank = data.get("opponent1_rank")
    #         battle.opponent1_level_star = data.get("opponent1_level_star")
    #         battle.opponent1_level = data.get("opponent1_level")
    #         battle.opponent1_kills = data.get("opponent1_kills")
    #         battle.opponent1_deaths = data.get("opponent1_deaths")
    #         battle.opponent1_assists = data.get("opponent1_assists")
    #         battle.opponent1_specials = data.get("opponent1_specials")
    #         battle.opponent1_game_paint_point = data.get("opponent1_game_paint_point")
    #         battle.opponent1_gender = data.get("opponent1_gender")
    #         battle.opponent1_species = data.get("opponent1_species")
    #         # headgear
    #         battle.opponent1_headgear = data.get("opponent1_headgear")
    #         battle.opponent1_headgear_main = data.get("opponent1_headgear_main")
    #         battle.opponent1_headgear_sub0 = data.get("opponent1_headgear_sub0")
    #         battle.opponent1_headgear_sub1 = data.get("opponent1_headgear_sub1")
    #         battle.opponent1_headgear_sub2 = data.get("opponent1_headgear_sub2")
    #         # clothes
    #         battle.opponent1_clothes = data.get("opponent1_clothes")
    #         battle.opponent1_clothes_main = data.get("opponent1_clothes_main")
    #         battle.opponent1_clothes_sub0 = data.get("opponent1_clothes_sub0")
    #         battle.opponent1_clothes_sub1 = data.get("opponent1_clothes_sub1")
    #         battle.opponent1_clothes_sub2 = data.get("opponent1_clothes_sub2")
    #         # shoes
    #         battle.opponent1_shoes = data.get("opponent1_shoes")
    #         battle.opponent1_shoes_main = data.get("opponent1_shoes_main")
    #         battle.opponent1_shoes_sub0 = data.get("opponent1_shoes_sub0")
    #         battle.opponent1_shoes_sub1 = data.get("opponent1_shoes_sub1")
    #         battle.opponent1_shoes_sub2 = data.get("opponent1_shoes_sub2")

    #         # opponent2
    #         battle.opponent2_splatnet_id = data.get("opponent2_splatnet_id")
    #         battle.opponent2_name = data.get("opponent2_name")
    #         battle.opponent2_weapon = data.get("opponent2_weapon")
    #         battle.opponent2_rank = data.get("opponent2_rank")
    #         battle.opponent2_level_star = data.get("opponent2_level_star")
    #         battle.opponent2_level = data.get("opponent2_level")
    #         battle.opponent2_kills = data.get("opponent2_kills")
    #         battle.opponent2_deaths = data.get("opponent2_deaths")
    #         battle.opponent2_assists = data.get("opponent2_assists")
    #         battle.opponent2_specials = data.get("opponent2_specials")
    #         battle.opponent2_game_paint_point = data.get("opponent2_game_paint_point")
    #         battle.opponent2_gender = data.get("opponent2_gender")
    #         battle.opponent2_species = data.get("opponent2_species")
    #         # headgear
    #         battle.opponent2_headgear = data.get("opponent2_headgear")
    #         battle.opponent2_headgear_main = data.get("opponent2_headgear_main")
    #         battle.opponent2_headgear_sub0 = data.get("opponent2_headgear_sub0")
    #         battle.opponent2_headgear_sub1 = data.get("opponent2_headgear_sub1")
    #         battle.opponent2_headgear_sub2 = data.get("opponent2_headgear_sub2")
    #         # clothes
    #         battle.opponent2_clothes = data.get("opponent2_clothes")
    #         battle.opponent2_clothes_main = data.get("opponent2_clothes_main")
    #         battle.opponent2_clothes_sub0 = data.get("opponent2_clothes_sub0")
    #         battle.opponent2_clothes_sub1 = data.get("opponent2_clothes_sub1")
    #         battle.opponent2_clothes_sub2 = data.get("opponent2_clothes_sub2")
    #         # shoes
    #         battle.opponent2_shoes = data.get("opponent2_shoes")
    #         battle.opponent2_shoes_main = data.get("opponent2_shoes_main")
    #         battle.opponent2_shoes_sub0 = data.get("opponent2_shoes_sub0")
    #         battle.opponent2_shoes_sub1 = data.get("opponent2_shoes_sub1")
    #         battle.opponent2_shoes_sub2 = data.get("opponent2_shoes_sub2")

    #         # opponent3
    #         battle.opponent3_splatnet_id = data.get("opponent3_splatnet_id")
    #         battle.opponent3_name = data.get("opponent3_name")
    #         battle.opponent3_weapon = data.get("opponent3_weapon")
    #         battle.opponent3_rank = data.get("opponent3_rank")
    #         battle.opponent3_level_star = data.get("opponent3_level_star")
    #         battle.opponent3_level = data.get("opponent3_level")
    #         battle.opponent3_kills = data.get("opponent3_kills")
    #         battle.opponent3_deaths = data.get("opponent3_deaths")
    #         battle.opponent3_assists = data.get("opponent3_assists")
    #         battle.opponent3_specials = data.get("opponent3_specials")
    #         battle.opponent3_game_paint_point = data.get("opponent3_game_paint_point")
    #         battle.opponent3_gender = data.get("opponent3_gender")
    #         battle.opponent3_species = data.get("opponent3_species")
    #         # headgear
    #         battle.opponent3_headgear = data.get("opponent3_headgear")
    #         battle.opponent3_headgear_main = data.get("opponent3_headgear_main")
    #         battle.opponent3_headgear_sub0 = data.get("opponent3_headgear_sub0")
    #         battle.opponent3_headgear_sub1 = data.get("opponent3_headgear_sub1")
    #         battle.opponent3_headgear_sub2 = data.get("opponent3_headgear_sub2")
    #         # clothes
    #         battle.opponent3_clothes = data.get("opponent3_clothes")
    #         battle.opponent3_clothes_main = data.get("opponent3_clothes_main")
    #         battle.opponent3_clothes_sub0 = data.get("opponent3_clothes_sub0")
    #         battle.opponent3_clothes_sub1 = data.get("opponent3_clothes_sub1")
    #         battle.opponent3_clothes_sub2 = data.get("opponent3_clothes_sub2")
    #         # shoes
    #         battle.opponent3_shoes = data.get("opponent3_shoes")
    #         battle.opponent3_shoes_main = data.get("opponent3_shoes_main")
    #         battle.opponent3_shoes_sub0 = data.get("opponent3_shoes_sub0")
    #         battle.opponent3_shoes_sub1 = data.get("opponent3_shoes_sub1")
    #         battle.opponent3_shoes_sub2 = data.get("opponent3_shoes_sub2")
    #         battle.save()

    #     return Battle.objects.filter(
    #         battle_number=data.get("battle_number"), player_user=player_user
    #     )[0]

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
