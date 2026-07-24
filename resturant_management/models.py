from django.db import models

# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # CASCADE DELETE ALL DATA IF CAT IS DELETED
    # PROTECTED DOES NOT LET CATEGORY TO BE DELETED IF DATA EXISTS
    # SET_NULL SET THE CATEGORY AS NULL
    price = models.FloatField()
    image = models.ImageField(
        null=True, blank=True
    )  # null means the data can be empty, black means via API if no data exists it is fine

    def __str__(self):
        return self.name


class Table(models.Model):

    num = models.CharField(max_length=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Order(models.Model):

    STATUS_CHOICE = [
        ("P", "PENDING"),
        ("C", "COMPLETE"),
        ("D", "DELIVERED"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, blank=True, default=1)
    total_price = models.FloatField(null=True, blank=True, default=1)
    status = models.CharField(max_length=1, choices=STATUS_CHOICE, default="P")
    is_paid = models.BooleanField(default=False)


class OrderMenu(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    menu = models.ForeignKey(Menu, on_delete=models.PROTECT)
