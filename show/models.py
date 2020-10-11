from django.db import models
from django.contrib.auth.models import User
from django.core.validators import int_list_validator

# Create your models here.
class Show(models.Model):
    """Model representing a tv show"""
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200, null=True)
    genre = models.CharField(max_length=50, null=True)
    next_ep = models.DateField(null=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ep_list = models.CharField(validators=[int_list_validator], max_length=100)   

    def __str__(self):
        return self.user.username