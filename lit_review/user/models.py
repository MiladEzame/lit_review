from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.fields.CharField(max_length=100, null=True)
    last_name = models.fields.CharField(max_length=100, null=True)
    email = models.fields.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.first_name}'