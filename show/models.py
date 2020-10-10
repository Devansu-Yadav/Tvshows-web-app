from django.db import models

# Create your models here.
class Show(models.Model):
    """Model representing a tv show"""
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    genre = models.CharField(max_length=50)
    next_ep = models.DateField()

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class User(models.Model):
    """Model representing a User"""
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    user_data_list = [] 

    def __str__(self):
        """String for representing the Model object."""
        return self.name