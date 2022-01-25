from django.db import models

# Create your models here.
class Ticket(models.Model):
    title = models.fields.CharField(max_length=100)
    content = models.fields.CharField(max_length=100)