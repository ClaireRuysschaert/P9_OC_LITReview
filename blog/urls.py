from django.urls import path, include
import blog.views

urlpatterns = [
    path("", blog.views.flux, name="flux"),
    path("create_ticket/", blog.views.create_ticket, name="create_ticket"),
    path("ticket/<int:ticket_id>/", blog.views.ticket_detail, name="ticket_detail"),
    path("ticket/<int:ticket_id>/edit/", blog.views.edit_ticket, name="edit_ticket"),
    path("ticket/<int:ticket_id>/delete/", blog.views.delete_ticket, name="delete_ticket"),
    path("my_tickets/", blog.views.display_all_user_tickets, name="display_all_user_tickets"),
    path("ticket/<int:ticket_id>/review/", blog.views.create_review, name="create_review"),
    path("ticket/<int:ticket_id>/review/<int:review_id>/", blog.views.review_detail, name="review_detail"),
]