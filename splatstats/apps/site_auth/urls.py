from django.conf.urls import url
from django.urls import path, include
from two_factor.urls import urlpatterns as tf_urls
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as token_views
from django.contrib.auth import views as auth_views

router = DefaultRouter()
router.register(r"users", views.UserViewSet)

urlpatterns = [
    url(
        r"^account_activation_sent/$",
        views.account_activation_sent,
        name="account_activation_sent",
    ),
    path("api/", include(router.urls)),
    # path("api/", include("rest_framework.urls")),
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
    path("logout/", auth_views.LogoutView.as_view()),
    path("password_reset", auth_views.PasswordResetView.as_view()),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "password_reset_done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "password_reset_complete",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    path(
        "password_change",
        auth_views.PasswordChangeView.as_view(),
        name="password_change",
    ),
    path(
        "password_change_done",
        auth_views.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
]
