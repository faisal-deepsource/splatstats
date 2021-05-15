from django.shortcuts import render
from .models import Shift
from rest_framework import viewsets
from .serializers import ShiftSerializer
from rest_framework import permissions
from ...permissions import IsOwnerOrReadOnly

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
