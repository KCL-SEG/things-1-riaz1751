from django.core.validators import RegexValidator
from django.db import models

class Thing(models.Model):
    name = models.TextField(
        max_length=30,
        unique=True,
        validators=[RegexValidator(
            regex=r'^\w{1,}$',
            message='Name cannot be be empty and must be 30 characters or less'
        )])
    description = models.TextField()
    quantity = models.IntegerField(default=0)
