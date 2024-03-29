from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import LITUserCreationForm, UserSearchForm
from .models import LITUser


class SignUpView(CreateView):
    form_class = LITUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "authentication/signup.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request,
            "Votre compte a bien été créé, vous pouvez maintenant vous connecter.",
        )
        return response


@login_required
def subscription_view(request: HttpRequest):
    user: LITUser = request.user  # type: ignore[assignment]
    form = UserSearchForm(request.GET)
    context = {"form": form, "users": None, "following": None, "followers": None}
    if form.is_valid():
        username = form.cleaned_data["username"]
        try:
            user_to_follow = LITUser.objects.get(username__iexact=username)
            user.follows.add(user_to_follow)
            user.save()
            context["users"] = user_to_follow  # type: ignore[assignment]
            messages.success(
                request, f"Vous suivez maintenant {user_to_follow.username}."
            )
        except LITUser.DoesNotExist:
            messages.error(request, "Cet utilisateur n'existe pas.")
    following = user.follows.all()
    context["following"] = following  # type: ignore[assignment]
    followers = user.followed_by.all()
    context["followers"] = followers  # type: ignore[assignment]
    return render(request, "authentication/subscription.html", context)


@login_required
def unfollow_user(request: HttpRequest, username: str):
    user: LITUser = request.user  # type: ignore[assignment]
    user_to_unfollow = get_object_or_404(LITUser, username__iexact=username)
    user.follows.remove(user_to_unfollow)
    messages.success(request, f"Vous ne suivez plus {user_to_unfollow.username}.")
    return redirect("subscription")
