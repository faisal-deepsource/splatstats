from .advanced_search_language import Interpreter, Lexer
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from rest_framework import views, status, permissions
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from time import gmtime
from time import strftime
from .forms import BattleForm, FilterForm, AdvancedFilterForm
import base64
from .models import Battle
from .objects import Player
from django.templatetags.static import static
import json
from datetime import datetime
import regex
from django.core.paginator import Paginator


def index(request):
    form = FilterForm(request.GET)
    attributes = ""
    if form.is_valid():
        battles = Battle.objects
        if "query" in form.cleaned_data and form.cleaned_data["query"] != "":
            battles = get_query(form)
            query = form.cleaned_data["query"]
            attributes = ""
        else:
            attributes = ""
            if form.cleaned_data["rule"] != "all":
                battles = battles.filter(rule=form.cleaned_data["rule"])
            if form.cleaned_data["match_type"] != "all":
                battles = battles.filter(match_type=form.cleaned_data["match_type"])
            if form.cleaned_data["stage"] != "all":
                battles = battles.filter(stage=form.cleaned_data["stage"])
            if form.cleaned_data["rank"] != "21":
                battles = battles.filter(player_rank=int(form.cleaned_data["rank"]))
            if form.cleaned_data["weapon"] != "all":
                battles = battles.filter(player_weapon=form.cleaned_data["weapon"])
            query = ""
            attributes += "&rule=" + form.cleaned_data["rule"]
            attributes += "&match_type=" + form.cleaned_data["match_type"]
            attributes += "&stage=" + form.cleaned_data["stage"]
            attributes += "&rank=" + form.cleaned_data["rank"]
            attributes += "&weapon=" + form.cleaned_data["weapon"]
        battles = battles.order_by("-time")
    else:
        query = ""
        battles = Battle.objects.order_by("-time")
        attributes = ""
    paginator = Paginator(battles, 50)  # Show 50 battles per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    results = []
    time_vals = []
    player_weapons = []
    for battle in page_obj:
        results.append("Win" if battle.win else "Lose")
        if battle.time is not None:
            time_vals.append(
                datetime.utcfromtimestamp(battle.time).strftime("%Y-%m-%d %H:%M:%S")
            )
        else:
            time_vals.append(None)
        player_weapons.append(
            static("two_battles/weapons/" + battle.player_weapon + ".png")
        )
    context = {
        "page_obj": page_obj,
        "my_list": zip(
            page_obj,
            results,
            time_vals,
            player_weapons,
        ),
        "form": form,
        "query": query,
        "attributes": attributes,
    }
    return render(request, "two_battles/index.html", context)


def detail(request, id):
    battle = get_object_or_404(Battle, pk=id)
    if battle.player_kills is not None and battle.player_assists is not None:
        player_k_a = battle.player_kills + battle.player_assists
    else:
        player_k_a = None
    player_weapon = static("two_battles/weapons/" + battle.player_weapon + ".png")
    if battle.player_headgear_main is not None:
        player_headgear_main = static(
            "two_battles/abilities/mains/" + battle.player_headgear_main + ".png"
        )
    else:
        player_headgear_main = None
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
    if battle.player_clothes_main is not None:
        player_clothes_main = static(
            "two_battles/abilities/mains/" + battle.player_clothes_main + ".png"
        )
    else:
        player_clothes_main = None
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
    if battle.player_shoes_main is not None:
        player_shoes_main = static(
            "two_battles/abilities/mains/" + battle.player_shoes_main + ".png"
        )
    else:
        player_shoes_main = None
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
            )
            if battle.time is not None
            else None,
            "end_time": datetime.utcfromtimestamp(
                battle.time + battle.elapsed_time
            ).strftime("%Y-%m-%d %H:%M:%S")
            if battle.time is not None and battle.elapsed_time is not None
            else None,
            "elapsed_time_min_sec": strftime("%M:%S", gmtime(battle.elapsed_time))
            if battle.elapsed_time is not None
            else None,
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

    @staticmethod
    def get(request):
        return HttpResponseRedirect("/two_battles/")

    @staticmethod
    def post(request, format=None):
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


def to_int(value):
    try:
        return int(value)
    except:
        return None


def to_bool(value):
    return value == "True"


def to_float(value):
    try:
        return float(value)
    except:
        return None


def find_2nd(string, substring):
    return string.find(substring, string.find(substring) + 1)


def attribute_cast(attr, val):
    lookups = (
        ("(win)|(has_disconnected_player)", "bool"),
        (
            "((elapsed_)?time)|(win_meter)|(((player)|(teammate_[a-c])|(opponent_[a-d]))_((rank)|(level(_star)?)|(kills)|(deaths)|(assists)|(specials)|(game_paint_point)))",
            "int",
        ),
        (
            "(((my)|(other))_team_count)|(((league)|(splatfest))_point)|(player_x_power)",
            "float",
        ),
    )
    switch = {"bool": to_bool(val), "int": to_int(val), "float": to_float(val)}
    for pattern, value in lookups:
        if regex.search(pattern, attr):
            return switch.get(value)
    return val


def get_query(form):
    tokens = form.cleaned_data["query"].split()
    current_attribute = None
    past_tokens = []
    mapping = {
        "abcd-abc": {},
        "abcd-acb": {},
        "abcd-bac": {},
        "abcd-bca": {},
        "abcd-cab": {},
        "abcd-cba": {},
        "abdc-abc": {},
        "abdc-acb": {},
        "abdc-bac": {},
        "abdc-bca": {},
        "abdc-cab": {},
        "abdc-cba": {},
        "acbd-abc": {},
        "acbd-acb": {},
        "acbd-bac": {},
        "acbd-bca": {},
        "acbd-cab": {},
        "acbd-cba": {},
        "acdb-abc": {},
        "acdb-acb": {},
        "acdb-bac": {},
        "acdb-bca": {},
        "acdb-cab": {},
        "acdb-cba": {},
        "adbc-abc": {},
        "adbc-acb": {},
        "adbc-bac": {},
        "adbc-bca": {},
        "adbc-cab": {},
        "adbc-cba": {},
        "adcb-abc": {},
        "adcb-acb": {},
        "adcb-bac": {},
        "adcb-bca": {},
        "adcb-cab": {},
        "adcb-cba": {},
        "bacd-abc": {},
        "bacd-acb": {},
        "bacd-bac": {},
        "bacd-bca": {},
        "bacd-cab": {},
        "bacd-cba": {},
        "badc-abc": {},
        "badc-acb": {},
        "badc-bac": {},
        "badc-bca": {},
        "badc-cab": {},
        "badc-cba": {},
        "bcad-abc": {},
        "bcad-acb": {},
        "bcad-bac": {},
        "bcad-bca": {},
        "bcad-cab": {},
        "bcad-cba": {},
        "bcda-abc": {},
        "bcda-acb": {},
        "bcda-bac": {},
        "bcda-bca": {},
        "bcda-cab": {},
        "bcda-cba": {},
        "bdac-abc": {},
        "bdac-acb": {},
        "bdac-bac": {},
        "bdac-bca": {},
        "bdac-cab": {},
        "bdac-cba": {},
        "bdca-abc": {},
        "bdca-acb": {},
        "bdca-bac": {},
        "bdca-bca": {},
        "bdca-cab": {},
        "bdca-cba": {},
        "cabd-abc": {},
        "cabd-acb": {},
        "cabd-bac": {},
        "cabd-bca": {},
        "cabd-cab": {},
        "cabd-cba": {},
        "cadb-abc": {},
        "cadb-acb": {},
        "cadb-bac": {},
        "cadb-bca": {},
        "cadb-cab": {},
        "cadb-cba": {},
        "cbad-abc": {},
        "cbad-acb": {},
        "cbad-bac": {},
        "cbad-bca": {},
        "cbad-cab": {},
        "cbad-cba": {},
        "cbda-abc": {},
        "cbda-acb": {},
        "cbda-bac": {},
        "cbda-bca": {},
        "cbda-cab": {},
        "cbda-cba": {},
        "cdab-abc": {},
        "cdab-acb": {},
        "cdab-bac": {},
        "cdab-bca": {},
        "cdab-cab": {},
        "cdab-cba": {},
        "cdba-abc": {},
        "cdba-acb": {},
        "cdba-bac": {},
        "cdba-bca": {},
        "cdba-cab": {},
        "cdba-cba": {},
        "dabc-abc": {},
        "dabc-acb": {},
        "dabc-bac": {},
        "dabc-bca": {},
        "dabc-cab": {},
        "dabc-cba": {},
        "dacb-abc": {},
        "dacb-acb": {},
        "dacb-bac": {},
        "dacb-bca": {},
        "dacb-cab": {},
        "dacb-cba": {},
        "dbac-abc": {},
        "dbac-acb": {},
        "dbac-bac": {},
        "dbac-bca": {},
        "dbac-cab": {},
        "dbac-cba": {},
        "dbca-abc": {},
        "dbca-acb": {},
        "dbca-bac": {},
        "dbca-bca": {},
        "dbca-cab": {},
        "dbca-cba": {},
        "dcab-abc": {},
        "dcab-acb": {},
        "dcab-bac": {},
        "dcab-bca": {},
        "dcab-cab": {},
        "dcab-cba": {},
        "dcba-abc": {},
        "dcba-acb": {},
        "dcba-bac": {},
        "dcba-bca": {},
        "dcba-cab": {},
        "dcba-cba": {},
    }
    for token in tokens:
        if current_attribute is None:
            current_attribute = token
        else:
            if len(past_tokens) > 0:
                if token[-1] == '"':
                    past_tokens.append(token[: len(token) - 1])
                    if regex.search(
                        "(rule)|(match_type)|(stage)|(win(_meter)?)|(has_disconnected_player)|(((my)|(other))_team_count)|((elapsed_)?time)|(tag_id)|(battle_number)|(((league)|(splatfest))_point)|(splatfest_title_after)|(player_x_power)|(((player)|(teammate_[a-c])|(opponent_[a-d]))_(((headgear)|(clothes)|(shoes))_((sub[0-2])|(main))?|(weapon)|(rank)|(level(_star)?)|(kills)|(deaths)|(assists)|(specials)|(game_paint_point)|(splatfest_title)|(name)|(splatnet_id)|(gender)|(species)))",
                        current_attribute,
                    ):
                        if regex.search(
                            "((teammate_[a-c])|(opponent_[a-d]))_[0-z_]*",
                            current_attribute,
                        ):
                            for key in mapping:
                                if current_attribute[0:8] == "teammate":
                                    mapping[key][
                                        "{}{}{}".format(
                                            current_attribute[0:8],
                                            find_2nd(key, current_attribute[9]) - 5,
                                            current_attribute[10:],
                                        )
                                    ] = attribute_cast(
                                        current_attribute, "".join(past_tokens)
                                    )
                                else:
                                    mapping[key][
                                        "{}{}{}".format(
                                            current_attribute[0:8],
                                            key.index(current_attribute[9]),
                                            current_attribute[10:],
                                        )
                                    ] = attribute_cast(
                                        current_attribute, "".join(past_tokens)
                                    )
                        else:
                            for key in mapping:
                                mapping[key][current_attribute] = attribute_cast(
                                    current_attribute, "".join(past_tokens)
                                )
                        past_tokens = []
                        current_attribute = None
                    else:
                        return Battle.objects.none()
                else:
                    past_tokens.append(token)
            else:
                if token[0] == '"':
                    past_tokens.append(token[1:])
                    past_tokens.append(" ")
                else:
                    past_tokens.append(token)
                    if regex.search(
                        "(rule)|(match_type)|(stage)|(win(_meter)?)|(has_disconnected_player)|(((my)|(other))_team_count)|((elapsed_)?time)|(tag_id)|(battle_number)|(((league)|(splatfest))_point)|(splatfest_title_after)|(player_x_power)|(((player)|(teammate_[a-c])|(opponent_[a-d]))_(((headgear)|(clothes)|(shoes))_((sub[0-2])|(main))?|(weapon)|(rank)|(level(_star)?)|(kills)|(deaths)|(assists)|(specials)|(game_paint_point)|(splatfest_title)|(name)|(splatnet_id)|(gender)|(species)))",
                        current_attribute,
                    ):
                        if regex.search(
                            "((teammate_[a-c])|(opponent_[a-d]))_[0-z_]*",
                            current_attribute,
                        ):
                            for key in mapping:
                                if current_attribute[0:8] == "teammate":
                                    mapping[key][
                                        "{}{}{}".format(
                                            current_attribute[0:8],
                                            find_2nd(key, current_attribute[9]) - 5,
                                            current_attribute[10:],
                                        )
                                    ] = attribute_cast(
                                        current_attribute, "".join(past_tokens)
                                    )
                                else:
                                    mapping[key][
                                        "{}{}{}".format(
                                            current_attribute[0:8],
                                            key.index(current_attribute[9]),
                                            current_attribute[10:],
                                        )
                                    ] = attribute_cast(
                                        current_attribute, "".join(past_tokens)
                                    )
                        else:
                            for key in mapping:
                                mapping[key][current_attribute] = attribute_cast(
                                    current_attribute, "".join(past_tokens)
                                )
                        past_tokens = []
                        current_attribute = None
                    else:
                        return Battle.objects.none()
    battles = Battle.objects.none()
    for key in mapping:
        battles = battles | Battle.objects.filter(**(mapping[key])).order_by("-time")
    return battles


def advanced_search(request):
    form = AdvancedFilterForm(request.GET)
    if form.is_valid():
        lexer = Lexer(form.cleaned_data["query"])
        interpreter = Interpreter(lexer)
        battles = interpreter.term()
        paginator = Paginator(battles, 50)  # Show 50 battles per page
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        results = []
        time_vals = []
        player_weapons = []
        for battle in page_obj:
            results.append("Win" if battle.win else "Lose")
            if battle.time is not None:
                time_vals.append(
                    datetime.utcfromtimestamp(battle.time).strftime("%Y-%m-%d %H:%M:%S")
                )
            else:
                time_vals.append(None)
            player_weapons.append(
                static("two_battles/weapons/" + battle.player_weapon + ".png")
            )
        query = form.cleaned_data["query"]
        context = {
            "page_obj": page_obj,
            "my_list": zip(
                page_obj,
                results,
                time_vals,
                player_weapons,
            ),
            "form": form,
            "search_status": True,
            "query": query,
            "attributes": "",
        }
        return render(request, "two_battles/index.html", context)
    return render(request, "two_battles/advanced_search.html", {"form": form})
