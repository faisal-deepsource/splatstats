from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from rest_framework import views, status, permissions
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from time import gmtime
from time import strftime
from .forms import BattleForm
import base64
from .models import Battle
from .objects import Player
from django.templatetags.static import static
import json
from datetime import datetime


def index(request):
    latest_battles = Battle.objects.order_by("-time")
    results = []
    time_vals = []
    player_weapons = []
    for battle in latest_battles:
        results.append("Win" if battle.win else "Lose")
        time_vals.append(
            datetime.utcfromtimestamp(battle.time).strftime("%Y-%m-%d %H:%M:%S")
        )
        player_weapons.append(
            static("two_battles/weapons/" + battle.player_weapon + ".png")
        )
    context = {
        "my_list": zip(
            latest_battles,
            results,
            time_vals,
            player_weapons,
        )
    }
    return render(request, "two_battles/index.html", context)


def detail(request, id):
    battle = get_object_or_404(Battle, pk=id)
    player_k_a = battle.player_kills + battle.player_assists
    player_weapon = static("two_battles/weapons/" + battle.player_weapon + ".png")
    player_headgear_main = static(
        "two_battles/abilities/mains/" + battle.player_headgear_main + ".png"
    )
    if battle.player_headgear_sub0 is not None:
        player_headgear_sub0 = static(
            "two_battles/abilities/subs/" + battle.player_headgear_sub0 + ".png"
        )
        if battle.player_headgear_sub1 is not None:
            player_headgear_sub1 = static(
                "two_battles/abilities/subs/" + battle.player_headgear_sub1 + ".png"
            )
            if battle.player_headgear_sub2 is not None:
                player_headgear_sub2 = static(
                    "two_battles/abilities/subs/" + battle.player_headgear_sub2 + ".png"
                )
            else:
                player_headgear_sub2 = None
        else:
            player_headgear_sub1 = None
            player_headgear_sub2 = None
    else:
        player_headgear_sub0 = None
        player_headgear_sub1 = None
        player_headgear_sub2 = None
    player_clothes_main = static(
        "two_battles/abilities/mains/" + battle.player_clothes_main + ".png"
    )
    if battle.player_clothes_sub0 is not None:
        player_clothes_sub0 = static(
            "two_battles/abilities/subs/" + battle.player_clothes_sub0 + ".png"
        )
        if battle.player_clothes_sub1 is not None:
            player_clothes_sub1 = static(
                "two_battles/abilities/subs/" + battle.player_clothes_sub1 + ".png"
            )
            if battle.player_clothes_sub2 is not None:
                player_clothes_sub2 = static(
                    "two_battles/abilities/subs/" + battle.player_clothes_sub2 + ".png"
                )
            else:
                player_clothes_sub2 = None
        else:
            player_clothes_sub1 = None
            player_clothes_sub2 = None
    else:
        player_clothes_sub0 = None
        player_clothes_sub1 = None
        player_clothes_sub2 = None
    player_shoes_main = static(
        "two_battles/abilities/mains/" + battle.player_shoes_main + ".png"
    )
    if battle.player_shoes_sub0 is not None:
        player_shoes_sub0 = static(
            "two_battles/abilities/subs/" + battle.player_shoes_sub0 + ".png"
        )
        if battle.player_shoes_sub1 is not None:
            player_shoes_sub1 = static(
                "two_battles/abilities/subs/" + battle.player_shoes_sub1 + ".png"
            )
            if battle.player_shoes_sub2 is not None:
                player_shoes_sub2 = static(
                    "two_battles/abilities/subs/" + battle.player_shoes_sub2 + ".png"
                )
            else:
                player_shoes_sub2 = None
        else:
            player_shoes_sub1 = None
            player_shoes_sub2 = None
    else:
        player_shoes_sub0 = None
        player_shoes_sub1 = None
        player_shoes_sub2 = None
    player = Player(
        "row1",
        battle.player_name,
        player_weapon,
        battle.get_player_weapon_display(),
        battle.player_level_star,
        battle.player_level,
        battle.get_player_rank_display(),
        battle.player_game_paint_point,
        player_k_a,
        battle.player_assists,
        battle.player_specials,
        battle.player_kills,
        battle.player_deaths,
        player_headgear_main,
        player_headgear_sub0,
        player_headgear_sub1,
        player_headgear_sub2,
        player_clothes_main,
        player_clothes_sub0,
        player_clothes_sub1,
        player_clothes_sub2,
        player_shoes_main,
        player_shoes_sub0,
        player_shoes_sub1,
        player_shoes_sub2,
    )
    battle_players = [player]
    if battle.teammate1_splatnet_id is not None:
        teammate1_weapon = static(
            "two_battles/weapons/" + battle.teammate1_weapon + ".png"
        )
        teammate1_k_a = battle.teammate1_kills + battle.teammate1_assists
        if battle.teammate1_headgear_main is not None:
            teammate1_headgear_main = static(
                "two_battles/abilities/mains/" + battle.teammate1_headgear_main + ".png"
            )
            if battle.teammate1_headgear_sub0 is not None:
                teammate1_headgear_sub0 = static(
                    "two_battles/abilities/subs/"
                    + battle.teammate1_headgear_sub0
                    + ".png"
                )
                if battle.teammate1_headgear_sub1 is not None:
                    teammate1_headgear_sub1 = static(
                        "two_battles/abilities/subs/"
                        + battle.teammate1_headgear_sub1
                        + ".png"
                    )
                    if battle.teammate1_headgear_sub2 is not None:
                        teammate1_headgear_sub2 = static(
                            "two_battles/abilities/subs/"
                            + battle.teammate1_headgear_sub2
                            + ".png"
                        )
                    else:
                        teammate1_headgear_sub2 = None
                else:
                    teammate1_headgear_sub1 = None
                    teammate1_headgear_sub2 = None
            else:
                teammate1_headgear_sub0 = None
                teammate1_headgear_sub1 = None
                teammate1_headgear_sub2 = None
        else:
            teammate1_headgear_main = None
            teammate1_headgear_sub0 = None
            teammate1_headgear_sub1 = None
            teammate1_headgear_sub2 = None
        if battle.teammate1_clothes_main is not None:
            teammate1_clothes_main = static(
                "two_battles/abilities/mains/" + battle.teammate1_clothes_main + ".png"
            )
            if battle.teammate1_clothes_sub0 is not None:
                teammate1_clothes_sub0 = static(
                    "two_battles/abilities/subs/"
                    + battle.teammate1_clothes_sub0
                    + ".png"
                )
                if battle.teammate1_clothes_sub1 is not None:
                    teammate1_clothes_sub1 = static(
                        "two_battles/abilities/subs/"
                        + battle.teammate1_clothes_sub1
                        + ".png"
                    )
                    if battle.teammate1_clothes_sub2 is not None:
                        teammate1_clothes_sub2 = static(
                            "two_battles/abilities/subs/"
                            + battle.teammate1_clothes_sub2
                            + ".png"
                        )
                    else:
                        teammate1_clothes_sub2 = None
                else:
                    teammate1_clothes_sub1 = None
                    teammate1_clothes_sub2 = None
            else:
                teammate1_clothes_sub0 = None
                teammate1_clothes_sub1 = None
                teammate1_clothes_sub2 = None
        else:
            teammate1_clothes_main = None
            teammate1_clothes_sub0 = None
            teammate1_clothes_sub1 = None
            teammate1_clothes_sub2 = None
        if battle.teammate1_shoes_main is not None:
            teammate1_shoes_main = static(
                "two_battles/abilities/mains/" + battle.teammate1_shoes_main + ".png"
            )
            if battle.teammate1_shoes_sub0 is not None:
                teammate1_shoes_sub0 = static(
                    "two_battles/abilities/subs/" + battle.teammate1_shoes_sub0 + ".png"
                )
                if battle.teammate1_shoes_sub1 is not None:
                    teammate1_shoes_sub1 = static(
                        "two_battles/abilities/subs/"
                        + battle.teammate1_shoes_sub1
                        + ".png"
                    )
                    if battle.teammate1_shoes_sub2 is not None:
                        teammate1_shoes_sub2 = static(
                            "two_battles/abilities/subs/"
                            + battle.teammate1_shoes_sub2
                            + ".png"
                        )
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
            teammate1_shoes_main = None
            teammate1_shoes_sub0 = None
            teammate1_shoes_sub1 = None
            teammate1_shoes_sub2 = None
        teammate1 = Player(
            "row2",
            battle.teammate1_name,
            teammate1_weapon,
            battle.get_teammate1_weapon_display(),
            battle.teammate1_level_star,
            battle.teammate1_level,
            battle.get_teammate1_rank_display(),
            battle.teammate1_game_paint_point,
            teammate1_k_a,
            battle.teammate1_assists,
            battle.teammate1_specials,
            battle.teammate1_kills,
            battle.teammate1_deaths,
            teammate1_headgear_main,
            teammate1_headgear_sub0,
            teammate1_headgear_sub1,
            teammate1_headgear_sub2,
            teammate1_clothes_main,
            teammate1_clothes_sub0,
            teammate1_clothes_sub1,
            teammate1_clothes_sub2,
            teammate1_shoes_main,
            teammate1_shoes_sub0,
            teammate1_shoes_sub1,
            teammate1_shoes_sub2,
        )
        battle_players.append(teammate1)
    if battle.teammate2_splatnet_id is not None:
        teammate2_weapon = static(
            "two_battles/weapons/" + battle.teammate2_weapon + ".png"
        )
        teammate2_k_a = battle.teammate2_kills + battle.teammate2_assists
        if battle.teammate2_headgear_main is not None:
            teammate2_headgear_main = static(
                "two_battles/abilities/mains/" + battle.teammate2_headgear_main + ".png"
            )
            if battle.teammate2_headgear_sub0 is not None:
                teammate2_headgear_sub0 = static(
                    "two_battles/abilities/subs/"
                    + battle.teammate2_headgear_sub0
                    + ".png"
                )
                if battle.teammate2_headgear_sub1 is not None:
                    teammate2_headgear_sub1 = static(
                        "two_battles/abilities/subs/"
                        + battle.teammate2_headgear_sub1
                        + ".png"
                    )
                    if battle.teammate2_headgear_sub2 is not None:
                        teammate2_headgear_sub2 = static(
                            "two_battles/abilities/subs/"
                            + battle.teammate2_headgear_sub2
                            + ".png"
                        )
                    else:
                        teammate2_headgear_sub2 = None
                else:
                    teammate2_headgear_sub1 = None
                    teammate2_headgear_sub2 = None
            else:
                teammate2_headgear_sub0 = None
                teammate2_headgear_sub1 = None
                teammate2_headgear_sub2 = None
        else:
            teammate2_headgear_main = None
            teammate2_headgear_sub0 = None
            teammate2_headgear_sub1 = None
            teammate2_headgear_sub2 = None
        if battle.teammate2_clothes_main is not None:
            teammate2_clothes_main = static(
                "two_battles/abilities/mains/" + battle.teammate2_clothes_main + ".png"
            )
            if battle.teammate2_clothes_sub0 is not None:
                teammate2_clothes_sub0 = static(
                    "two_battles/abilities/subs/"
                    + battle.teammate2_clothes_sub0
                    + ".png"
                )
                if battle.teammate2_clothes_sub1 is not None:
                    teammate2_clothes_sub1 = static(
                        "two_battles/abilities/subs/"
                        + battle.teammate2_clothes_sub1
                        + ".png"
                    )
                    if battle.teammate2_clothes_sub2 is not None:
                        teammate2_clothes_sub2 = static(
                            "two_battles/abilities/subs/"
                            + battle.teammate2_clothes_sub2
                            + ".png"
                        )
                    else:
                        teammate2_clothes_sub2 = None
                else:
                    teammate2_clothes_sub1 = None
                    teammate2_clothes_sub2 = None
            else:
                teammate2_clothes_sub0 = None
                teammate2_clothes_sub1 = None
                teammate2_clothes_sub2 = None
        else:
            teammate2_clothes_main = None
            teammate2_clothes_sub0 = None
            teammate2_clothes_sub1 = None
            teammate2_clothes_sub2 = None
        if battle.teammate2_shoes_main is not None:
            teammate2_shoes_main = static(
                "two_battles/abilities/mains/" + battle.teammate2_shoes_main + ".png"
            )
            if battle.teammate2_shoes_sub0 is not None:
                teammate2_shoes_sub0 = static(
                    "two_battles/abilities/subs/" + battle.teammate2_shoes_sub0 + ".png"
                )
                if battle.teammate2_shoes_sub1 is not None:
                    teammate2_shoes_sub1 = static(
                        "two_battles/abilities/subs/"
                        + battle.teammate2_shoes_sub1
                        + ".png"
                    )
                    if battle.teammate2_shoes_sub2 is not None:
                        teammate2_shoes_sub2 = static(
                            "two_battles/abilities/subs/"
                            + battle.teammate2_shoes_sub2
                            + ".png"
                        )
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
            teammate2_shoes_main = None
            teammate2_shoes_sub0 = None
            teammate2_shoes_sub1 = None
            teammate2_shoes_sub2 = None
        teammate2 = Player(
            "row3",
            battle.teammate2_name,
            teammate2_weapon,
            battle.get_teammate2_weapon_display(),
            battle.teammate2_level_star,
            battle.teammate2_level,
            battle.get_teammate2_rank_display(),
            battle.teammate2_game_paint_point,
            teammate2_k_a,
            battle.teammate2_assists,
            battle.teammate2_specials,
            battle.teammate2_kills,
            battle.teammate2_deaths,
            teammate2_headgear_main,
            teammate2_headgear_sub0,
            teammate2_headgear_sub1,
            teammate2_headgear_sub2,
            teammate2_clothes_main,
            teammate2_clothes_sub0,
            teammate2_clothes_sub1,
            teammate2_clothes_sub2,
            teammate2_shoes_main,
            teammate2_shoes_sub0,
            teammate2_shoes_sub1,
            teammate2_shoes_sub2,
        )
        battle_players.append(teammate2)
    if battle.teammate0_splatnet_id is not None:
        if battle.teammate0_weapon is not None:
            teammate0_weapon = static(
                "two_battles/weapons/" + battle.teammate0_weapon + ".png"
            )
        else:
            teammate0_weapon = ""
        teammate0_k_a = battle.teammate0_kills + battle.teammate0_assists
        if battle.teammate0_headgear_main is not None:
            teammate0_headgear_main = static(
                "two_battles/abilities/mains/" + battle.teammate0_headgear_main + ".png"
            )
            if battle.teammate0_headgear_sub0 is not None:
                teammate0_headgear_sub0 = static(
                    "two_battles/abilities/subs/"
                    + battle.teammate0_headgear_sub0
                    + ".png"
                )
                if battle.teammate0_headgear_sub1 is not None:
                    teammate0_headgear_sub1 = static(
                        "two_battles/abilities/subs/"
                        + battle.teammate0_headgear_sub1
                        + ".png"
                    )
                    if battle.teammate0_headgear_sub2 is not None:
                        teammate0_headgear_sub2 = static(
                            "two_battles/abilities/subs/"
                            + battle.teammate0_headgear_sub2
                            + ".png"
                        )
                    else:
                        teammate0_headgear_sub2 = None
                else:
                    teammate0_headgear_sub1 = None
                    teammate0_headgear_sub2 = None
            else:
                teammate0_headgear_sub0 = None
                teammate0_headgear_sub1 = None
                teammate0_headgear_sub2 = None
        else:
            teammate0_headgear_main = None
            teammate0_headgear_sub0 = None
            teammate0_headgear_sub1 = None
            teammate0_headgear_sub2 = None
        if battle.teammate0_clothes_main is not None:
            teammate0_clothes_main = static(
                "two_battles/abilities/mains/" + battle.teammate0_clothes_main + ".png"
            )
            if battle.teammate0_clothes_sub0 is not None:
                teammate0_clothes_sub0 = static(
                    "two_battles/abilities/subs/"
                    + battle.teammate0_clothes_sub0
                    + ".png"
                )
                if battle.teammate0_clothes_sub1 is not None:
                    teammate0_clothes_sub1 = static(
                        "two_battles/abilities/subs/"
                        + battle.teammate0_clothes_sub1
                        + ".png"
                    )
                    if battle.teammate0_clothes_sub2 is not None:
                        teammate0_clothes_sub2 = static(
                            "two_battles/abilities/subs/"
                            + battle.teammate0_clothes_sub2
                            + ".png"
                        )
                    else:
                        teammate0_clothes_sub2 = None
                else:
                    teammate0_clothes_sub1 = None
                    teammate0_clothes_sub2 = None
            else:
                teammate0_clothes_sub0 = None
                teammate0_clothes_sub1 = None
                teammate0_clothes_sub2 = None
        else:
            teammate0_clothes_main = None
            teammate0_clothes_sub0 = None
            teammate0_clothes_sub1 = None
            teammate0_clothes_sub2 = None
        if battle.teammate0_shoes_main is not None:
            teammate0_shoes_main = static(
                "two_battles/abilities/mains/" + battle.teammate0_shoes_main + ".png"
            )
            if battle.teammate0_shoes_sub0 is not None:
                teammate0_shoes_sub0 = static(
                    "two_battles/abilities/subs/" + battle.teammate0_shoes_sub0 + ".png"
                )
                if battle.teammate0_shoes_sub1 is not None:
                    teammate0_shoes_sub1 = static(
                        "two_battles/abilities/subs/"
                        + battle.teammate0_shoes_sub1
                        + ".png"
                    )
                    if battle.teammate0_shoes_sub2 is not None:
                        teammate0_shoes_sub2 = static(
                            "two_battles/abilities/subs/"
                            + battle.teammate0_shoes_sub2
                            + ".png"
                        )
                    else:
                        teammate0_shoes_sub2 = None
                else:
                    teammate0_shoes_sub1 = None
                    teammate0_shoes_sub2 = None
            else:
                teammate0_shoes_sub0 = None
                teammate0_shoes_sub1 = None
                teammate0_shoes_sub2 = None
        else:
            teammate0_shoes_main = None
            teammate0_shoes_sub0 = None
            teammate0_shoes_sub1 = None
            teammate0_shoes_sub2 = None
        teammate0 = Player(
            "row4",
            battle.teammate0_name,
            teammate0_weapon,
            battle.get_teammate0_weapon_display(),
            battle.teammate0_level_star,
            battle.teammate0_level,
            battle.get_teammate0_rank_display(),
            battle.teammate0_game_paint_point,
            teammate0_k_a,
            battle.teammate0_assists,
            battle.teammate0_specials,
            battle.teammate0_kills,
            battle.teammate0_deaths,
            teammate0_headgear_main,
            teammate0_headgear_sub0,
            teammate0_headgear_sub1,
            teammate0_headgear_sub2,
            teammate0_clothes_main,
            teammate0_clothes_sub0,
            teammate0_clothes_sub1,
            teammate0_clothes_sub2,
            teammate0_shoes_main,
            teammate0_shoes_sub0,
            teammate0_shoes_sub1,
            teammate0_shoes_sub2,
        )
        battle_players.append(teammate0)
    if battle.opponent0_splatnet_id is not None:
        opponent0_weapon = static(
            "two_battles/weapons/" + battle.opponent0_weapon + ".png"
        )
        opponent0_k_a = battle.opponent0_kills + battle.opponent0_assists
        if battle.opponent0_headgear_main is not None:
            opponent0_headgear_main = static(
                "two_battles/abilities/mains/" + battle.opponent0_headgear_main + ".png"
            )
            if battle.opponent0_headgear_sub0 is not None:
                opponent0_headgear_sub0 = static(
                    "two_battles/abilities/subs/"
                    + battle.opponent0_headgear_sub0
                    + ".png"
                )
                if battle.opponent0_headgear_sub1 is not None:
                    opponent0_headgear_sub1 = static(
                        "two_battles/abilities/subs/"
                        + battle.opponent0_headgear_sub1
                        + ".png"
                    )
                    if battle.opponent0_headgear_sub2 is not None:
                        opponent0_headgear_sub2 = static(
                            "two_battles/abilities/subs/"
                            + battle.opponent0_headgear_sub2
                            + ".png"
                        )
                    else:
                        opponent0_headgear_sub2 = None
                else:
                    opponent0_headgear_sub1 = None
                    opponent0_headgear_sub2 = None
            else:
                opponent0_headgear_sub0 = None
                opponent0_headgear_sub1 = None
                opponent0_headgear_sub2 = None
        else:
            opponent0_headgear_main = None
            opponent0_headgear_sub0 = None
            opponent0_headgear_sub1 = None
            opponent0_headgear_sub2 = None
        if battle.opponent0_clothes_main is not None:
            opponent0_clothes_main = static(
                "two_battles/abilities/mains/" + battle.opponent0_clothes_main + ".png"
            )
            if battle.opponent0_clothes_sub0 is not None:
                opponent0_clothes_sub0 = static(
                    "two_battles/abilities/subs/"
                    + battle.opponent0_clothes_sub0
                    + ".png"
                )
                if battle.opponent0_clothes_sub1 is not None:
                    opponent0_clothes_sub1 = static(
                        "two_battles/abilities/subs/"
                        + battle.opponent0_clothes_sub1
                        + ".png"
                    )
                    if battle.opponent0_clothes_sub2 is not None:
                        opponent0_clothes_sub2 = static(
                            "two_battles/abilities/subs/"
                            + battle.opponent0_clothes_sub2
                            + ".png"
                        )
                    else:
                        opponent0_clothes_sub2 = None
                else:
                    opponent0_clothes_sub1 = None
                    opponent0_clothes_sub2 = None
            else:
                opponent0_clothes_sub0 = None
                opponent0_clothes_sub1 = None
                opponent0_clothes_sub2 = None
        else:
            opponent0_clothes_main = None
            opponent0_clothes_sub0 = None
            opponent0_clothes_sub1 = None
            opponent0_clothes_sub2 = None
        if battle.opponent0_shoes_main is not None:
            opponent0_shoes_main = static(
                "two_battles/abilities/mains/" + battle.opponent0_shoes_main + ".png"
            )
            if battle.opponent0_shoes_sub0 is not None:
                opponent0_shoes_sub0 = static(
                    "two_battles/abilities/subs/" + battle.opponent0_shoes_sub0 + ".png"
                )
                if battle.opponent0_shoes_sub1 is not None:
                    opponent0_shoes_sub1 = static(
                        "two_battles/abilities/subs/"
                        + battle.opponent0_shoes_sub1
                        + ".png"
                    )
                    if battle.opponent0_shoes_sub2 is not None:
                        opponent0_shoes_sub2 = static(
                            "two_battles/abilities/subs/"
                            + battle.opponent0_shoes_sub2
                            + ".png"
                        )
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
            opponent0_shoes_main = None
            opponent0_shoes_sub0 = None
            opponent0_shoes_sub1 = None
            opponent0_shoes_sub2 = None
        opponent0 = Player(
            "row5",
            battle.opponent0_name,
            opponent0_weapon,
            battle.get_opponent0_weapon_display(),
            battle.opponent0_level_star,
            battle.opponent0_level,
            battle.get_opponent0_rank_display(),
            battle.opponent0_game_paint_point,
            opponent0_k_a,
            battle.opponent0_assists,
            battle.opponent0_specials,
            battle.opponent0_kills,
            battle.opponent0_deaths,
            opponent0_headgear_main,
            opponent0_headgear_sub0,
            opponent0_headgear_sub1,
            opponent0_headgear_sub2,
            opponent0_clothes_main,
            opponent0_clothes_sub0,
            opponent0_clothes_sub1,
            opponent0_clothes_sub2,
            opponent0_shoes_main,
            opponent0_shoes_sub0,
            opponent0_shoes_sub1,
            opponent0_shoes_sub2,
        )
        battle_players.append(opponent0)
    if battle.opponent1_splatnet_id is not None:
        opponent1_weapon = static(
            "two_battles/weapons/" + battle.opponent1_weapon + ".png"
        )
        opponent1_k_a = battle.opponent1_kills + battle.opponent1_assists
        if battle.opponent1_headgear_main is not None:
            opponent1_headgear_main = static(
                "two_battles/abilities/mains/" + battle.opponent1_headgear_main + ".png"
            )
            if battle.opponent1_headgear_sub0 is not None:
                opponent1_headgear_sub0 = static(
                    "two_battles/abilities/subs/"
                    + battle.opponent1_headgear_sub0
                    + ".png"
                )
                if battle.opponent1_headgear_sub1 is not None:
                    opponent1_headgear_sub1 = static(
                        "two_battles/abilities/subs/"
                        + battle.opponent1_headgear_sub1
                        + ".png"
                    )
                    if battle.opponent1_headgear_sub2 is not None:
                        opponent1_headgear_sub2 = static(
                            "two_battles/abilities/subs/"
                            + battle.opponent1_headgear_sub2
                            + ".png"
                        )
                    else:
                        opponent1_headgear_sub2 = None
                else:
                    opponent1_headgear_sub1 = None
                    opponent1_headgear_sub2 = None
            else:
                opponent1_headgear_sub0 = None
                opponent1_headgear_sub1 = None
                opponent1_headgear_sub2 = None
        else:
            opponent1_headgear_main = None
            opponent1_headgear_sub0 = None
            opponent1_headgear_sub1 = None
            opponent1_headgear_sub2 = None
        if battle.opponent1_clothes_main is not None:
            opponent1_clothes_main = static(
                "two_battles/abilities/mains/" + battle.opponent1_clothes_main + ".png"
            )
            if battle.opponent1_clothes_sub0 is not None:
                opponent1_clothes_sub0 = static(
                    "two_battles/abilities/subs/"
                    + battle.opponent1_clothes_sub0
                    + ".png"
                )
                if battle.opponent1_clothes_sub1 is not None:
                    opponent1_clothes_sub1 = static(
                        "two_battles/abilities/subs/"
                        + battle.opponent1_clothes_sub1
                        + ".png"
                    )
                    if battle.opponent1_clothes_sub2 is not None:
                        opponent1_clothes_sub2 = static(
                            "two_battles/abilities/subs/"
                            + battle.opponent1_clothes_sub2
                            + ".png"
                        )
                    else:
                        opponent1_clothes_sub2 = None
                else:
                    opponent1_clothes_sub1 = None
                    opponent1_clothes_sub2 = None
            else:
                opponent1_clothes_sub0 = None
                opponent1_clothes_sub1 = None
                opponent1_clothes_sub2 = None
        else:
            opponent1_clothes_main = None
            opponent1_clothes_sub0 = None
            opponent1_clothes_sub1 = None
            opponent1_clothes_sub2 = None
        if battle.opponent1_shoes_main is not None:
            opponent1_shoes_main = static(
                "two_battles/abilities/mains/" + battle.opponent1_shoes_main + ".png"
            )
            if battle.opponent1_shoes_sub0 is not None:
                opponent1_shoes_sub0 = static(
                    "two_battles/abilities/subs/" + battle.opponent1_shoes_sub0 + ".png"
                )
                if battle.opponent1_shoes_sub1 is not None:
                    opponent1_shoes_sub1 = static(
                        "two_battles/abilities/subs/"
                        + battle.opponent1_shoes_sub1
                        + ".png"
                    )
                    if battle.opponent1_shoes_sub2 is not None:
                        opponent1_shoes_sub2 = static(
                            "two_battles/abilities/subs/"
                            + battle.opponent1_shoes_sub2
                            + ".png"
                        )
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
            opponent1_shoes_main = None
            opponent1_shoes_sub0 = None
            opponent1_shoes_sub1 = None
            opponent1_shoes_sub2 = None
        opponent1 = Player(
            "row6",
            battle.opponent1_name,
            opponent1_weapon,
            battle.get_opponent1_weapon_display(),
            battle.opponent1_level_star,
            battle.opponent1_level,
            battle.get_opponent1_rank_display(),
            battle.opponent1_game_paint_point,
            opponent1_k_a,
            battle.opponent1_assists,
            battle.opponent1_specials,
            battle.opponent1_kills,
            battle.opponent1_deaths,
            opponent1_headgear_main,
            opponent1_headgear_sub0,
            opponent1_headgear_sub1,
            opponent1_headgear_sub2,
            opponent1_clothes_main,
            opponent1_clothes_sub0,
            opponent1_clothes_sub1,
            opponent1_clothes_sub2,
            opponent1_shoes_main,
            opponent1_shoes_sub0,
            opponent1_shoes_sub1,
            opponent1_shoes_sub2,
        )
        battle_players.append(opponent1)
    if battle.opponent2_splatnet_id is not None:
        opponent2_weapon = static(
            "two_battles/weapons/" + battle.opponent2_weapon + ".png"
        )
        opponent2_k_a = battle.opponent2_kills + battle.opponent2_assists
        if battle.opponent2_headgear_main is not None:
            opponent2_headgear_main = static(
                "two_battles/abilities/mains/" + battle.opponent2_headgear_main + ".png"
            )
            if battle.opponent2_headgear_sub0 is not None:
                opponent2_headgear_sub0 = static(
                    "two_battles/abilities/subs/"
                    + battle.opponent2_headgear_sub0
                    + ".png"
                )
                if battle.opponent2_headgear_sub1 is not None:
                    opponent2_headgear_sub1 = static(
                        "two_battles/abilities/subs/"
                        + battle.opponent2_headgear_sub1
                        + ".png"
                    )
                    if battle.opponent2_headgear_sub2 is not None:
                        opponent2_headgear_sub2 = static(
                            "two_battles/abilities/subs/"
                            + battle.opponent2_headgear_sub2
                            + ".png"
                        )
                    else:
                        opponent2_headgear_sub2 = None
                else:
                    opponent2_headgear_sub1 = None
                    opponent2_headgear_sub2 = None
            else:
                opponent2_headgear_sub0 = None
                opponent2_headgear_sub1 = None
                opponent2_headgear_sub2 = None
        else:
            opponent2_headgear_main = None
            opponent2_headgear_sub0 = None
            opponent2_headgear_sub1 = None
            opponent2_headgear_sub2 = None
        if battle.opponent2_clothes_main is not None:
            opponent2_clothes_main = static(
                "two_battles/abilities/mains/" + battle.opponent2_clothes_main + ".png"
            )
            if battle.opponent2_clothes_sub0 is not None:
                opponent2_clothes_sub0 = static(
                    "two_battles/abilities/subs/"
                    + battle.opponent2_clothes_sub0
                    + ".png"
                )
                if battle.opponent2_clothes_sub1 is not None:
                    opponent2_clothes_sub1 = static(
                        "two_battles/abilities/subs/"
                        + battle.opponent2_clothes_sub1
                        + ".png"
                    )
                    if battle.opponent2_clothes_sub2 is not None:
                        opponent2_clothes_sub2 = static(
                            "two_battles/abilities/subs/"
                            + battle.opponent2_clothes_sub2
                            + ".png"
                        )
                    else:
                        opponent2_clothes_sub2 = None
                else:
                    opponent2_clothes_sub1 = None
                    opponent2_clothes_sub2 = None
            else:
                opponent2_clothes_sub0 = None
                opponent2_clothes_sub1 = None
                opponent2_clothes_sub2 = None
        else:
            opponent2_clothes_main = None
            opponent2_clothes_sub0 = None
            opponent2_clothes_sub1 = None
            opponent2_clothes_sub2 = None
        if battle.opponent2_shoes_main is not None:
            opponent2_shoes_main = static(
                "two_battles/abilities/mains/" + battle.opponent2_shoes_main + ".png"
            )
            if battle.opponent2_shoes_sub0 is not None:
                opponent2_shoes_sub0 = static(
                    "two_battles/abilities/subs/" + battle.opponent2_shoes_sub0 + ".png"
                )
                if battle.opponent2_shoes_sub1 is not None:
                    opponent2_shoes_sub1 = static(
                        "two_battles/abilities/subs/"
                        + battle.opponent2_shoes_sub1
                        + ".png"
                    )
                    if battle.opponent2_shoes_sub2 is not None:
                        opponent2_shoes_sub2 = static(
                            "two_battles/abilities/subs/"
                            + battle.opponent2_shoes_sub2
                            + ".png"
                        )
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
            opponent2_shoes_main = None
            opponent2_shoes_sub0 = None
            opponent2_shoes_sub1 = None
            opponent2_shoes_sub2 = None
        opponent2 = Player(
            "row7",
            battle.opponent2_name,
            opponent2_weapon,
            battle.get_opponent2_weapon_display(),
            battle.opponent2_level_star,
            battle.opponent2_level,
            battle.get_opponent2_rank_display(),
            battle.opponent2_game_paint_point,
            opponent2_k_a,
            battle.opponent2_assists,
            battle.opponent2_specials,
            battle.opponent2_kills,
            battle.opponent2_deaths,
            opponent2_headgear_main,
            opponent2_headgear_sub0,
            opponent2_headgear_sub1,
            opponent2_headgear_sub2,
            opponent2_clothes_main,
            opponent2_clothes_sub0,
            opponent2_clothes_sub1,
            opponent2_clothes_sub2,
            opponent2_shoes_main,
            opponent2_shoes_sub0,
            opponent2_shoes_sub1,
            opponent2_shoes_sub2,
        )
        battle_players.append(opponent2)
    if battle.opponent3_splatnet_id is not None:
        opponent3_weapon = static(
            "two_battles/weapons/" + battle.opponent3_weapon + ".png"
        )
        opponent3_k_a = battle.opponent3_kills + battle.opponent3_assists
        if battle.opponent3_headgear_main is not None:
            opponent3_headgear_main = static(
                "two_battles/abilities/mains/" + battle.opponent3_headgear_main + ".png"
            )
            if battle.opponent3_headgear_sub0 is not None:
                opponent3_headgear_sub0 = static(
                    "two_battles/abilities/subs/"
                    + battle.opponent3_headgear_sub0
                    + ".png"
                )
                if battle.opponent3_headgear_sub1 is not None:
                    opponent3_headgear_sub1 = static(
                        "two_battles/abilities/subs/"
                        + battle.opponent3_headgear_sub1
                        + ".png"
                    )
                    if battle.opponent3_headgear_sub2 is not None:
                        opponent3_headgear_sub2 = static(
                            "two_battles/abilities/subs/"
                            + battle.opponent3_headgear_sub2
                            + ".png"
                        )
                    else:
                        opponent3_headgear_sub2 = None
                else:
                    opponent3_headgear_sub1 = None
                    opponent3_headgear_sub2 = None
            else:
                opponent3_headgear_sub0 = None
                opponent3_headgear_sub1 = None
                opponent3_headgear_sub2 = None
        else:
            opponent3_headgear_main = None
            opponent3_headgear_sub0 = None
            opponent3_headgear_sub1 = None
            opponent3_headgear_sub2 = None
        if battle.opponent3_clothes_main is not None:
            opponent3_clothes_main = static(
                "two_battles/abilities/mains/" + battle.opponent3_clothes_main + ".png"
            )
            if battle.opponent3_clothes_sub0 is not None:
                opponent3_clothes_sub0 = static(
                    "two_battles/abilities/subs/"
                    + battle.opponent3_clothes_sub0
                    + ".png"
                )
                if battle.opponent3_clothes_sub1 is not None:
                    opponent3_clothes_sub1 = static(
                        "two_battles/abilities/subs/"
                        + battle.opponent3_clothes_sub1
                        + ".png"
                    )
                    if battle.opponent3_clothes_sub2 is not None:
                        opponent3_clothes_sub2 = static(
                            "two_battles/abilities/subs/"
                            + battle.opponent3_clothes_sub2
                            + ".png"
                        )
                    else:
                        opponent3_clothes_sub2 = None
                else:
                    opponent3_clothes_sub1 = None
                    opponent3_clothes_sub2 = None
            else:
                opponent3_clothes_sub0 = None
                opponent3_clothes_sub1 = None
                opponent3_clothes_sub2 = None
        else:
            opponent3_clothes_main = None
            opponent3_clothes_sub0 = None
            opponent3_clothes_sub1 = None
            opponent3_clothes_sub2 = None
        if battle.opponent3_shoes_main is not None:
            opponent3_shoes_main = static(
                "two_battles/abilities/mains/" + battle.opponent3_shoes_main + ".png"
            )
            if battle.opponent3_shoes_sub0 is not None:
                opponent3_shoes_sub0 = static(
                    "two_battles/abilities/subs/" + battle.opponent3_shoes_sub0 + ".png"
                )
                if battle.opponent3_shoes_sub1 is not None:
                    opponent3_shoes_sub1 = static(
                        "two_battles/abilities/subs/"
                        + battle.opponent3_shoes_sub1
                        + ".png"
                    )
                    if battle.opponent3_shoes_sub2 is not None:
                        opponent3_shoes_sub2 = static(
                            "two_battles/abilities/subs/"
                            + battle.opponent3_shoes_sub2
                            + ".png"
                        )
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
            opponent3_shoes_main = None
            opponent3_shoes_sub0 = None
            opponent3_shoes_sub1 = None
            opponent3_shoes_sub2 = None
        opponent3 = Player(
            "row8",
            battle.opponent3_name,
            opponent3_weapon,
            battle.get_opponent3_weapon_display(),
            battle.opponent3_level_star,
            battle.opponent3_level,
            battle.get_opponent3_rank_display(),
            battle.opponent3_game_paint_point,
            opponent3_k_a,
            battle.opponent3_assists,
            battle.opponent3_specials,
            battle.opponent3_kills,
            battle.opponent3_deaths,
            opponent3_headgear_main,
            opponent3_headgear_sub0,
            opponent3_headgear_sub1,
            opponent3_headgear_sub2,
            opponent3_clothes_main,
            opponent3_clothes_sub0,
            opponent3_clothes_sub1,
            opponent3_clothes_sub2,
            opponent3_shoes_main,
            opponent3_shoes_sub0,
            opponent3_shoes_sub1,
            opponent3_shoes_sub2,
        )
        battle_players.append(opponent3)
    return render(
        request,
        "two_battles/battle.html",
        {
            "battle": battle,
            "battle_players": battle_players,
            "result": "Win" if battle.win else "Lose",
            "end_result": "Time"
            if battle.rule != "turf_war" and battle.elapsed_time >= 300
            else "Knockout",
            "start_time": datetime.utcfromtimestamp(battle.time).strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "end_time": datetime.utcfromtimestamp(
                battle.time + battle.elapsed_time
            ).strftime("%Y-%m-%d %H:%M:%S"),
            "elapsed_time_min_sec": strftime("%M:%S", gmtime(battle.elapsed_time)),
        },
    )


def upload(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = BattleForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            battle = Battle.create(
                splatnet_json=form.cleaned_data["splatnet_json"], user=request.user
            )
            battle.save()
            return HttpResponseRedirect("/two_battles/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = BattleForm()

    return render(request, "two_battles/upload.html", {"form": form})


class BattleAPIView(views.APIView):
    throttle_classes = ()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    parser_classes = (JSONParser,)

    def get(self, request):
        return HttpResponseRedirect("/two_battles/")

    def post(self, request, format=None):
        image_result = (
            base64.b64decode(
                request.data.get("image_result", None).encode(encoding="ascii")
            )
            if request.data.get("image_result", None) is not None
            else None
        )
        image_gear = image_gear = (
            base64.b64decode(
                request.data.get("image_gear", None).encode(encoding="ascii")
            )
            if request.data.get("image_gear", None) is not None
            else None
        )
        if request.data.get("splatnet_json", None) is not None:
            if request.data.get("stat_ink_json", None) is not None:
                Battle.create(
                    splatnet_json=json.loads(request.data.get("splatnet_json", None)),
                    stat_ink_json=json.loads(request.data.get("stat_ink_json", None)),
                    image_result=image_result,
                    image_gear=image_gear,
                    user=request.user,
                )
            else:
                Battle.create(
                    splatnet_json=json.loads(request.data.get("splatnet_json", None)),
                    image_result=image_result,
                    image_gear=image_gear,
                    user=request.user,
                )
        elif request.data.get("stat_ink_json", None) is not None:
            Battle.create(
                stat_ink_json=json.loads(request.data.get("stat_ink_json", None)),
                image_result=image_result,
                image_gear=image_gear,
                user=request.user,
            )
        return Response(data=None, status=status.HTTP_200_OK)
