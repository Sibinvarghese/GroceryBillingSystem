from django.forms import ModelForm
from django import forms
from billing.models import Product,Purchase,Order,OrderLines

class ProductCreateForm(ModelForm):
    class Meta:
        model=Product
        fields=["product_name"]


class PurchaseCreateForm(ModelForm):
    class Meta:
        model = Purchase
        fields = ["product","qty","purchase_price","selling_price"]


class OrderCreateForm(ModelForm):
    class Meta:
        model = Order
        fields = ["billnumber","customer_name","phone_number"]

class OrderlinesCreateForm(forms.Form):
        # fields = ["bill_number","product_name","product_qty"]

        bill_number=forms.CharField()
        queryset = Purchase.objects.all().values_list('product__product_name',flat=True)
        choices = [(name, name) for name in queryset]

        product_name=forms.ChoiceField(choices=choices,required=False,widget=forms.Select())
        product_qty=forms.IntegerField()

        class Meta:
            model=OrderLines
            fields = ["bill_number", "product_name", "product_qty"]

