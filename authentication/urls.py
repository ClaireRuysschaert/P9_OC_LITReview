from django.urls import path

from .views import SignUpView, subscription_view, unfollow_user

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("subscription/", subscription_view, name="subscription"),
    path("unfollow/<str:username>/", unfollow_user, name="unfollow"),
]
