from django.contrib.auth.models import AbstractUser
from django.db import models


class LITUser(AbstractUser):
    follows = models.ManyToManyField(
        "self",
        symmetrical=False,
        related_name="followed_by",
        blank=True,
    )
    # backwards relationships
    followed_by: models.QuerySet["LITUser"]
