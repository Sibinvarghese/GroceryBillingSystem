
from django.contrib import admin
from django.urls import path,include
from api.views import Product,ProductDetail,Purchase,PurchaseDetails

urlpatterns = [
   path("product",Product.as_view()),
   path("product/<int:pk>",ProductDetail.as_view()),
   path("purchase",Purchase.as_view()),
   path("purchase/<int:pk>",PurchaseDetails.as_view()),
   ]
