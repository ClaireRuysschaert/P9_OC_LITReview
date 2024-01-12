from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

class LITUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ("username", "email")
class LITUserChangeForm(UserChangeForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ("username", "email")