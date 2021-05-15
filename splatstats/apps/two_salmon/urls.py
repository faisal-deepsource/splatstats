from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"shifts", views.ShiftViewSet)

urlpatterns = [
    #path("", views.index, name="index"),
    #path("<int:id>/", views.detail, name="detail"),
    path("api/", include(router.urls)),
    #path("advanced_search/", views.advanced_search, name="advanced_search"),
    #path("user/<int:id>/", views.index_user, name="user_shifts"),
]
