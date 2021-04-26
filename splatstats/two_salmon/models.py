from django.db import models
from django.utils.translation import gettext_lazy as _
import sys

sys.path.append("..")
from models import Species, Gender

# Create your models here.
class Shift(models.Model):
    class Weapons(models.TextChoices):
        bold = "0", _("Sploosh-o-matic")
        wakaba = "10", _("Splattershot Jr.")
        sharp = "20", _("Splash-o-matic")
        promodeler_mg = "30", _("Aerospray MG")
        sshooter = "40", _("Splattershot")
        five2gal = "50", _(".52 Gal")
        nzap85 = "60", _("N-ZAP '85")
        prime = "70", _("Splattershot Pro")
        nine6gal = "80", _(".96 Gal")
        jetsweeper = "90", _("Jet Squelcher")
        nova = "200", _("Luna Blaster")
        hotblaster = "210", _("Blaster")
        longblaster = "220", _("Range Blaster")
        clashblaster = "230", _("Clash Blaster")
        rapid = "240", _("Rapid Blaster")
        rapid_elite = "250", _("Rapid Blaster Pro")
        l3reelgun = "300", _("L-3 Nozzlenose")
        h3reelgun = "310", _("H-3 Nozzlenose")
        bottlegeyser = "400", _("Squeezer")
        carbon = "1000", _("Carbon Roller")
        splatroller = "1010", _("Splat Roller")
        dynamo = "1020", _("Dynamo Roller")
        variableroller = "1030", _("Flingza Roller")
        pablo = "1100", _("Inkbrush")
        hokusai = "1110", _("Octobrush")
        squiclean_a = "2000", _("Classic Squiffer")
        splatcharger = "2010", _("Splat Charger")
        splatscope = "2020", _("Splatterscope")
        liter4k = "2030", _("E-liter 4K")
        liter4k_scope = "2040", _("E-liter 4K Scope")
        bamboo14mk1 = "2050", _("Bamboozler 14 Mk I")
        soytuber = "2060", _("Goo Tuber")
        bucketslosher = "3000", _("Slosher")
        hissen = "3010", _("Tri-Slosher")
        screwslosher = "3020", _("Sloshing Machine")
        furo = "3030", _("Bloblobber")
        explosher = "3040", _("Explosher")
        splatspinner = "4000", _("Mini Splatling")
        barrelspinner = "4010", _("Heavy Splatling")
        hydra = "4020", _("Hydra Splatling")
        kugelschreiber = "4030", _("Ballpoint Splatling")
        sputtery = "5000", _("Dapple Dualies")
        maneuver = "5010", _("Splat Dualies")
        kelvin525 = "5020", _("Glooga Dualies")
        dualsweeper = "5030", _("Dualie Squelchers")
        quadhopper_black = "5040", _("Dark Tetra Dualies")
        parashelter = "6000", _("Splat Brella")
        campingshelter = "6010", _("Tenta Brella")
        spygadget = "6020", _("Undercover Brella")
        grizblast = "20000", _("Grizzco Blaster")
        grizbrella = "20010", _("Grizzco Brella")
        grizcharger = "20020", _("Grizzco Charger")
        grizslosher = "20030", _("Grizzco Slosher")

    class Stages(models.TextChoices):
        smokeyard = "Salmonid Smokeyard"
        ark = "Ruins of Ark Polaris"
        grounds = "Spwaning Grounds"
        bay = "Marooner's Bay"
        outpust = "Lost Outpost"
