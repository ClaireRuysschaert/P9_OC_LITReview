from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    follows = models.ManyToManyField('self', symmetrical=False, verbose_name="suit", related_name="suivi par+")
    