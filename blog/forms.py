from django import forms

from .models import Review, Ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["title", "description", "image"]
        labels = {
            "title": "Titre",
            "description": "Description",
            "image": "Image",
        }


class ReviewForm(forms.ModelForm):
    RATING_CHOICES = [(i, str(i)) for i in range(6)]
    rating = forms.ChoiceField(
        choices=RATING_CHOICES, widget=forms.RadioSelect, label="Note"
    )

    class Meta:
        model = Review
        fields = ["title", "rating", "content"]
        labels = {
            "title": "Titre",
            "content": "Commentaire",
            "rating": "Note",
        }
