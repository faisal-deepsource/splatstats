from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:id>/", views.detail, name="detail"),
    path("upload/", views.upload, name="upload"),
    path("api/auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api/battles/", views.BattleAPIView.as_view()),
    path("advanced_search/", views.advanced_search, name="advanced_search"),
]
