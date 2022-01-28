from django.shortcuts import render
from user.models import User
from .filters import UserFilter

# Create your views here.
def users(request):
    users = User.objects.all()
    myFilter = UserFilter()

    return render(request, 'user/users.html',
                  context={'users' : users, 'myFilter': myFilter})

def show(request, pk):
    user = User.objects.get(id=pk)

    context = {'user': user}
    return render(request, 'user/show.html', context)