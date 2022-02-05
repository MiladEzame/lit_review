from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserFollow(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='following')
    followed_user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='followed_by')
    time_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user.username} follows {self.followed_user.username}"
    
    class Meta:
        # ensures we don't get multiple UserFollows instances
        # for unique user-user_followed pairs
        unique_together = ('user', 'followed_user', )
        