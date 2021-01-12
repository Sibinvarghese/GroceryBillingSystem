from rest_framework.serializers import ModelSerializer
from billing.models import Product,Purchase



class ProductSerializer(ModelSerializer):
    class Meta:
        model=Product
        fields=["product_name"]


class PurchaseSerializer(ModelSerializer):
    class Meta:
        model=Purchase
        fields=["product","qty","purchase_price","selling_price","purchase_date"]
