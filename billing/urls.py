
from django.contrib import admin
from django.urls import path
from .views import CreateProduct,ViewProduct,HomePage,EditProduct,DeleteProduct,CreatePurchase,ViewPurchase,EditPurchase,DeletePurchase
urlpatterns = [
    path("addproduct",CreateProduct.as_view(),name="create"),
    path("listproduct",ViewProduct.as_view(),name="list"),
    path("home",HomePage.as_view(),name="home"),
    path("editproduct/<int:pk>",EditProduct.as_view(),name="edit"),
    path("deleteproduct/<int:pk>",DeleteProduct.as_view(),name="delete"),
    path("addpurchase",CreatePurchase.as_view(),name="add"),
    path("listpurchases",ViewPurchase.as_view(),name="listpurchase"),
    path("editpurchase/<int:pk>",EditPurchase.as_view(),name="editpurchase"),
    path("deletepurchase/<int:pk>",DeletePurchase.as_view(),name="deletepurchase"),

]
