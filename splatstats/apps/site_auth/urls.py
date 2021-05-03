from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r"^account_activation_sent/$",
        views.account_activation_sent,
        name="account_activation_sent",
    ),
]
