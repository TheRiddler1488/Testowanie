from django.test import TestCase
from django.urls import reverse
from testapp.models import BurgerModel
from datetime import datetime, timedelta


# Create your tests here.
class BurgerTest(TestCase):
    def setUp(self):
        BurgerModel.objects.create(name='Test burger', price=9)
        BurgerModel.objects.create(name='Another burger', price=7)

    def test_is_more8(self):
        burger = BurgerModel.objects.get(name='Test burger')
        self.assertTrue(burger.is_more8())

    def test_is_less8(self):
        burger = BurgerModel.objects.get(name='Another burger')
        self.assertFalse(burger.is_less8())
