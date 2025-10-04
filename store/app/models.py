from django.db import models
from django.contrib.auth import get_user_model


class Category(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField()

class PurchaseItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField()

class Customer(models.Model):
    name = models.CharField(max_length=100)
    is_member = models.BooleanField(default=False)
    phone = models.CharField(max_length=10)

class Purchase(models.Model):
    items = models.ManyToManyField(PurchaseItem)
    total_cost = models.IntegerField()
    discount = models.IntegerField()
    seller = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    is_cancel = models.BooleanField(default=False)

