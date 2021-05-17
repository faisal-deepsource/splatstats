from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    two_battles = serializers.HyperlinkedRelatedField(
        many=True, view_name="battle-detail", read_only=True
    )
    two_salmon = serializers.HyperlinkedRelatedField(
        many=True, view_name="shift-detail", read_only=True
    )

    class Meta:
        model = User
        fields = ["url", "id", "username", "two_battles", "two_salmon"]


class SocialSerializer(serializers.Serializer):
    """
    Serializer which accepts an OAuth2 access token.
    """
    access_token = serializers.CharField(
        allow_blank=False,
        trim_whitespace=True,
    )
