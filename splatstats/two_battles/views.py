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


def index(request):
    latest_battles = Battle.objects.order_by("-time")
    context = {
        "latest_battles": latest_battles,
    }
    return render(request, "two_battles/index.html", context)


def detail(request, id):
    battle = get_object_or_404(Battle, pk=id)
    player_k_a = battle.player_kills + battle.player_assists
    player_headgear_main = (
        "two_battles/abilities/mains/" + battle.player_headgear_main + ".png"
    )
    player_headgear_sub0 = (
        "two_battles/abilities/subs/" + battle.player_headgear_sub0 + ".png"
    )
    player_headgear_sub1 = (
        "two_battles/abilities/subs/" + battle.player_headgear_sub1 + ".png"
    )
    player_headgear_sub2 = (
        "two_battles/abilities/subs/" + battle.player_headgear_sub2 + ".png"
    )
    player_clothes_main = (
        "two_battles/abilities/mains/" + battle.player_clothes_main + ".png"
    )
    player_clothes_sub0 = (
        "two_battles/abilities/subs/" + battle.player_clothes_sub0 + ".png"
    )
    player_clothes_sub1 = (
        "two_battles/abilities/subs/" + battle.player_clothes_sub1 + ".png"
    )
    player_clothes_sub2 = (
        "two_battles/abilities/subs/" + battle.player_clothes_sub2 + ".png"
    )
    player_shoes_main = (
        "two_battles/abilities/mains/" + battle.player_shoes_main + ".png"
    )
    player_shoes_sub0 = (
        "two_battles/abilities/subs/" + battle.player_shoes_sub0 + ".png"
    )
    player_shoes_sub1 = (
        "two_battles/abilities/subs/" + battle.player_shoes_sub1 + ".png"
    )
    player_shoes_sub2 = (
        "two_battles/abilities/subs/" + battle.player_shoes_sub2 + ".png"
    )
    teammate1_k_a = battle.teammate1_kills + battle.teammate1_assists
    teammate1_headgear_main = (
        "two_battles/abilities/mains/" + battle.teammate1_headgear_main + ".png"
    )
    teammate1_headgear_sub0 = (
        "two_battles/abilities/subs/" + battle.teammate1_headgear_sub0 + ".png"
    )
    teammate1_headgear_sub1 = (
        "two_battles/abilities/subs/" + battle.teammate1_headgear_sub1 + ".png"
    )
    teammate1_headgear_sub2 = (
        "two_battles/abilities/subs/" + battle.teammate1_headgear_sub2 + ".png"
    )
    teammate1_clothes_main = (
        "two_battles/abilities/mains/" + battle.teammate1_clothes_main + ".png"
    )
    teammate1_clothes_sub0 = (
        "two_battles/abilities/subs/" + battle.teammate1_clothes_sub0 + ".png"
    )
    teammate1_clothes_sub1 = (
        "two_battles/abilities/subs/" + battle.teammate1_clothes_sub1 + ".png"
    )
    teammate1_clothes_sub2 = (
        "two_battles/abilities/subs/" + battle.teammate1_clothes_sub2 + ".png"
    )
    teammate1_shoes_main = (
        "two_battles/abilities/mains/" + battle.teammate1_shoes_main + ".png"
    )
    teammate1_shoes_sub0 = (
        "two_battles/abilities/subs/" + battle.teammate1_shoes_sub0 + ".png"
    )
    teammate1_shoes_sub1 = (
        "two_battles/abilities/subs/" + battle.teammate1_shoes_sub1 + ".png"
    )
    teammate1_shoes_sub2 = (
        "two_battles/abilities/subs/" + battle.teammate1_shoes_sub2 + ".png"
    )
    teammate2_k_a = battle.teammate2_kills + battle.teammate2_assists
    teammate2_headgear_main = (
        "two_battles/abilities/mains/" + battle.teammate2_headgear_main + ".png"
    )
    teammate2_headgear_sub0 = (
        "two_battles/abilities/subs/" + battle.teammate2_headgear_sub0 + ".png"
    )
    teammate2_headgear_sub1 = (
        "two_battles/abilities/subs/" + battle.teammate2_headgear_sub1 + ".png"
    )
    teammate2_headgear_sub2 = (
        "two_battles/abilities/subs/" + battle.teammate2_headgear_sub2 + ".png"
    )
    teammate2_clothes_main = (
        "two_battles/abilities/mains/" + battle.teammate2_clothes_main + ".png"
    )
    teammate2_clothes_sub0 = (
        "two_battles/abilities/subs/" + battle.teammate2_clothes_sub0 + ".png"
    )
    teammate2_clothes_sub1 = (
        "two_battles/abilities/subs/" + battle.teammate2_clothes_sub1 + ".png"
    )
    teammate2_clothes_sub2 = (
        "two_battles/abilities/subs/" + battle.teammate2_clothes_sub2 + ".png"
    )
    teammate2_shoes_main = (
        "two_battles/abilities/mains/" + battle.teammate2_shoes_main + ".png"
    )
    teammate2_shoes_sub0 = (
        "two_battles/abilities/subs/" + battle.teammate2_shoes_sub0 + ".png"
    )
    teammate2_shoes_sub1 = (
        "two_battles/abilities/subs/" + battle.teammate2_shoes_sub1 + ".png"
    )
    teammate2_shoes_sub2 = (
        "two_battles/abilities/subs/" + battle.teammate2_shoes_sub2 + ".png"
    )
    teammate3_k_a = battle.teammate3_kills + battle.teammate3_assists
    teammate3_headgear_main = (
        "two_battles/abilities/mains/" + battle.teammate3_headgear_main + ".png"
    )
    teammate3_headgear_sub0 = (
        "two_battles/abilities/subs/" + battle.teammate3_headgear_sub0 + ".png"
    )
    teammate3_headgear_sub1 = (
        "two_battles/abilities/subs/" + battle.teammate3_headgear_sub1 + ".png"
    )
    teammate3_headgear_sub2 = (
        "two_battles/abilities/subs/" + battle.teammate3_headgear_sub2 + ".png"
    )
    teammate3_clothes_main = (
        "two_battles/abilities/mains/" + battle.teammate3_clothes_main + ".png"
    )
    teammate3_clothes_sub0 = (
        "two_battles/abilities/subs/" + battle.teammate3_clothes_sub0 + ".png"
    )
    teammate3_clothes_sub1 = (
        "two_battles/abilities/subs/" + battle.teammate3_clothes_sub1 + ".png"
    )
    teammate3_clothes_sub2 = (
        "two_battles/abilities/subs/" + battle.teammate3_clothes_sub2 + ".png"
    )
    teammate3_shoes_main = (
        "two_battles/abilities/mains/" + battle.teammate3_shoes_main + ".png"
    )
    teammate3_shoes_sub0 = (
        "two_battles/abilities/subs/" + battle.teammate3_shoes_sub0 + ".png"
    )
    teammate3_shoes_sub1 = (
        "two_battles/abilities/subs/" + battle.teammate3_shoes_sub1 + ".png"
    )
    teammate3_shoes_sub2 = (
        "two_battles/abilities/subs/" + battle.teammate3_shoes_sub2 + ".png"
    )
    opponent0_k_a = battle.opponent0_kills + battle.opponent0_assists
    opponent0_headgear_main = (
        "two_battles/abilities/mains/" + battle.opponent0_headgear_main + ".png"
    )
    opponent0_headgear_sub0 = (
        "two_battles/abilities/subs/" + battle.opponent0_headgear_sub0 + ".png"
    )
    opponent0_headgear_sub1 = (
        "two_battles/abilities/subs/" + battle.opponent0_headgear_sub1 + ".png"
    )
    opponent0_headgear_sub2 = (
        "two_battles/abilities/subs/" + battle.opponent0_headgear_sub2 + ".png"
    )
    opponent0_clothes_main = (
        "two_battles/abilities/mains/" + battle.opponent0_clothes_main + ".png"
    )
    opponent0_clothes_sub0 = (
        "two_battles/abilities/subs/" + battle.opponent0_clothes_sub0 + ".png"
    )
    opponent0_clothes_sub1 = (
        "two_battles/abilities/subs/" + battle.opponent0_clothes_sub1 + ".png"
    )
    opponent0_clothes_sub2 = (
        "two_battles/abilities/subs/" + battle.opponent0_clothes_sub2 + ".png"
    )
    opponent0_shoes_main = (
        "two_battles/abilities/mains/" + battle.opponent0_shoes_main + ".png"
    )
    opponent0_shoes_sub0 = (
        "two_battles/abilities/subs/" + battle.opponent0_shoes_sub0 + ".png"
    )
    opponent0_shoes_sub1 = (
        "two_battles/abilities/subs/" + battle.opponent0_shoes_sub1 + ".png"
    )
    opponent0_shoes_sub2 = (
        "two_battles/abilities/subs/" + battle.opponent0_shoes_sub2 + ".png"
    )
    opponent1_k_a = battle.opponent1_kills + battle.opponent1_assists
    opponent1_headgear_main = (
        "two_battles/abilities/mains/" + battle.opponent1_headgear_main + ".png"
    )
    opponent1_headgear_sub0 = (
        "two_battles/abilities/subs/" + battle.opponent1_headgear_sub0 + ".png"
    )
    opponent1_headgear_sub1 = (
        "two_battles/abilities/subs/" + battle.opponent1_headgear_sub1 + ".png"
    )
    opponent1_headgear_sub2 = (
        "two_battles/abilities/subs/" + battle.opponent1_headgear_sub2 + ".png"
    )
    opponent1_clothes_main = (
        "two_battles/abilities/mains/" + battle.opponent1_clothes_main + ".png"
    )
    opponent1_clothes_sub0 = (
        "two_battles/abilities/subs/" + battle.opponent1_clothes_sub0 + ".png"
    )
    opponent1_clothes_sub1 = (
        "two_battles/abilities/subs/" + battle.opponent1_clothes_sub1 + ".png"
    )
    opponent1_clothes_sub2 = (
        "two_battles/abilities/subs/" + battle.opponent1_clothes_sub2 + ".png"
    )
    opponent1_shoes_main = (
        "two_battles/abilities/mains/" + battle.opponent1_shoes_main + ".png"
    )
    opponent1_shoes_sub0 = (
        "two_battles/abilities/subs/" + battle.opponent1_shoes_sub0 + ".png"
    )
    opponent1_shoes_sub1 = (
        "two_battles/abilities/subs/" + battle.opponent1_shoes_sub1 + ".png"
    )
    opponent1_shoes_sub2 = (
        "two_battles/abilities/subs/" + battle.opponent1_shoes_sub2 + ".png"
    )
    opponent2_k_a = battle.opponent2_kills + battle.opponent2_assists
    opponent2_headgear_main = (
        "two_battles/abilities/mains/" + battle.opponent2_headgear_main + ".png"
    )
    opponent2_headgear_sub0 = (
        "two_battles/abilities/subs/" + battle.opponent2_headgear_sub0 + ".png"
    )
    opponent2_headgear_sub1 = (
        "two_battles/abilities/subs/" + battle.opponent2_headgear_sub1 + ".png"
    )
    opponent2_headgear_sub2 = (
        "two_battles/abilities/subs/" + battle.opponent2_headgear_sub2 + ".png"
    )
    opponent2_clothes_main = (
        "two_battles/abilities/mains/" + battle.opponent2_clothes_main + ".png"
    )
    opponent2_clothes_sub0 = (
        "two_battles/abilities/subs/" + battle.opponent2_clothes_sub0 + ".png"
    )
    opponent2_clothes_sub1 = (
        "two_battles/abilities/subs/" + battle.opponent2_clothes_sub1 + ".png"
    )
    opponent2_clothes_sub2 = (
        "two_battles/abilities/subs/" + battle.opponent2_clothes_sub2 + ".png"
    )
    opponent2_shoes_main = (
        "two_battles/abilities/mains/" + battle.opponent2_shoes_main + ".png"
    )
    opponent2_shoes_sub0 = (
        "two_battles/abilities/subs/" + battle.opponent2_shoes_sub0 + ".png"
    )
    opponent2_shoes_sub1 = (
        "two_battles/abilities/subs/" + battle.opponent2_shoes_sub1 + ".png"
    )
    opponent2_shoes_sub2 = (
        "two_battles/abilities/subs/" + battle.opponent2_shoes_sub2 + ".png"
    )
    opponent3_k_a = battle.opponent3_kills + battle.opponent3_assists
    opponent3_headgear_main = (
        "two_battles/abilities/mains/" + battle.opponent3_headgear_main + ".png"
    )
    opponent3_headgear_sub0 = (
        "two_battles/abilities/subs/" + battle.opponent3_headgear_sub0 + ".png"
    )
    opponent3_headgear_sub1 = (
        "two_battles/abilities/subs/" + battle.opponent3_headgear_sub1 + ".png"
    )
    opponent3_headgear_sub2 = (
        "two_battles/abilities/subs/" + battle.opponent3_headgear_sub2 + ".png"
    )
    opponent3_clothes_main = (
        "two_battles/abilities/mains/" + battle.opponent3_clothes_main + ".png"
    )
    opponent3_clothes_sub0 = (
        "two_battles/abilities/subs/" + battle.opponent3_clothes_sub0 + ".png"
    )
    opponent3_clothes_sub1 = (
        "two_battles/abilities/subs/" + battle.opponent3_clothes_sub1 + ".png"
    )
    opponent3_clothes_sub2 = (
        "two_battles/abilities/subs/" + battle.opponent3_clothes_sub2 + ".png"
    )
    opponent3_shoes_main = (
        "two_battles/abilities/mains/" + battle.opponent3_shoes_main + ".png"
    )
    opponent3_shoes_sub0 = (
        "two_battles/abilities/subs/" + battle.opponent3_shoes_sub0 + ".png"
    )
    opponent3_shoes_sub1 = (
        "two_battles/abilities/subs/" + battle.opponent3_shoes_sub1 + ".png"
    )
    opponent3_shoes_sub2 = (
        "two_battles/abilities/subs/" + battle.opponent3_shoes_sub2 + ".png"
    )
    return render(
        request,
        "two_battles/battle.html",
        {
            "battle": battle,
            "player_k_a": player_k_a,
            "player_headgear_main": static(player_headgear_main),
            "player_headgear_sub0": static(player_headgear_sub0),
            "player_headgear_sub1": static(player_headgear_sub1),
            "player_headgear_sub2": static(player_headgear_sub2),
            "player_clothes_main": static(player_clothes_main),
            "player_clothes_sub0": static(player_clothes_sub0),
            "player_clothes_sub1": static(player_clothes_sub1),
            "player_clothes_sub2": static(player_clothes_sub2),
            "player_shoes_main": static(player_shoes_main),
            "player_shoes_sub0": static(player_shoes_sub0),
            "player_shoes_sub1": static(player_shoes_sub1),
            "player_shoes_sub2": static(player_shoes_sub2),
            "teammate1_k_a": teammate1_k_a,
            "teammate1_headgear_main": static(teammate1_headgear_main),
            "teammate1_headgear_sub0": static(teammate1_headgear_sub0),
            "teammate1_headgear_sub1": static(teammate1_headgear_sub1),
            "teammate1_headgear_sub2": static(teammate1_headgear_sub2),
            "teammate1_clothes_main": static(teammate1_clothes_main),
            "teammate1_clothes_sub0": static(teammate1_clothes_sub0),
            "teammate1_clothes_sub1": static(teammate1_clothes_sub1),
            "teammate1_clothes_sub2": static(teammate1_clothes_sub2),
            "teammate1_shoes_main": static(teammate1_shoes_main),
            "teammate1_shoes_sub0": static(teammate1_shoes_sub0),
            "teammate1_shoes_sub1": static(teammate1_shoes_sub1),
            "teammate1_shoes_sub2": static(teammate1_shoes_sub2),
            "teammate2_k_a": teammate2_k_a,
            "teammate2_headgear_main": static(teammate2_headgear_main),
            "teammate2_headgear_sub0": static(teammate2_headgear_sub0),
            "teammate2_headgear_sub1": static(teammate2_headgear_sub1),
            "teammate2_headgear_sub2": static(teammate2_headgear_sub2),
            "teammate2_clothes_main": static(teammate2_clothes_main),
            "teammate2_clothes_sub0": static(teammate2_clothes_sub0),
            "teammate2_clothes_sub1": static(teammate2_clothes_sub1),
            "teammate2_clothes_sub2": static(teammate2_clothes_sub2),
            "teammate2_shoes_main": static(teammate2_shoes_main),
            "teammate2_shoes_sub0": static(teammate2_shoes_sub0),
            "teammate2_shoes_sub1": static(teammate2_shoes_sub1),
            "teammate2_shoes_sub2": static(teammate2_shoes_sub2),
            "teammate3_k_a": teammate3_k_a,
            "teammate3_headgear_main": static(teammate3_headgear_main),
            "teammate3_headgear_sub0": static(teammate3_headgear_sub0),
            "teammate3_headgear_sub1": static(teammate3_headgear_sub1),
            "teammate3_headgear_sub2": static(teammate3_headgear_sub2),
            "teammate3_clothes_main": static(teammate3_clothes_main),
            "teammate3_clothes_sub0": static(teammate3_clothes_sub0),
            "teammate3_clothes_sub1": static(teammate3_clothes_sub1),
            "teammate3_clothes_sub2": static(teammate3_clothes_sub2),
            "teammate3_shoes_main": static(teammate3_shoes_main),
            "teammate3_shoes_sub0": static(teammate3_shoes_sub0),
            "teammate3_shoes_sub1": static(teammate3_shoes_sub1),
            "teammate3_shoes_sub2": static(teammate3_shoes_sub2),
            "opponent0_k_a": opponent0_k_a,
            "opponent0_headgear_main": static(opponent0_headgear_main),
            "opponent0_headgear_sub0": static(opponent0_headgear_sub0),
            "opponent0_headgear_sub1": static(opponent0_headgear_sub1),
            "opponent0_headgear_sub2": static(opponent0_headgear_sub2),
            "opponent0_clothes_main": static(opponent0_clothes_main),
            "opponent0_clothes_sub0": static(opponent0_clothes_sub0),
            "opponent0_clothes_sub1": static(opponent0_clothes_sub1),
            "opponent0_clothes_sub2": static(opponent0_clothes_sub2),
            "opponent0_shoes_main": static(opponent0_shoes_main),
            "opponent0_shoes_sub0": static(opponent0_shoes_sub0),
            "opponent0_shoes_sub1": static(opponent0_shoes_sub1),
            "opponent0_shoes_sub2": static(opponent0_shoes_sub2),
            "opponent1_k_a": opponent1_k_a,
            "opponent1_headgear_main": static(opponent1_headgear_main),
            "opponent1_headgear_sub0": static(opponent1_headgear_sub0),
            "opponent1_headgear_sub1": static(opponent1_headgear_sub1),
            "opponent1_headgear_sub2": static(opponent1_headgear_sub2),
            "opponent1_clothes_main": static(opponent1_clothes_main),
            "opponent1_clothes_sub0": static(opponent1_clothes_sub0),
            "opponent1_clothes_sub1": static(opponent1_clothes_sub1),
            "opponent1_clothes_sub2": static(opponent1_clothes_sub2),
            "opponent1_shoes_main": static(opponent1_shoes_main),
            "opponent1_shoes_sub0": static(opponent1_shoes_sub0),
            "opponent1_shoes_sub1": static(opponent1_shoes_sub1),
            "opponent1_shoes_sub2": static(opponent1_shoes_sub2),
            "opponent2_k_a": opponent2_k_a,
            "opponent2_headgear_main": static(opponent2_headgear_main),
            "opponent2_headgear_sub0": static(opponent2_headgear_sub0),
            "opponent2_headgear_sub1": static(opponent2_headgear_sub1),
            "opponent2_headgear_sub2": static(opponent2_headgear_sub2),
            "opponent2_clothes_main": static(opponent2_clothes_main),
            "opponent2_clothes_sub0": static(opponent2_clothes_sub0),
            "opponent2_clothes_sub1": static(opponent2_clothes_sub1),
            "opponent2_clothes_sub2": static(opponent2_clothes_sub2),
            "opponent2_shoes_main": static(opponent2_shoes_main),
            "opponent2_shoes_sub0": static(opponent2_shoes_sub0),
            "opponent2_shoes_sub1": static(opponent2_shoes_sub1),
            "opponent2_shoes_sub2": static(opponent2_shoes_sub2),
            "opponent3_k_a": opponent3_k_a,
            "opponent3_headgear_main": static(opponent3_headgear_main),
            "opponent3_headgear_sub0": static(opponent3_headgear_sub0),
            "opponent3_headgear_sub1": static(opponent3_headgear_sub1),
            "opponent3_headgear_sub2": static(opponent3_headgear_sub2),
            "opponent3_clothes_main": static(opponent3_clothes_main),
            "opponent3_clothes_sub0": static(opponent3_clothes_sub0),
            "opponent3_clothes_sub1": static(opponent3_clothes_sub1),
            "opponent3_clothes_sub2": static(opponent3_clothes_sub2),
            "opponent3_shoes_main": static(opponent3_shoes_main),
            "opponent3_shoes_sub0": static(opponent3_shoes_sub0),
            "opponent3_shoes_sub1": static(opponent3_shoes_sub1),
            "opponent3_shoes_sub2": static(opponent3_shoes_sub2),
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
