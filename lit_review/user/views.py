from django.shortcuts import render
from user.models import User

# Create your views here.
def users(request):
    users = User.objects.all()
    return render(request, 'user/users.html',
                  context={'users' : users})

def show(request, pk):
    user = User.objects.get(id=pk)

    context = {'user': user}
    return render(request, 'user/show.html', context)