from django.core.paginator import Paginator
from datetime import datetime
import urllib
from django.shortcuts import render
from .models import Shift
from rest_framework import viewsets
from .serializers import ShiftSerializer
from rest_framework import permissions
from ...permissions import IsOwnerOrReadOnly
from .advanced_search_language import Lexer, Interpreter
from .forms import FilterForm

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
            time_vals.append(
                shift.playtime.strftime("%Y-%m-%d %H:%M:%S")
            )
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
