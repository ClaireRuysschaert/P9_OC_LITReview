from django.urls import path, include
import blog.views

urlpatterns = [
    path("", blog.views.home, name="home"),
    path("create_ticket/", blog.views.create_ticket, name="create_ticket"),
    path("ticket/<int:ticket_id>/", blog.views.ticket_detail, name="ticket_detail"),
]