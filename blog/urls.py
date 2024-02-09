from django.urls import path

import blog.views

urlpatterns = [
    path("", blog.views.flux, name="flux"),
    path("create_ticket/", blog.views.create_ticket, name="create_ticket"),
    path("ticket/<int:ticket_id>/", blog.views.ticket_detail, name="ticket_detail"),
    path("ticket/<int:ticket_id>/edit/", blog.views.edit_ticket, name="edit_ticket"),
    path(
        "ticket/<int:ticket_id>/delete/", blog.views.delete_ticket, name="delete_ticket"
    ),
    path("my_tickets/", blog.views.user_tickets_reviews, name="user_tickets_reviews"),
    path(
        "ticket/<int:ticket_id>/review/", blog.views.create_review, name="create_review"
    ),
    path("review/<int:review_id>/", blog.views.review_detail, name="review_detail"),
    path("review/<int:review_id>/edit/", blog.views.edit_review, name="edit_review"),
    path(
        "review/<int:review_id>/delete/", blog.views.delete_review, name="delete_review"
    ),
]
