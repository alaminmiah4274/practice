from django.shortcuts import render
from rest_framework.decorators import api_view
from product.models import Product
from django.shortcuts import get_object_or_404
from product.serializers import ProductModelSerializer
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
@api_view(["GET", "POST"])
def view_products(request):
    if request.method == "GET":
        products = Product.objects.all()
        serializer = ProductModelSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == "POST":
        serializer = ProductModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
def view_specific_product(request, pk):
    if request.method == "GET":
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductModelSerializer(product)
        return Response(serializer.data)


def view_categories(request):
    pass


def view_specific_categories(request):
    pass
