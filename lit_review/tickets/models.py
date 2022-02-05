from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Ticket(models.Model):
    title = models.fields.CharField(max_length=100 , null=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)
    content = models.fields.CharField(max_length=100 , null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title