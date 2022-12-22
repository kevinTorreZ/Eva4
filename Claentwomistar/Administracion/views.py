from django.shortcuts import render
from .serializers import ProductosSerializer
from .models import Productos
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def products_list(request):
    if request.method == "GET":
        AllProductos = Productos.objects.all()
        serializer = ProductosSerializer(AllProductos,many=True)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = ProductosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
status=status.HTTP_400_BAD_REQUEST)

