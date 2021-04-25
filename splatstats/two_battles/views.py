from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics

from .serializers import BattleSerializer, UserSerializer
from .forms import BattleForm
from .models import Battle


def index(request):
    latest_battles = Battle.objects.order_by("-time")[:5]
    context = {
        "latest_battles": latest_battles,
    }
    return render(request, "two_battles/index.html", context)


def detail(request, id):
    battle = get_object_or_404(Battle, pk=id)
    return render(request, "two_battles/detail.html", {"battle": battle})


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


class BattleViewSet(viewsets.ModelViewSet):
    queryset = Battle.objects.all().order_by("id")
    serializer_class = BattleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Battle.objects.all().order_by("id").filter(player_user=user)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
