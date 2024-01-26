from django.contrib import admin
from .models import Ticket, Review

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1

class TicketAdmin(admin.ModelAdmin):
    inlines = [ReviewInline]

admin.site.register(Ticket, TicketAdmin)
admin.site.register(Review)
