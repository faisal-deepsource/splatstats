from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from splatstats.apps.two_battles.models import Battle as Two_Battle


class UserSerializer(serializers.HyperlinkedModelSerializer):
    two_battles = serializers.HyperlinkedRelatedField(
        many=True, view_name="battle-detail", read_only=True
    )

    class Meta:
        model = User
        fields = ["url", "id", "username", "two_battles"]
