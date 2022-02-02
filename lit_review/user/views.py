from django.shortcuts import render
from user.models import User
from .filters import UserFilter
from .forms import CreateUserForm, LoginForm

# Create your views here.
def profile(request):
    users = User.objects.all()
    myFilter = UserFilter()

    return render(request, 'user/profile.html',
                  context={'users' : users, 'myFilter': myFilter})

def show(request, pk):
    user = User.objects.get(id=pk)

    context = {'user': user}
    return render(request, 'user/show.html', context)

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid:
            form.save()

    return render(request, 'user/login.html', context={'form': form})

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid:
            form.save()

    return render(request, 'user/register.html', context={'form': form})