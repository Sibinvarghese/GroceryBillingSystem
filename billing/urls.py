
from django.contrib import admin
from django.urls import path
from .views import CreateProduct,ViewProduct,HomePage,\
    EditProduct,DeleteProduct,CreatePurchase,\
    ViewPurchase,EditPurchase,DeletePurchase,\
    OrderCreate,OrderLinesView,BillGenerate,\
    ViewBill,ViewBillItems,SearchOrder,HomePageFinal,UserLogin,UserLogout,SearchByDate
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
    path("billgenerate/<int:billno>",BillGenerate.as_view(),name="billgenerate"),
    path("viewbill",ViewBill.as_view(),name="viewbill"),
    path("viewbillitems/<int:billno>",ViewBillItems.as_view(),name="billitems"),
    path("search",SearchOrder.as_view(),name="search"),
    path("homepage",HomePageFinal.as_view(),name="page"),
    path("",UserLogin.as_view(),name="login"),
    path("sreachdate",SearchByDate.as_view(),name="datesearch"),
    path("logout",UserLogout.as_view(),name="logout")
]
