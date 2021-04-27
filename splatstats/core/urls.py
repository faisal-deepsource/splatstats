"""splatstats URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from two_factor.urls import urlpatterns as tf_urls
from rest_framework.authtoken import views
from django.conf import settings
from django.conf.urls.static import static
import sys

sys.path.append("..")
from site_auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(tf_urls)),
    path("api-auth/", include("rest_framework.urls")),
    path("two_battles/", include("two_battles.urls")),
    path("api-token-auth/", views.obtain_auth_token),
    url(r"^signup/$", auth_views.signup, name="signup"),
    url(
        r"^account_activation_sent/$",
        auth_views.account_activation_sent,
        name="account_activation_sent",
    ),
    url(
        r"^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,32})/$",
        auth_views.activate,
        name="activate",
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
