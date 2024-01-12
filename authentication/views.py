from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import LITUserCreationForm

class SignUpView(CreateView):
    form_class = LITUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "authentication/signup.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Votre compte a bien été créé, vous pouvez maintenant vous connecter.")
        return response
