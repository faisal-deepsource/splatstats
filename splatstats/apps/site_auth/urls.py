from django.conf.urls import url
from django.urls import path, include
from two_factor.urls import urlpatterns as tf_urls
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as token_views

router = DefaultRouter()
router.register(r"users", views.UserViewSet)

urlpatterns = [
    url(
        r"^account_activation_sent/$",
        views.account_activation_sent,
        name="account_activation_sent",
    ),
    path("api/", include("rest_framework.urls")),
    path("api/", include(router.urls)),
    url(r"^signup/$", views.signup, name="signup"),
    url(
        r"^account_activation_sent/$",
        views.account_activation_sent,
        name="account_activation_sent",
    ),
    url(
        r"^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,32})/$",
        views.activate,
        name="activate",
    ),
    path("", include(tf_urls)),
    path("api-token/", token_views.obtain_auth_token),
]
