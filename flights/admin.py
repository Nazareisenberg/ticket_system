from django.contrib import admin
from .models import Flight, Ticket

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ('flight_number', 'departure', 'destination', 'date', 'price')

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('user', 'flight', 'purchase_date')
