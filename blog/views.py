from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render

from blog.forms import TicketForm
from blog.models import Ticket

@login_required
def home(request):
    return render(request, 'blog/home.html')

@login_required
def create_ticket(request: HttpRequest):
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket: Ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            messages.success(request, f"Votre ticket a bien été créé.")
            return redirect('ticket_detail', ticket_id=ticket.pk)
    else:
        form = TicketForm()
    return render(request, 'blog/create_ticket.html', {'form': form})

def ticket_detail(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    return render(request, 'blog/ticket_detail.html', {'ticket': ticket})

def edit_ticket(request:HttpRequest, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            ticket:Ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            messages.success(request, f"Votre ticket a bien été modifié.")
            return redirect('ticket_detail', ticket_id=ticket.pk)
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'blog/edit_ticket.html', {'form': form})

def delete_ticket(request: HttpRequest, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if request.method == 'POST':
        ticket.delete()
        messages.success(request, "Votre ticket a bien été supprimé.")
        return redirect('home')
    return render(request, 'blog/delete_ticket.html', {'ticket': ticket})