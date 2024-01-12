from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import LITUserCreationForm

class SignUpView(CreateView):
    form_class = LITUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "authentication/signup.html"