from django.forms import ModelForm
from django import forms
from billing.models import Product,Purchase

class ProductCreateForm(ModelForm):
    class Meta:
        model=Product
        fields=["product_name"]


class PurchaseCreateForm(ModelForm):
    class Meta:
        model = Purchase
        fields = ["product","qty","purchase_price","selling_price"]

