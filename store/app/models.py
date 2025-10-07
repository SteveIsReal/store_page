from django.db import models
from django.contrib.auth import get_user_model


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self):
        return f"{self.name}: {self.price}฿"

class PurchaseItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.product.name}, {self.price}"

class Customer(models.Model):
    name = models.CharField(max_length=100)
    is_member = models.BooleanField(default=False)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} (member:{self.is_member})"

class Purchase(models.Model):
    items = models.ManyToManyField(PurchaseItem)
    total_cost = models.IntegerField()
    discount = models.IntegerField()
    seller = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateTimeField(null=True)
    is_cancel = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.seller}, {self.customer} ({self.date})"

