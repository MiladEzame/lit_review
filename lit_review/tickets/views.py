from django.shortcuts import render
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
    context = {'form': form}
    return render(request, 'tickets/create_order.html')

