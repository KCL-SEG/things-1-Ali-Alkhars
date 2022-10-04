from django.db import models
from django.db.models import Model
from django.core.validators import MaxValueValidator, MinValueValidator

class Thing(Model):
    name = models.CharField(
        max_length = 30,
        unique = True,
        blank = False
    )
    description = models.CharField(
        max_length = 120
    )
    quantity = models.IntegerField(
        validators = [
            MinValueValidator(limit_value=0, message='You have entered a value below the minimum'),
            MaxValueValidator(limit_value=100, message='You have entered a value above the maximum')
        ]
    )
