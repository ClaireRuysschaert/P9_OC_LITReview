from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from PIL import Image

from LITReview.settings import AUTH_USER_MODEL


class Ticket(models.Model):
    """User Asking's critics for a book or a litterary article."""

    user = models.ForeignKey(to=AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def rezise_image(self):
        image = Image.open(self.image)
        image.thumbnail((400, 400))
        image.save(self.image.path)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            self.rezise_image()


class Review(models.Model):
    """User's critics for a book or a litterary article."""

    user = models.ForeignKey(to=AUTH_USER_MODEL, on_delete=models.CASCADE)
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    rating = models.PositiveSmallIntegerField(
        blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    title = models.CharField(max_length=128)
    content = models.TextField(max_length=8192, blank=True)

    def __str__(self):
        return self.content
