from django.test import TestCase
from django.urls import reverse
from testapp.models import Burger
from datetime import  datetime , timedelta

# Create your tests here.
class BurgerModelTest(TestCase):
    def setUp(self):
        Burger.objects.create(name='Test burger',price = 8, weight = 180,meat = "FISH", bacon = True, date = datetime.now() - timedelta (5),pk = 1)
    def test_fresh(self):
        burger = Burger.objects.get(name='Test burger')
        self.assertTrue(not burger.is_fresh())