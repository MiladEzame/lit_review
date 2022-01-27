from django.shortcuts import render, redirect
from tickets.models import Ticket
from .forms import TicketForm

# Create your views here.
def dashboard(request):
    tickets = Ticket.objects.all()
    return render(request, 'tickets/dashboard.html',
                  context={'tickets' : tickets})

def tickets(request):
    tickets = Ticket.objects.all()
    return render(request, 'tickets/tickets.html',
                  context={'tickets' : tickets})

def show(request, pk):
    ticket = Ticket.objects.get(id=pk)

    context = {'ticket': ticket}
    return render(request, 'tickets/show.html', context)

def home(request):
    return render(request, 'tickets/home.html')

def createTicket(request):

    form = TicketForm()
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('tickets')

    context = {'form': form}
    return render(request, 'tickets/create_ticket.html', context)

def updateTicket(request, pk):

    ticket = Ticket.objects.get(id=pk)
    form = TicketForm(instance=ticket)
    if request.method == "POST":
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect ('tickets')

    context = {'form': form}
    return render(request, 'tickets/create_ticket.html', context)
