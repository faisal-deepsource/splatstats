from django.contrib.auth.models import User
from django.core.paginator import Paginator
import urllib
from django.shortcuts import get_object_or_404, render
from .models import Shift
from rest_framework import viewsets
from .serializers import ShiftSerializer
from rest_framework import permissions
from ...permissions import IsOwnerOrReadOnly
from .advanced_search_language import Lexer, Interpreter
from .forms import FilterForm, AdvancedFilterForm
from .objects import Wave, Player, Boss

# Create your views here.
class ShiftViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(player_user=self.request.user)


def index(request):
    form = FilterForm(request.GET)
    attributes = ""
    if form.is_valid():
        if "query" in form.cleaned_data and form.cleaned_data["query"] != "":
            query = urllib.parse.quote(form.cleaned_data["query"])
            lexer = Lexer(query)
            interpreter = Interpreter(lexer)
            battles = interpreter.interpret()
            battles = battles.order_by("-playtime")
            attributes = ""
        else:
            attributes = ""
            shifts = Shift.objects.order_by("-playtime")
            if form.cleaned_data["rule"] != "all":
                shifts = shifts.filter(rule=form.cleaned_data["rule"])
            if form.cleaned_data["match_type"] != "all":
                shifts = shifts.filter(match_type=form.cleaned_data["match_type"])
            if form.cleaned_data["stage"] != "all":
                shifts = shifts.filter(stage=form.cleaned_data["stage"])
            if form.cleaned_data["rank"] != "21":
                shifts = shifts.filter(player_rank=int(form.cleaned_data["rank"]))
            if form.cleaned_data["weapon"] != "all":
                shifts = shifts.filter(player_weapon=form.cleaned_data["weapon"])
            query = ""
            attributes += "&rule=" + form.cleaned_data["rule"]
            attributes += "&match_type=" + form.cleaned_data["match_type"]
            attributes += "&stage=" + form.cleaned_data["stage"]
            attributes += "&rank=" + form.cleaned_data["rank"]
            attributes += "&weapon=" + form.cleaned_data["weapon"]
        shifts = shifts.order_by("-playtime")
    else:
        query = ""
        shifts = Shift.objects.order_by("-playtime")
        attributes = ""
    paginator = Paginator(shifts, 50)  # Show 50 shifts per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    time_vals = []
    team_golden = []
    team_power = []
    for shift in page_obj:
        if shift.playtime is not None:
            time_vals.append(shift.playtime.strftime("%Y-%m-%d %H:%M:%S"))
        else:
            time_vals.append(None)
        team_golden.append(
            int(shift.wave_1_golden_delivered or 0)
            + int(shift.wave_2_golden_delivered or 0)
            + int(shift.wave_3_golden_delivered or 0)
        )
        team_power.append(
            int(shift.wave_1_power_eggs or 0)
            + int(shift.wave_2_power_eggs or 0)
            + int(shift.wave_3_power_eggs or 0)
        )
    context = {
        "page_obj": page_obj,
        "my_list": zip(
            page_obj,
            team_golden,
            team_power,
            time_vals,
        ),
        "form": form,
        "query": query,
        "attributes": attributes,
    }
    return render(request, "two_salmon/index.html", context)


def detail(request, id):
    shift = get_object_or_404(Shift, pk=id)
    context = {
        "shift": shift,
        "shift_players": [
            Player(
                shift.player_name,
                shift.player_weapon_w1,
                shift.player_weapon_w2,
                shift.player_weapon_w3,
                shift.player_special,
                shift.player_w1_specials,
                shift.player_w2_specials,
                shift.player_w3_specials,
                shift.player_revive_count,
                shift.player_death_count,
                shift.player_golden_eggs,
                shift.player_power_eggs,
            )
        ],
        "shift_bosses": (
            Boss(
                "Drizzler",
                shift.drizzler_count,
                shift.player_drizzler_kills,
                shift.teammate0_drizzler_kills,
                shift.teammate1_drizzler_kills,
                shift.teammate2_drizzler_kills,
            ),
            Boss(
                "Flyfish",
                shift.flyfish_count,
                shift.player_flyfish_kills,
                shift.teammate0_flyfish_kills,
                shift.teammate1_flyfish_kills,
                shift.teammate2_flyfish_kills,
            ),
            Boss(
                "Goldie",
                shift.goldie_count,
                shift.player_goldie_kills,
                shift.teammate0_goldie_kills,
                shift.teammate1_goldie_kills,
                shift.teammate2_goldie_kills,
            ),
            Boss(
                "Griller",
                shift.griller_count,
                shift.player_griller_kills,
                shift.teammate0_griller_kills,
                shift.teammate1_griller_kills,
                shift.teammate2_griller_kills,
            ),
            Boss(
                "Maws",
                shift.maws_count,
                shift.player_maws_kills,
                shift.teammate0_maws_kills,
                shift.teammate1_maws_kills,
                shift.teammate2_maws_kills,
            ),
            Boss(
                "Scrapper",
                shift.scrapper_count,
                shift.player_scrapper_kills,
                shift.teammate0_scrapper_kills,
                shift.teammate1_scrapper_kills,
                shift.teammate2_scrapper_kills,
            ),
            Boss(
                "Steelhead",
                shift.steelhead_count,
                shift.player_steelhead_kills,
                shift.teammate0_steelhead_kills,
                shift.teammate1_steelhead_kills,
                shift.teammate2_steelhead_kills,
            ),
            Boss(
                "Steel Eel",
                shift.steel_eel_count,
                shift.player_steel_eel_kills,
                shift.teammate0_steel_eel_kills,
                shift.teammate1_steel_eel_kills,
                shift.teammate2_steel_eel_kills,
            ),
            Boss(
                "Stinger",
                shift.stinger_count,
                shift.player_stinger_kills,
                shift.teammate0_stinger_kills,
                shift.teammate1_stinger_kills,
                shift.teammate2_stinger_kills,
            ),
        ),
        "result": "Cleared"
        if shift.is_clear
        else "Failed on {}, {}".format(
            shift.failure_wave, shift.get_job_failure_reason_display()
        ),
        "shift_waves": [
            Wave(
                1,
                shift.wave_1_event_type,
                shift.wave_1_water_level,
                shift.wave_1_quota,
                shift.wave_1_golden_delivered,
                shift.wave_1_golden_appear,
                shift.wave_1_power_eggs,
            )
        ],
    }
    if shift.failure_wave is None or shift.failure_wave > 1:
        context["shift_waves"].append(
            Wave(
                2,
                shift.wave_2_event_type,
                shift.wave_2_water_level,
                shift.wave_2_quota,
                shift.wave_2_golden_delivered,
                shift.wave_2_golden_appear,
                shift.wave_2_power_eggs,
            )
        )
        if shift.failure_wave is None or shift.failure_wave > 2:
            context["shift_waves"].append(
                Wave(
                    3,
                    shift.wave_3_event_type,
                    shift.wave_3_water_level,
                    shift.wave_3_quota,
                    shift.wave_3_golden_delivered,
                    shift.wave_3_golden_appear,
                    shift.wave_3_power_eggs,
                )
            )
    if shift.teammate0_name is not None:
        context["shift_players"].append(
            Player(
                shift.teammate0_name,
                shift.teammate0_weapon_w1,
                shift.teammate0_weapon_w2,
                shift.teammate0_weapon_w3,
                shift.teammate0_special,
                shift.teammate0_w1_specials,
                shift.teammate0_w2_specials,
                shift.teammate0_w3_specials,
                shift.teammate0_revive_count,
                shift.teammate0_death_count,
                shift.teammate0_golden_eggs,
                shift.teammate0_power_eggs,
            )
        )
        if shift.teammate1_name is not None:
            context["shift_players"].append(
                Player(
                    shift.teammate1_name,
                    shift.teammate1_weapon_w1,
                    shift.teammate1_weapon_w2,
                    shift.teammate1_weapon_w3,
                    shift.teammate1_special,
                    shift.teammate1_w1_specials,
                    shift.teammate1_w2_specials,
                    shift.teammate1_w3_specials,
                    shift.teammate1_revive_count,
                    shift.teammate1_death_count,
                    shift.teammate1_golden_eggs,
                    shift.teammate1_power_eggs,
                )
            )
            if shift.teammate2_name is not None:
                context["shift_players"].append(
                    Player(
                        shift.teammate2_name,
                        shift.teammate2_weapon_w1,
                        shift.teammate2_weapon_w2,
                        shift.teammate2_weapon_w3,
                        shift.teammate2_special,
                        shift.teammate2_w1_specials,
                        shift.teammate2_w2_specials,
                        shift.teammate2_w3_specials,
                        shift.teammate2_revive_count,
                        shift.teammate2_death_count,
                        shift.teammate2_golden_eggs,
                        shift.teammate2_power_eggs,
                    )
                )
    return render(request, "two_salmon/shift.html", context)


def index_user(request, id):
    form = FilterForm(request.GET)
    attributes = ""
    if form.is_valid():
        if "query" in form.cleaned_data and form.cleaned_data["query"] != "":
            query = urllib.parse.quote(form.cleaned_data["query"])
            lexer = Lexer(query)
            interpreter = Interpreter(lexer)
            battles = interpreter.interpret()
            battles = battles.filter(player_user=User.objects.get(pk=id)).order_by(
                "-playtime"
            )
            attributes = ""
        else:
            attributes = ""
            shifts = Shift.objects.filter(player_user=User.objects.get(pk=id)).order_by(
                "-playtime"
            )
            if form.cleaned_data["rule"] != "all":
                shifts = shifts.filter(rule=form.cleaned_data["rule"])
            if form.cleaned_data["match_type"] != "all":
                shifts = shifts.filter(match_type=form.cleaned_data["match_type"])
            if form.cleaned_data["stage"] != "all":
                shifts = shifts.filter(stage=form.cleaned_data["stage"])
            if form.cleaned_data["rank"] != "21":
                shifts = shifts.filter(player_rank=int(form.cleaned_data["rank"]))
            if form.cleaned_data["weapon"] != "all":
                shifts = shifts.filter(player_weapon=form.cleaned_data["weapon"])
            query = ""
            attributes += "&rule=" + form.cleaned_data["rule"]
            attributes += "&match_type=" + form.cleaned_data["match_type"]
            attributes += "&stage=" + form.cleaned_data["stage"]
            attributes += "&rank=" + form.cleaned_data["rank"]
            attributes += "&weapon=" + form.cleaned_data["weapon"]
        shifts = shifts.order_by("-playtime")
    else:
        query = ""
        shifts = Shift.objects.filter(player_user=User.objects.get(pk=id)).order_by(
            "-playtime"
        )
        attributes = ""
    paginator = Paginator(shifts, 50)  # Show 50 shifts per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    time_vals = []
    team_golden = []
    team_power = []
    for shift in page_obj:
        if shift.playtime is not None:
            time_vals.append(shift.playtime.strftime("%Y-%m-%d %H:%M:%S"))
        else:
            time_vals.append(None)
        team_golden.append(
            int(shift.wave_1_golden_delivered or 0)
            + int(shift.wave_2_golden_delivered or 0)
            + int(shift.wave_3_golden_delivered or 0)
        )
        team_power.append(
            int(shift.wave_1_power_eggs or 0)
            + int(shift.wave_2_power_eggs or 0)
            + int(shift.wave_3_power_eggs or 0)
        )
    context = {
        "page_obj": page_obj,
        "my_list": zip(
            page_obj,
            team_golden,
            team_power,
            time_vals,
        ),
        "form": form,
        "query": query,
        "attributes": attributes,
    }
    return render(request, "two_salmon/index.html", context)


def advanced_search(request):
    form = AdvancedFilterForm(request.GET)
    if form.is_valid():
        lexer = Lexer(form.cleaned_data["query"])
        interpreter = Interpreter(lexer)
        shifts = interpreter.interpret()
        if request.user.is_authenticated:
            shifts = shifts.filter(player_user=request.user).order_by("-playtime")
        else:
            shifts = shifts.order_by("-playtime")
        paginator = Paginator(shifts, 50)  # Show 50 battles per page
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        time_vals = []
        team_golden = []
        team_power = []
        for shift in page_obj:
            if shift.playtime is not None:
                time_vals.append(shift.playtime.strftime("%Y-%m-%d %H:%M:%S"))
            else:
                time_vals.append(None)
            team_golden.append(
                int(shift.wave_1_golden_delivered or 0)
                + int(shift.wave_2_golden_delivered or 0)
                + int(shift.wave_3_golden_delivered or 0)
            )
            team_power.append(
                int(shift.wave_1_power_eggs or 0)
                + int(shift.wave_2_power_eggs or 0)
                + int(shift.wave_3_power_eggs or 0)
            )
        query = urllib.parse.quote(form.cleaned_data["query"])
        context = {
            "page_obj": page_obj,
            "my_list": zip(
                page_obj,
                team_golden,
                team_power,
                time_vals,
            ),
            "form": form,
            "query": query,
            "attributes": "",
        }
        return render(request, "two_salmon/index.html", context)
    return render(request, "two_salmon/advanced_search.html", {"form": form})
