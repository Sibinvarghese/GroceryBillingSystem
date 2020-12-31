
from django.contrib import admin
from django.urls import path
from .views import CreateProduct,ViewProduct,HomePage,\
    EditProduct,DeleteProduct,CreatePurchase,\
    ViewPurchase,EditPurchase,DeletePurchase,\
    OrderCreate,OrderLinesView,View_Bill,\
    View_ToatlBill,View_BillDetails
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
    path("order",OrderCreate.as_view(),name="billing"),
    path("orderlines<int:billno>",OrderLinesView.as_view(),name="orderlines"),
    path("view",View_Bill.as_view(),name="viewbills"),
    path("viewbill",View_ToatlBill.as_view(),name="viewtotalbill"),
    path("viewbillitems/<int:billnumber>",View_BillDetails.as_view(),name="viewbilldetails")
]
