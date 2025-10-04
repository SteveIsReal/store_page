from django.contrib import admin
from .models import *


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    pass


@admin.register(Category)
class AdminProduct(admin.ModelAdmin):
    pass

@admin.register(Purchase)
class AdminProduct(admin.ModelAdmin):
    pass

@admin.register(PurchaseItem)
class AdminProduct(admin.ModelAdmin):
    pass

@admin.register(Customer)
class AdminProduct(admin.ModelAdmin):
    pass

