from django.db import models
from django.contrib.auth.models import AbstractUser

class Thing(AbstractUser):
    name = models.TextField()
    description = models.TextField()
    quantity = models.TextField()
