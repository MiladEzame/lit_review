from django.shortcuts import render, redirect
from tickets.models import Ticket
from .forms import TicketForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from userfollows.models import UserFollow
from .filters import UserFilter
from .forms import CreateUserForm, LoginForm


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
    return render(request, 'tickets/update_ticket.html', context)


def deleteTicket(request, pk):

    ticket = Ticket.objects.get(id=pk)
    if request.method == "POST":
        ticket.delete()
        return redirect ('tickets')

    context = {'item': ticket}
    return render(request, 'tickets/delete_ticket.html', context)

def profile(request):
    users = User.objects.all()
    myFilter = UserFilter()

    user = User.objects.get(id=2)
    followers = UserFollow.objects.filter(followed_user = user).all()
    following = UserFollow.objects.filter(user = user).all()

    return render(request, 'tickets/profile.html',
                  context={
                      'users' : users, 
                      'myFilter': myFilter,
                      'followers': followers,
                      'following': following,
                      })

def show_user(request, pk):
    user = User.objects.get(id=pk)

    context = {'user': user}
    return render(request, 'tickets/show_user.html', context)

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')

    return render(request, 'tickets/login.html', context={'form': form})

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')

    return render(request, 'tickets/register.html', context={'form': form})