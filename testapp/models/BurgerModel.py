from django.db import models
from datetime import datetime
from datetime import timedelta
from django.urls import reverse


class BurgerModel(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=8)

    def __str__(self):
        return self.name

    def is_more8(self):
        return self.price > 8

    def is_less8(self):
        return self.price < 8
