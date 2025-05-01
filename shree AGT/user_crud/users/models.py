from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    # Add custom fields here if needed, for example:
    phone = models.CharField(max_length=15, blank=True)
    gender = models.CharField(max_length=10, choices=[
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    ], blank=True)
    hobbies = models.CharField(max_length=255, blank=True)
    dob = models.DateField(null=True, blank=True, default="YYYY-MM-DD")

    def __str__(self):
        return self.username