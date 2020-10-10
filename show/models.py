from django.db import models

# Create your models here.
class Show(models.Model):
    """Model representing a tv show"""
    name = models.CharField(max_length=200)

    def __str__(self):
        """String for representing the Model object."""
        return self.name