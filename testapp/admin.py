from django.contrib import admin
from  .models import BurgerModel
from  .models import ListCars

# Register your models here.
admin.site.register(BurgerModel)
admin.site.register(ListCars)
