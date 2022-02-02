from django.shortcuts import render
from .models import User, UserFollow

# Create your views here.
def user_followers(request):
    user = User.objects.get(id=4)
    followed_by = UserFollow.objects.filter(followed_user = user).all()
    following = UserFollow.objects.filter(user = user).all()

    return render(
        request, 'user/profile.html', 
        context={'user': user, 'followed_by': followed_by, 'following': following}
    )