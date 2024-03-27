
from django.db import models
from datetime import datetime
from datetime import timedelta
from django.urls import reverse
class BurgerModel(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveSmallIntegerField(default=8)
    weight = models.PositiveSmallIntegerField(default=180)
    material = models.TextChoices("Meat" , "BEEF FISH CHIKEN VEGE")
    bacon = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now=True)
    sell = True
    pk = models.IntegerField(name='sosat')

    def __str__(self):
        return self.name
    def is_fresh(self):
        return(datetime.now().date()-self.date)<= timedelta(minutes=5)
    def get_absolute_url(self):
        return reverse("burger-details", kwargs = {'pk':self.pk})
    def have_bacon(self):
        self.bacon = True
    def is_sell(self):
        self.sell = True
        self.save()
