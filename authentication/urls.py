from django.urls import path
from .views import SignUpView, subscription_view

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("subscription/", subscription_view, name="subscription"),
]
