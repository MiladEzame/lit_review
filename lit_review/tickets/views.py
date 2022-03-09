from mimetypes import init
from .forms import CreateUserForm, LoginForm, CreateReviewForm
from .forms import TicketForm
from .filters import UserFilter
from tickets.models import Ticket
from django.shortcuts import get_object_or_404, render, redirect
from userfollows.models import UserFollow
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def dashboard(request):
    user = request.user
    tickets = Ticket.objects.all()
    followers_feed = UserFollow.objects.filter(followed_user = user).all()
    followings_feed = UserFollow.objects.filter(user = user).all()
    return render(request, 'tickets/dashboard.html',
                  context={'tickets': tickets,
                           'followers_feed': followers_feed,
                           'followings_feed': followings_feed})


def tickets(request):
    user = request.user
    tickets = user.ticket_set.all()
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
            obj = form.save(commit=False) 
            obj.user = User.objects.get(pk=request.user.id)
            obj.save() 
            return redirect ('tickets')

    context = {'form': form}
    return render(request, 'tickets/create_ticket.html', context)

#@login_required
def updateTicket(request, pk):

    ticket = Ticket.objects.get(id=pk)
    form = TicketForm()
    if request.method == "POST":
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            obj = form.save(commit=False) 
            obj.user = User.objects.get(pk=request.user.id)
            obj.save() 
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

    user = request.user
    followers = UserFollow.objects.filter(followed_user = user).all()
    following = UserFollow.objects.filter(user = user).all()

    if not request.user.is_authenticated:
        return redirect('login')
    else: 
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

def loginPage(request):
    form = LoginForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        context = {}    

        user = authenticate(request, username=username, password=password)
        if user is not None: 
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Username or Password incorrect', context)

    return render(request, 'tickets/login.html', context={'form': form})

def createReview(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if request.method == 'POST':
        form = CreateReviewForm(request.POST, instance=Ticket)
        if form.is_valid():
            obj = form.save(commit=False) 
            obj.user = User.objects.get(pk=request.user.id)
            obj.save() 
            return redirect ('dashboard')

    context = {'form': form}
    return render(request, 'dashboard/create_review', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')

            messages.success(request, 'Account was created for ' + user)
            return redirect('login')

    return render(request, 'tickets/register.html', context={'form': form})