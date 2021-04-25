from typing import SupportsAbs
from django.db import models
from django.utils.translation import gettext_lazy as _

class Species(models.TextChoices):
        ink = "inklings", _("Inkling")
        octo = "octolings", _("Octoling")

class Gender(models.TextChoices):
    girl = "girl", _("Female")
    boy = "boy", _("Male")