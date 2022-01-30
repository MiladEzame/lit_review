from django.shortcuts import render
from .models import User

# Create your views here.
def user_followers(request):
    user = User.objects.get(id=4)
    followed_by = user.userfollow_set.all()

    return render(request, 'user/profile.html', context={'user' : user, 'followed_by' : followed_by})