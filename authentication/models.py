from django.contrib.auth.models import AbstractUser
from django.db import models


class LITUser(AbstractUser):
    follows = models.ManyToManyField(
        "self",
        symmetrical=False,
        verbose_name="suit",
        related_name="suivi_par",
        blank=True,
    )
