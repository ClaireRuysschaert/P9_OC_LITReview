from django.urls import path, include
import blog.views

urlpatterns = [
    path("", blog.views.home, name="home"),
]