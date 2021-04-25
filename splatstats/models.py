from django.db import models
from django.utils.translation import gettext_lazy as _


class Weapons(models.IntegerChoices):
    bold = "Sploosh-o-matic"
    bold_neo = "Neo Sploosh-o-matic"
    bold_7 = "Sploosh-o-matic 7"
    wakaba = "Splattershot Jr."
    momiji = "Custom Splattershot Jr."
    ochiba = "Kensa Splattershot Jr."
    sharp = "Splash-o-matic"
    sharp_neo = "Neo Splash-o-matic"
    promodeler_mg = "Aerospray MG"
    promodeler_rg = "Aerospray RG"
    promodeler_pg = "Aerospray PG"
    sshooter = "Splattershot"
    sshooter_collabo = "Tentatek Splattershot"
    sshooter_becchu = "Kensa Splattershot"
    heroshooter_replica = "Hero Shot Replica"
    octoshooter_replica = "Octo Shot Replica"
    five2gal = ".52 Gal"
    five2gal_deco = ".52 Gal Deco"
    five2gal_becchu = "Kensa .52 Gal"
