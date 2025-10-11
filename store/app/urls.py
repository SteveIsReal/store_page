from django.urls import path
from app import views

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('product/', views.ListProduct.as_view()),
    path('category/', views.ListOfCategories.as_view()),
    path('customer/', views.FindCustomer.as_view()),
    path('add_purchase_item/', views.AddPurchaseItem.as_view()),
    path('create_purchase/', views.CreatePurchase.as_view()),
    path('cancel_bill/<int:id>', views.CancelBill.as_view()),

    #Authentication
    path('user/token/refresh/', TokenRefreshView.as_view()),
    path('user/token/', TokenObtainPairView.as_view()),

]
