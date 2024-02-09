from itertools import chain

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render

from authentication.models import LITUser
from blog.forms import ReviewForm, TicketForm
from blog.models import Review, Ticket


@login_required
def user_tickets_reviews(request: HttpRequest):
    user: LITUser = request.user  # type: ignore[assignment]
    tickets = Ticket.objects.filter(user=user)
    reviews = Review.objects.filter(user=user)
    items = sorted(
        chain(tickets, reviews), key=lambda item: item.created_on, reverse=True  # type: ignore[attr-defined]
    )
    return render(request, "blog/user_tickets_reviews.html", {"items": items})


@login_required
def flux(request: HttpRequest):
    user: LITUser = request.user  # type: ignore[assignment]
    user_tickets = Ticket.objects.filter(user=user)
    following_users_tickets = Ticket.objects.filter(user__in=user.follows.all())
    tickets = user_tickets | following_users_tickets
    user_reviews = Review.objects.filter(user=user)
    followers = user.followed_by.all()
    followers_reviews = Review.objects.filter(user__in=followers, ticket__user=user)
    reviews = user_reviews | followers_reviews
    items = sorted(
        chain(tickets, reviews), key=lambda item: item.created_on, reverse=True  # type: ignore[attr-defined]
    )
    return render(request, "blog/user_tickets_reviews.html", {"items": items})


@login_required
def create_ticket(request: HttpRequest):
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket: Ticket = form.save(commit=False)
            ticket.user = request.user  # type: ignore[assignment]
            ticket.save()
            messages.success(request, "Votre ticket a bien été créé.")
            return redirect("ticket_detail", ticket_id=ticket.pk)
    else:
        form = TicketForm()
    return render(request, "blog/create_ticket.html", {"form": form})


@login_required
def ticket_detail(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    return render(request, "blog/ticket_detail.html", {"ticket": ticket})


@login_required
def edit_ticket(request: HttpRequest, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if ticket.user != request.user:
        messages.error(request, "You are not authorized to edit this ticket.")
        return redirect("ticket_detail", ticket_id=ticket.pk)
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user  # type: ignore[assignment]
            ticket.save()
            messages.success(request, "Votre ticket a bien été modifié.")
            return redirect("ticket_detail", ticket_id=ticket.pk)
    else:
        form = TicketForm(instance=ticket)
    return render(request, "blog/edit_ticket.html", {"form": form})


@login_required
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
    if Review.objects.filter(user=request.user, ticket=ticket).exists():  # type: ignore[misc]
        messages.error(request, "Vous avez déjà posté une critique pour ce ticket.")
        return redirect("ticket_detail", ticket_id=ticket.pk)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review: Review = form.save(commit=False)
            review.user = request.user  # type: ignore[assignment]
            review.ticket = ticket
            review.save()
            messages.success(request, "Votre critique a bien été créée.")
            return redirect("review_detail", review_id=review.pk)
    else:
        form = ReviewForm()
    return render(request, "blog/create_review.html", {"form": form, "ticket": ticket})


@login_required
def review_detail(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    ticket = get_object_or_404(Ticket, id=review.ticket.pk)
    stars = list(range(1, review.rating + 1))
    empty_stars = list(range(1, 5 - review.rating + 1))
    return render(
        request,
        "blog/review_detail.html",
        {
            "ticket": ticket,
            "review": review,
            "stars": stars,
            "empty_stars": empty_stars,
        },
    )


@login_required
def edit_review(request: HttpRequest, review_id):
    review = get_object_or_404(Review, id=review_id)
    if review.user != request.user:
        messages.error(request, "You are not authorized to edit this review.")
        return redirect("review_detail", review_id=review.pk)
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user  # type: ignore[assignment]
            review.save()
            messages.success(request, "Votre critique a bien été modifié.")
            return redirect("review_detail", review_id=review.pk)
    else:
        form = ReviewForm(instance=review)
    return render(request, "blog/edit_review.html", {"form": form, "review": review})


@login_required
def delete_review(request: HttpRequest, review_id):
    review = get_object_or_404(Review, id=review_id)
    if review.user != request.user:
        messages.error(request, "You are not authorized to delete this review.")
        return redirect("review_detail", review_id=review.pk)
    if request.method == "POST":
        review.delete()
        messages.success(request, "Votre critique a bien été supprimé.")
        return redirect("flux")
    return render(request, "blog/delete_review.html", {"review": review})


@login_required
def create_ticket_and_review(request: HttpRequest):
    if request.method == "POST":
        ticket_form = TicketForm(request.POST, request.FILES)
        review_form = ReviewForm(request.POST)
        if ticket_form.is_valid() and review_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            messages.success(request, "Votre ticket et critique ont bien été créés.")
            return redirect("review_detail", review_id=review.pk)
    else:
        ticket_form = TicketForm()
        review_form = ReviewForm()
    return render(
        request,
        "blog/create_ticket_and_review.html",
        {"ticket_form": ticket_form, "review_form": review_form},
    )
