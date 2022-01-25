from django.shortcuts import render
from tickets.models import Ticket

# Create your views here.
def index(request):
    tickets = Ticket.objects.all()
    return render(request, 'tickets/index.html',
                  context={'tickets' : tickets})

def home(request):
    return render(request, 'tickets/home.html')