from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth.decorators import user_passes_test

def es_admin(user):
    return user.is_superuser


def Inicio(request):
    return render(request, "pages/home.html")


def verproductos(request):
    query=Productos.objects.all()
    data={
        'listaProductos':query
    }
    return render(request,'pages/verproductos.html',data)


def AgregarProd(request):
    data={
        'Formularios':FormularioProductos()
    }  
    # METODO Q LLEGA 
    if request.method=='POST':
# QUERY  accion en base de datos borrar, agregar , actualizar , seleccioar 
        query=FormularioProductos(data=request.POST,files=request.FILES)
        if  query.is_valid():
            query.save()           
            data['mensaje']='datos registrados'
        else: 
            data['Formularios']=FormularioProductos()
    
    return render(request,'pages/AgregarProductos.html', data)


@user_passes_test(es_admin)
def editar(request, id):
    producto = Productos.objects.get(Codigo=id)
    
    data = {
        'Formularios': FormularioProductos(instance=producto)
    }

    if request.method == 'POST':
        formulario = FormularioProductos(request.POST, request.FILES, instance=producto)
        if formulario.is_valid():
            formulario.save()
            return redirect('ver')

    return render(request, 'pages/AgregarProductos.html', data)

@user_passes_test(es_admin)
def eliminar(request, id):
    producto = Productos.objects.get(Codigo=id)
    producto.delete()
    return redirect('ver')


def verproductos(request):
    buscar = request.GET.get("buscar")

    if buscar:
        productos = Productos.objects.filter(Nombre__icontains=buscar)
    else:
        productos = Productos.objects.all()

    return render(request, 'pages/verproductos.html', {
        'listaProductos': productos
    })