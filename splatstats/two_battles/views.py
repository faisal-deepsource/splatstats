from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import views, status, permissions
from rest_framework.parsers import JSONParser
from rest_framework_msgpack.parsers import MessagePackParser
from rest_framework.response import Response
from .forms import BattleForm
import base64
from .models import Battle
from django.templatetags.static import static
import json
from datetime import datetime



def index(request):
    latest_battles = Battle.objects.order_by("-time")
    results = []
    time_vals = []
    for battle in latest_battles:
        results.append("Win" if battle.win else "Lose")
        time_vals.append(datetime.utcfromtimestamp(battle.time).strftime('%Y-%m-%d %H:%M:%S'))
    context = {
        "my_list": zip(
            latest_battles,
            results,
            time_vals,
        )
    }
    return render(request, "two_battles/index.html", context)


def detail(request, id):
    battle = get_object_or_404(Battle, pk=id)
    player_k_a = battle.player_kills + battle.player_assists
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
    if battle.teammate1_splatnet_id is not None:
        teammate1_k_a = battle.teammate1_kills + battle.teammate1_assists
        teammate1_headgear_main = static(
            "two_battles/abilities/mains/" + battle.teammate1_headgear_main + ".png"
        )
        if battle.teammate1_headgear_sub0 is not None:
            teammate1_headgear_sub0 = static(
                "two_battles/abilities/subs/" + battle.teammate1_headgear_sub0 + ".png"
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
        teammate1_clothes_main = static(
            "two_battles/abilities/mains/" + battle.teammate1_clothes_main + ".png"
        )
        if battle.teammate1_clothes_sub0 is not None:
            teammate1_clothes_sub0 = static(
                "two_battles/abilities/subs/" + battle.teammate1_clothes_sub0 + ".png"
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
        teammate1_shoes_main = static(
            "two_battles/abilities/mains/" + battle.teammate1_shoes_main + ".png"
        )
        if battle.teammate1_shoes_sub0 is not None:
            teammate1_shoes_sub0 = static(
                "two_battles/abilities/subs/" + battle.teammate1_shoes_sub0 + ".png"
            )
            if battle.teammate1_shoes_sub1 is not None:
                teammate1_shoes_sub1 = static(
                    "two_battles/abilities/subs/" + battle.teammate1_shoes_sub1 + ".png"
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
        teammate1_k_a = None
        teammate1_headgear_main = None
        teammate1_headgear_sub0 = None
        teammate1_headgear_sub1 = None
        teammate1_headgear_sub2 = None
        teammate1_clothes_main = None
        teammate1_clothes_sub0 = None
        teammate1_clothes_sub1 = None
        teammate1_clothes_sub2 = None
        teammate1_shoes_main = None
        teammate1_shoes_sub0 = None
        teammate1_shoes_sub1 = None
        teammate1_shoes_sub2 = None
    if battle.teammate2_splatnet_id is not None:
        teammate2_k_a = battle.teammate2_kills + battle.teammate2_assists
        teammate2_headgear_main = static(
            "two_battles/abilities/mains/" + battle.teammate2_headgear_main + ".png"
        )
        if battle.teammate2_headgear_sub0 is not None:
            teammate2_headgear_sub0 = static(
                "two_battles/abilities/subs/" + battle.teammate2_headgear_sub0 + ".png"
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
        teammate2_clothes_main = static(
            "two_battles/abilities/mains/" + battle.teammate2_clothes_main + ".png"
        )
        if battle.teammate2_clothes_sub0 is not None:
            teammate2_clothes_sub0 = static(
                "two_battles/abilities/subs/" + battle.teammate2_clothes_sub0 + ".png"
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
        teammate2_shoes_main = static(
            "two_battles/abilities/mains/" + battle.teammate2_shoes_main + ".png"
        )
        if battle.teammate2_shoes_sub0 is not None:
            teammate2_shoes_sub0 = static(
                "two_battles/abilities/subs/" + battle.teammate2_shoes_sub0 + ".png"
            )
            if battle.teammate2_shoes_sub1 is not None:
                teammate2_shoes_sub1 = static(
                    "two_battles/abilities/subs/" + battle.teammate2_shoes_sub1 + ".png"
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
        teammate2_k_a = None
        teammate2_headgear_main = None
        teammate2_headgear_sub0 = None
        teammate2_headgear_sub1 = None
        teammate2_headgear_sub2 = None
        teammate2_clothes_main = None
        teammate2_clothes_sub0 = None
        teammate2_clothes_sub1 = None
        teammate2_clothes_sub2 = None
        teammate2_shoes_main = None
        teammate2_shoes_sub0 = None
        teammate2_shoes_sub1 = None
        teammate2_shoes_sub2 = None
    if battle.teammate3_splatnet_id is not None:
        teammate3_k_a = battle.teammate3_kills + battle.teammate3_assists
        teammate3_headgear_main = static(
            "two_battles/abilities/mains/" + battle.teammate3_headgear_main + ".png"
        )
        if battle.teammate3_headgear_sub0 is not None:
            teammate3_headgear_sub0 = static(
                "two_battles/abilities/subs/" + battle.teammate3_headgear_sub0 + ".png"
            )
            if battle.teammate3_headgear_sub1 is not None:
                teammate3_headgear_sub1 = static(
                    "two_battles/abilities/subs/"
                    + battle.teammate3_headgear_sub1
                    + ".png"
                )
                if battle.teammate3_headgear_sub2 is not None:
                    teammate3_headgear_sub2 = static(
                        "two_battles/abilities/subs/"
                        + battle.teammate3_headgear_sub2
                        + ".png"
                    )
                else:
                    teammate3_headgear_sub2 = None
            else:
                teammate3_headgear_sub1 = None
                teammate3_headgear_sub2 = None
        else:
            teammate3_headgear_sub0 = None
            teammate3_headgear_sub1 = None
            teammate3_headgear_sub2 = None
        teammate3_clothes_main = static(
            "two_battles/abilities/mains/" + battle.teammate3_clothes_main + ".png"
        )
        if battle.teammate3_clothes_sub0 is not None:
            teammate3_clothes_sub0 = static(
                "two_battles/abilities/subs/" + battle.teammate3_clothes_sub0 + ".png"
            )
            if battle.teammate3_clothes_sub1 is not None:
                teammate3_clothes_sub1 = static(
                    "two_battles/abilities/subs/"
                    + battle.teammate3_clothes_sub1
                    + ".png"
                )
                if battle.teammate3_clothes_sub2 is not None:
                    teammate3_clothes_sub2 = static(
                        "two_battles/abilities/subs/"
                        + battle.teammate3_clothes_sub2
                        + ".png"
                    )
                else:
                    teammate3_clothes_sub2 = None
            else:
                teammate3_clothes_sub1 = None
                teammate3_clothes_sub2 = None
        else:
            teammate3_clothes_sub0 = None
            teammate3_clothes_sub1 = None
            teammate3_clothes_sub2 = None
        teammate3_shoes_main = static(
            "two_battles/abilities/mains/" + battle.teammate3_shoes_main + ".png"
        )
        if battle.teammate3_shoes_sub0 is not None:
            teammate3_shoes_sub0 = static(
                "two_battles/abilities/subs/" + battle.teammate3_shoes_sub0 + ".png"
            )
            if battle.teammate3_shoes_sub1 is not None:
                teammate3_shoes_sub1 = static(
                    "two_battles/abilities/subs/" + battle.teammate3_shoes_sub1 + ".png"
                )
                if battle.teammate3_shoes_sub2 is not None:
                    teammate3_shoes_sub2 = static(
                        "two_battles/abilities/subs/"
                        + battle.teammate3_shoes_sub2
                        + ".png"
                    )
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
        teammate3_k_a = None
        teammate3_headgear_main = None
        teammate3_headgear_sub0 = None
        teammate3_headgear_sub1 = None
        teammate3_headgear_sub2 = None
        teammate3_clothes_main = None
        teammate3_clothes_sub0 = None
        teammate3_clothes_sub1 = None
        teammate3_clothes_sub2 = None
        teammate3_shoes_main = None
        teammate3_shoes_sub0 = None
        teammate3_shoes_sub1 = None
        teammate3_shoes_sub2 = None
    if battle.opponent0_splatnet_id is not None:
        opponent0_k_a = battle.opponent0_kills + battle.opponent0_assists
        opponent0_headgear_main = static(
            "two_battles/abilities/mains/" + battle.opponent0_headgear_main + ".png"
        )
        if battle.opponent0_headgear_sub0 is not None:
            opponent0_headgear_sub0 = static(
                "two_battles/abilities/subs/" + battle.opponent0_headgear_sub0 + ".png"
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
        opponent0_clothes_main = static(
            "two_battles/abilities/mains/" + battle.opponent0_clothes_main + ".png"
        )
        if battle.opponent0_clothes_sub0 is not None:
            opponent0_clothes_sub0 = static(
                "two_battles/abilities/subs/" + battle.opponent0_clothes_sub0 + ".png"
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
        opponent0_shoes_main = static(
            "two_battles/abilities/mains/" + battle.opponent0_shoes_main + ".png"
        )
        if battle.opponent0_shoes_sub0 is not None:
            opponent0_shoes_sub0 = static(
                "two_battles/abilities/subs/" + battle.opponent0_shoes_sub0 + ".png"
            )
            if battle.opponent0_shoes_sub1 is not None:
                opponent0_shoes_sub1 = static(
                    "two_battles/abilities/subs/" + battle.opponent0_shoes_sub1 + ".png"
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
        opponent0_k_a = None
        opponent0_headgear_main = None
        opponent0_headgear_sub0 = None
        opponent0_headgear_sub1 = None
        opponent0_headgear_sub2 = None
        opponent0_clothes_main = None
        opponent0_clothes_sub0 = None
        opponent0_clothes_sub1 = None
        opponent0_clothes_sub2 = None
        opponent0_shoes_main = None
        opponent0_shoes_sub0 = None
        opponent0_shoes_sub1 = None
        opponent0_shoes_sub2 = None
    if battle.opponent1_splatnet_id is not None:
        opponent1_k_a = battle.opponent1_kills + battle.opponent1_assists
        opponent1_headgear_main = static(
            "two_battles/abilities/mains/" + battle.opponent1_headgear_main + ".png"
        )
        if battle.opponent1_headgear_sub0 is not None:
            opponent1_headgear_sub0 = static(
                "two_battles/abilities/subs/" + battle.opponent1_headgear_sub0 + ".png"
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
        opponent1_clothes_main = static(
            "two_battles/abilities/mains/" + battle.opponent1_clothes_main + ".png"
        )
        if battle.opponent1_clothes_sub0 is not None:
            opponent1_clothes_sub0 = static(
                "two_battles/abilities/subs/" + battle.opponent1_clothes_sub0 + ".png"
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
        opponent1_shoes_main = static(
            "two_battles/abilities/mains/" + battle.opponent1_shoes_main + ".png"
        )
        if battle.opponent1_shoes_sub0 is not None:
            opponent1_shoes_sub0 = static(
                "two_battles/abilities/subs/" + battle.opponent1_shoes_sub0 + ".png"
            )
            if battle.opponent1_shoes_sub1 is not None:
                opponent1_shoes_sub1 = static(
                    "two_battles/abilities/subs/" + battle.opponent1_shoes_sub1 + ".png"
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
        opponent1_k_a = None
        opponent1_headgear_main = None
        opponent1_headgear_sub0 = None
        opponent1_headgear_sub1 = None
        opponent1_headgear_sub2 = None
        opponent1_clothes_main = None
        opponent1_clothes_sub0 = None
        opponent1_clothes_sub1 = None
        opponent1_clothes_sub2 = None
        opponent1_shoes_main = None
        opponent1_shoes_sub0 = None
        opponent1_shoes_sub1 = None
        opponent1_shoes_sub2 = None
    if battle.opponent2_splatnet_id is not None:
        opponent2_k_a = battle.opponent2_kills + battle.opponent2_assists
        opponent2_headgear_main = static(
            "two_battles/abilities/mains/" + battle.opponent2_headgear_main + ".png"
        )
        if battle.opponent2_headgear_sub0 is not None:
            opponent2_headgear_sub0 = static(
                "two_battles/abilities/subs/" + battle.opponent2_headgear_sub0 + ".png"
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
        opponent2_clothes_main = static(
            "two_battles/abilities/mains/" + battle.opponent2_clothes_main + ".png"
        )
        if battle.opponent2_clothes_sub0 is not None:
            opponent2_clothes_sub0 = static(
                "two_battles/abilities/subs/" + battle.opponent2_clothes_sub0 + ".png"
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
        opponent2_shoes_main = static(
            "two_battles/abilities/mains/" + battle.opponent2_shoes_main + ".png"
        )
        if battle.opponent2_shoes_sub0 is not None:
            opponent2_shoes_sub0 = static(
                "two_battles/abilities/subs/" + battle.opponent2_shoes_sub0 + ".png"
            )
            if battle.opponent2_shoes_sub1 is not None:
                opponent2_shoes_sub1 = static(
                    "two_battles/abilities/subs/" + battle.opponent2_shoes_sub1 + ".png"
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
        opponent2_k_a = None
        opponent2_headgear_main = None
        opponent2_headgear_sub0 = None
        opponent2_headgear_sub1 = None
        opponent2_headgear_sub2 = None
        opponent2_clothes_main = None
        opponent2_clothes_sub0 = None
        opponent2_clothes_sub1 = None
        opponent2_clothes_sub2 = None
        opponent2_shoes_main = None
        opponent2_shoes_sub0 = None
        opponent2_shoes_sub1 = None
        opponent2_shoes_sub2 = None
    if battle.opponent3_splatnet_id is not None:
        opponent3_k_a = battle.opponent3_kills + battle.opponent3_assists
        opponent3_headgear_main = static(
            "two_battles/abilities/mains/" + battle.opponent3_headgear_main + ".png"
        )
        if battle.opponent3_headgear_sub0 is not None:
            opponent3_headgear_sub0 = static(
                "two_battles/abilities/subs/" + battle.opponent3_headgear_sub0 + ".png"
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
        opponent3_clothes_main = static(
            "two_battles/abilities/mains/" + battle.opponent3_clothes_main + ".png"
        )
        if battle.opponent3_clothes_sub0 is not None:
            opponent3_clothes_sub0 = static(
                "two_battles/abilities/subs/" + battle.opponent3_clothes_sub0 + ".png"
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
        opponent3_shoes_main = static(
            "two_battles/abilities/mains/" + battle.opponent3_shoes_main + ".png"
        )
        if battle.opponent3_shoes_sub0 is not None:
            opponent3_shoes_sub0 = static(
                "two_battles/abilities/subs/" + battle.opponent3_shoes_sub0 + ".png"
            )
            if battle.opponent3_shoes_sub1 is not None:
                opponent3_shoes_sub1 = static(
                    "two_battles/abilities/subs/" + battle.opponent3_shoes_sub1 + ".png"
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
        opponent3_k_a = None
        opponent3_headgear_main = None
        opponent3_headgear_sub0 = None
        opponent3_headgear_sub1 = None
        opponent3_headgear_sub2 = None
        opponent3_clothes_main = None
        opponent3_clothes_sub0 = None
        opponent3_clothes_sub1 = None
        opponent3_clothes_sub2 = None
        opponent3_shoes_main = None
        opponent3_shoes_sub0 = None
        opponent3_shoes_sub1 = None
        opponent3_shoes_sub2 = None

    return render(
        request,
        "two_battles/battle.html",
        {
            "battle": battle,
            "player_k_a": player_k_a,
            "player_headgear_main": player_headgear_main,
            "player_headgear_sub0": player_headgear_sub0,
            "player_headgear_sub1": player_headgear_sub1,
            "player_headgear_sub2": player_headgear_sub2,
            "player_clothes_main": player_clothes_main,
            "player_clothes_sub0": player_clothes_sub0,
            "player_clothes_sub1": player_clothes_sub1,
            "player_clothes_sub2": player_clothes_sub2,
            "player_shoes_main": player_shoes_main,
            "player_shoes_sub0": player_shoes_sub0,
            "player_shoes_sub1": player_shoes_sub1,
            "player_shoes_sub2": player_shoes_sub2,
            "teammate1_k_a": teammate1_k_a,
            "teammate1_headgear_main": teammate1_headgear_main,
            "teammate1_headgear_sub0": teammate1_headgear_sub0,
            "teammate1_headgear_sub1": teammate1_headgear_sub1,
            "teammate1_headgear_sub2": teammate1_headgear_sub2,
            "teammate1_clothes_main": teammate1_clothes_main,
            "teammate1_clothes_sub0": teammate1_clothes_sub0,
            "teammate1_clothes_sub1": teammate1_clothes_sub1,
            "teammate1_clothes_sub2": teammate1_clothes_sub2,
            "teammate1_shoes_main": teammate1_shoes_main,
            "teammate1_shoes_sub0": teammate1_shoes_sub0,
            "teammate1_shoes_sub1": teammate1_shoes_sub1,
            "teammate1_shoes_sub2": teammate1_shoes_sub2,
            "teammate2_k_a": teammate2_k_a,
            "teammate2_headgear_main": teammate2_headgear_main,
            "teammate2_headgear_sub0": teammate2_headgear_sub0,
            "teammate2_headgear_sub1": teammate2_headgear_sub1,
            "teammate2_headgear_sub2": teammate2_headgear_sub2,
            "teammate2_clothes_main": teammate2_clothes_main,
            "teammate2_clothes_sub0": teammate2_clothes_sub0,
            "teammate2_clothes_sub1": teammate2_clothes_sub1,
            "teammate2_clothes_sub2": teammate2_clothes_sub2,
            "teammate2_shoes_main": teammate2_shoes_main,
            "teammate2_shoes_sub0": teammate2_shoes_sub0,
            "teammate2_shoes_sub1": teammate2_shoes_sub1,
            "teammate2_shoes_sub2": teammate2_shoes_sub2,
            "teammate3_k_a": teammate3_k_a,
            "teammate3_headgear_main": teammate3_headgear_main,
            "teammate3_headgear_sub0": teammate3_headgear_sub0,
            "teammate3_headgear_sub1": teammate3_headgear_sub1,
            "teammate3_headgear_sub2": teammate3_headgear_sub2,
            "teammate3_clothes_main": teammate3_clothes_main,
            "teammate3_clothes_sub0": teammate3_clothes_sub0,
            "teammate3_clothes_sub1": teammate3_clothes_sub1,
            "teammate3_clothes_sub2": teammate3_clothes_sub2,
            "teammate3_shoes_main": teammate3_shoes_main,
            "teammate3_shoes_sub0": teammate3_shoes_sub0,
            "teammate3_shoes_sub1": teammate3_shoes_sub1,
            "teammate3_shoes_sub2": teammate3_shoes_sub2,
            "opponent0_k_a": opponent0_k_a,
            "opponent0_headgear_main": opponent0_headgear_main,
            "opponent0_headgear_sub0": opponent0_headgear_sub0,
            "opponent0_headgear_sub1": opponent0_headgear_sub1,
            "opponent0_headgear_sub2": opponent0_headgear_sub2,
            "opponent0_clothes_main": opponent0_clothes_main,
            "opponent0_clothes_sub0": opponent0_clothes_sub0,
            "opponent0_clothes_sub1": opponent0_clothes_sub1,
            "opponent0_clothes_sub2": opponent0_clothes_sub2,
            "opponent0_shoes_main": opponent0_shoes_main,
            "opponent0_shoes_sub0": opponent0_shoes_sub0,
            "opponent0_shoes_sub1": opponent0_shoes_sub1,
            "opponent0_shoes_sub2": opponent0_shoes_sub2,
            "opponent1_k_a": opponent1_k_a,
            "opponent1_headgear_main": opponent1_headgear_main,
            "opponent1_headgear_sub0": opponent1_headgear_sub0,
            "opponent1_headgear_sub1": opponent1_headgear_sub1,
            "opponent1_headgear_sub2": opponent1_headgear_sub2,
            "opponent1_clothes_main": opponent1_clothes_main,
            "opponent1_clothes_sub0": opponent1_clothes_sub0,
            "opponent1_clothes_sub1": opponent1_clothes_sub1,
            "opponent1_clothes_sub2": opponent1_clothes_sub2,
            "opponent1_shoes_main": opponent1_shoes_main,
            "opponent1_shoes_sub0": opponent1_shoes_sub0,
            "opponent1_shoes_sub1": opponent1_shoes_sub1,
            "opponent1_shoes_sub2": opponent1_shoes_sub2,
            "opponent2_k_a": opponent2_k_a,
            "opponent2_headgear_main": opponent2_headgear_main,
            "opponent2_headgear_sub0": opponent2_headgear_sub0,
            "opponent2_headgear_sub1": opponent2_headgear_sub1,
            "opponent2_headgear_sub2": opponent2_headgear_sub2,
            "opponent2_clothes_main": opponent2_clothes_main,
            "opponent2_clothes_sub0": opponent2_clothes_sub0,
            "opponent2_clothes_sub1": opponent2_clothes_sub1,
            "opponent2_clothes_sub2": opponent2_clothes_sub2,
            "opponent2_shoes_main": opponent2_shoes_main,
            "opponent2_shoes_sub0": opponent2_shoes_sub0,
            "opponent2_shoes_sub1": opponent2_shoes_sub1,
            "opponent2_shoes_sub2": opponent2_shoes_sub2,
            "opponent3_k_a": opponent3_k_a,
            "opponent3_headgear_main": opponent3_headgear_main,
            "opponent3_headgear_sub0": opponent3_headgear_sub0,
            "opponent3_headgear_sub1": opponent3_headgear_sub1,
            "opponent3_headgear_sub2": opponent3_headgear_sub2,
            "opponent3_clothes_main": opponent3_clothes_main,
            "opponent3_clothes_sub0": opponent3_clothes_sub0,
            "opponent3_clothes_sub1": opponent3_clothes_sub1,
            "opponent3_clothes_sub2": opponent3_clothes_sub2,
            "opponent3_shoes_main": opponent3_shoes_main,
            "opponent3_shoes_sub0": opponent3_shoes_sub0,
            "opponent3_shoes_sub1": opponent3_shoes_sub1,
            "opponent3_shoes_sub2": opponent3_shoes_sub2,
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
        Battle.create(
            splatnet_json=json.loads(request.data.get("splatnet_json", None)),
            image_result=image_result,
            image_gear=image_gear,
            user=request.user,
        )
        return Response(data=None, status=status.HTTP_200_OK)
