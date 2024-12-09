from django.shortcuts import render, get_object_or_404, redirect
from .models import Flight, Ticket
from django.contrib.auth.decorators import login_required
@login_required
def flight_list(request):
    flights = Flight.objects.all()
    return render(request, 'flights/flight_list.html', {'flights': flights})

@login_required
def book_ticket(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    Ticket.objects.create(user=request.user, flight=flight)
    return redirect('my_tickets')

@login_required
def my_tickets(request):
    tickets = Ticket.objects.filter(user=request.user)
    return render(request, 'flights/my_tickets.html', {'tickets': tickets})
