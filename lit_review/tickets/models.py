from django.db import models

# Create your models here.
class Ticket(models.Model):
    title = models.fields.CharField(max_length=100 , null=True)
    content = models.fields.CharField(max_length=100 , null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)