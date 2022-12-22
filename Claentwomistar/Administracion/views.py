from django.shortcuts import render,redirect
from .serializers import ProductosSerializer
from .models import Productos
from Principal.models import Usuario
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def products_list(request):
    if request.method == "GET":
        AllProductos = Productos.objects.all()
        serializer = ProductosSerializer(AllProductos, many=True)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = ProductosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def producto_detalle(request, pk):
    getproducto = Productos.objects.get(id=pk)
    getproducto.DoesNoe
    if request.method == 'GET':
        serializer = ProductosSerializer(getproducto)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = ProductosSerializer(getproducto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
        status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        getproducto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
@login_required()
def GestionUsuarios(request):
    Usuarios = Usuario.objects.all()
    if request.method == "POST":
        user = request.POST.get('Userid', False)
        activo = request.POST.get('activo', False)
        admin = request.POST.get('admin', False)
        tecnico = request.POST.get('tecnico', False)
        if admin:
            admin = True
        if activo:
            activo = True
        if tecnico:
            tecnico = True
        print(request.POST.get('Elimnar_user', False))
        userchange = Usuario.objects.get(id=user)
        userchange.admin = admin
        userchange.activo = activo
        userchange.tecnico = tecnico
        userchange.save()
        return redirect('/admin/')
    return render(request, "GestionUsuarios.html",{"Usuarios":Usuarios})
@login_required()
def EliminarUsuario(request,idUser):
    if request.user.admin:
        User = Usuario.objects.get(id=idUser)
        User.delete()
    return redirect('/admin/')
@login_required()
def HomeAdmin(request):
    Usuarios = Usuario.objects.all()
    if request.method == "POST":
        user = request.POST.get('Userid', False)
        activo = request.POST.get('activo', False)
        admin = request.POST.get('admin', False)
        tecnico = request.POST.get('tecnico', False)
        if admin:
            admin = True
        if activo:
            activo = True
        if tecnico:
            tecnico = True
        userchange = Usuario.objects.get(id=user)
        userchange.admin = admin
        userchange.activo = activo
        userchange.tecnico = tecnico
        userchange.save()
        return redirect('/admin/')
    return render(request, "Home.html",{"Usuarios":Usuarios})
