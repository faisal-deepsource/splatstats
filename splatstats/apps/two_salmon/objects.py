class Wave:
    def __init__(
        self, num, event, water_level, quota, delivers, appearances, power_eggs
    ):
        self.num = num
        self.event = event
        self.water_level = water_level
        self.quota = quota
        self.delivers = delivers
        self.appearances = appearances
        self.power_eggs = power_eggs


class Player:
    def __init__(
        self,
        w1_weapon,
        w2_weapon,
        w3_weapon,
        special,
        w1_specials,
        w2_specials,
        w3_specials,
        rescues,
        deaths,
        golden,
        power,
    ):
        self.w1_weapon = w1_weapon
        self.w2_weapon = w2_weapon
        self.w3_weapon = w3_weapon
        self.special = special
        self.w1_specials = w1_specials
        self.w2_specials = w2_specials
        self.w3_specials = w3_specials
        self.rescues = rescues
        self.deaths = deaths
        self.golden = golden
        self.power = power


class Boss:
    def __init__(
        self,
        name,
        appearances,
        player_kills,
        teammate0_kills,
        teammate1_kills,
        teammate2_kills,
    ):
        self.name = name
        self.appearances = appearances or 0
        self.player_kills = "{} kills".format(player_kills or 0)
        self.teammate0_kills = "{} kills".format(teammate0_kills or 0)
        self.teammate1_kills = "{} kills".format(teammate1_kills or 0)
        self.teammate2_kills = "{} kills".format(teammate2_kills or 0)
