from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializer
from .models import Product
# # Create your views here.
# @api_view(['GET'])
# def apiOverview(request):
#     api_urls = {
#         'List':'/product-list/',
#         'Detail View':'/product-detail/<int:id>',
#         'Create':'/product-create/',
#         'Update':'/product-update/<int:id>',
#         'Delete':'/product-detail/<int:id>',
#     }

#     return Response(api_urls)

@api_view(['GET'])
def ShowAll(request):
    Products = Product.objects.all()
    serializer = ProductSerializer(Products,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def oneproduct(request,pk):
    data=Product.objects.get(id=pk)
    serializer = ProductSerializer(data,many=False)
    return Response(serializer.data)


@api_view(['POST'])
def CreateProduct(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def update(request,pk):
    product= Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=product,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def delete(request,id):
    product=Product.objects.get(id=id)
    product.delete()
    return Response('Item deleted successfully')

