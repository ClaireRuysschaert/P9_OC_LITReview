from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render
from authentication.models import LITUser
from itertools import chain

from blog.forms import TicketForm, ReviewForm
from blog.models import Review, Ticket

@login_required
def user_tickets_reviews(request: HttpRequest):
    user: LITUser = request.user
    tickets = Ticket.objects.filter(user=user)
    reviews = Review.objects.filter(user=user)
    items = sorted(
        chain(tickets, reviews), key=lambda item: item.created_on, reverse=True
    )
    return render(request, "blog/user_tickets_reviews.html", {"items": items})


@login_required
def flux(request: HttpRequest):
    user: LITUser = request.user
    user_tickets = Ticket.objects.filter(user=user).order_by("-id")
    following_users_tickets = Ticket.objects.filter(user__in=user.follows.all()).order_by("-id")
    tickets = user_tickets | following_users_tickets
    return render(request, "blog/user_tickets_reviews.html", {"tickets": tickets})


@login_required
def create_ticket(request: HttpRequest):
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket: Ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            messages.success(request, f"Votre ticket a bien été créé.")
            return redirect("ticket_detail", ticket_id=ticket.pk)
    else:
        form = TicketForm()
    return render(request, "blog/create_ticket.html", {"form": form})


def ticket_detail(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    return render(request, "blog/ticket_detail.html", {"ticket": ticket})


def edit_ticket(request: HttpRequest, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if ticket.user != request.user:
        messages.error(request, "You are not authorized to edit this ticket.")
        return redirect("ticket_detail", ticket_id=ticket.pk)
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            ticket: Ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            messages.success(request, f"Votre ticket a bien été modifié.")
            return redirect("ticket_detail", ticket_id=ticket.pk)
    else:
        form = TicketForm(instance=ticket)
    return render(request, "blog/edit_ticket.html", {"form": form})


def delete_ticket(request: HttpRequest, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if ticket.user != request.user:
        messages.error(request, "You are not authorized to delete this ticket.")
        return redirect("ticket_detail", ticket_id=ticket.pk)
    if request.method == "POST":
        ticket.delete()
        messages.success(request, "Votre ticket a bien été supprimé.")
        return redirect("flux")
    return render(request, "blog/delete_ticket.html", {"ticket": ticket})

@login_required
def create_review(request: HttpRequest, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review: Review = form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            messages.success(request, f"Votre critique a bien été créée.")
            return redirect("review_detail", ticket_id=ticket.pk, review_id=review.pk)
    else:
        form = ReviewForm()
    return render(request, "blog/create_review.html", {"form": form, "ticket": ticket})

def review_detail(request, ticket_id, review_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    review = get_object_or_404(Review, id=review_id)
    stars = list(range(1, review.rating + 1))
    empty_stars = list(range(1, 5 - review.rating + 1))
    return render(request, "blog/review_detail.html", {"ticket": ticket, "review": review, 'stars': stars, 'empty_stars': empty_stars})