from django.shortcuts import render

from rest_framework import status, generics
from rest_framework.response import Response
from .models import *

from .serializer import *

class ListProduct(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        product_name = self.request.query_params.get('name', "")
        product_type = self.request.query_params.get('type', "")
        return Product.objects.filter(name__istartswith=product_name, category__name__istartswith=product_type)

class ListOfCategories(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class FindCustomer(generics.ListAPIView):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        cusomter_phone = self.request.query_params.get('phone', "")
        return Customer.objects.filter(phone__istartswith=cusomter_phone)

class AddPurchaseItem(generics.ListCreateAPIView):
    serializer_class = PurchaseItemSerializer
    queryset = PurchaseItem.objects.all()

class CreatePurchase(generics.ListCreateAPIView):
    serializer_class = PurchaseSerializer
    queryset = Purchase.objects.all()

class CancelBill(generics.UpdateAPIView):
    serializer_class = PurchaseSerializer
    lookup_field = "id"

    def get_queryset(self):
        get_data = self.kwargs['id']
        return Purchase.objects.filter(id=get_data)
