from django.shortcuts import render
from rest_framework.views import  APIView
from rest_framework.views import Response
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from api.serializers import  ProductSerializer,PurchaseSerializer
from billing.models import Product as pd
from billing.models import Purchase as ps
# Create your views here.

#api/product  => create And List
class Product(APIView):

    def get(self,request):
        products=pd.objects.all()
        serializer=ProductSerializer(products,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer= ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#api/product/1  => list , edit and delete
class ProductDetail(APIView):
    model = pd
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self,pk):
        try:
            return pd.objects.get(id=pk)
        except:
            raise Http404

    def get(self,request,pk,format=None):
        products=self.get_object(pk)
        serializer=ProductSerializer(products)
        return Response(serializer.data)

    def put(self,request,pk,format=None):
        products=self.get_object(pk)
        serializer=ProductSerializer(products,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        products=self.get_object(pk)
        products.delete()
        return Response(status=status.HTTP_200_OK)

#api/purchase => create and list
class Purchase(APIView):

    def get(self,request):
        purchases=ps.objects.all()
        serializer=PurchaseSerializer(purchases,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=PurchaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#api/purchase/1 => list, edit and delete
class PurchaseDetails(APIView):
    model = ps
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self,pk):
        try:
            return ps.objects.get(id=pk)
        except:
            raise Http404
    def get(self,request,pk):
        purchases=self.get_object(pk)
        serializer=PurchaseSerializer(purchases)
        return Response(serializer.data)
    def put(self,request,pk):
        purchases=self.get_object(pk)
        serializer=PurchaseSerializer(purchases,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        purchases=self.get_object(pk)
        purchases.delete()
        return Response(status=status.HTTP_200_OK)

