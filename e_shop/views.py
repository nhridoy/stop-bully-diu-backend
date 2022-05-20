from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from e_shop import models as e_model, serializers as e_ser


# Create your views here.

class ProductsView(generics.ListCreateAPIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = e_ser.ProductSerializer
    queryset = e_model.ProductsModel.objects.all()


class SingleProductView(generics.RetrieveAPIView):
    serializer_class = e_ser.ProductSerializer
    queryset = e_model.ProductsModel.objects.all()
    lookup_field = 'pk'
