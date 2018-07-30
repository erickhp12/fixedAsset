from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .serializers import MainSerializer
from rest_framework.views import APIView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework import status
from .models import Main
from marca.models import Marca
from .forms import RegistrarMain
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


class MainListView(ListView):
    template_name = "lista.html"

    @method_decorator(login_required(login_url='login.view.url'))
    def get(self, request, *args, **kwargs):
        Query = Main.objects.all().order_by('-fecha_inicio')
        total = Query.count()

        paginator = Paginator(Query, 50)
        page = request.GET.get('page')
        mensaje = ""

        try:
            entities = paginator.page(page)
        except PageNotAnInteger:
            entities = paginator.page(1)
        except EmptyPage:
            entities = paginator.page(paginator.num_pages)

        if total == 0:
            mensaje = "No tienes informacion registrada"

        context = {
            'entities': entities,
            'total': total,
            'mensaje': mensaje
        }

        return render(request, self.template_name, context)


    def post(self, request, *args, **kwargs):
        search = request.POST.get('search')
        mensaje = ""
        entities = Main.objects.all().filter(pedimento__icontains=search
                ) | Main.objects.all().filter(numProyecto__icontains=search
                ) | Main.objects.all().filter(localizacion__icontains=search).order_by('-fecha_inicio')
        total = entities.count()

        if total == 0:
            mensaje = "No tienes registros..."

        context = {
                    'entities':entities,
                    'total':total,
                    'mensaje':mensaje     
                    }
        
        return render(self.request, self.template_name, context)


class MainFormView(CreateView):
    template_name = "formulario.html"

    @method_decorator(login_required(login_url='login.view.url'))
    def get(self, request, *args, **kwargs):
        user_logged = request.user
        form = RegistrarMain()
        puedeEditar = False
        if request.user.groups.filter(name="aduanas").exists():
            puedeEditar = True

        marcas = Marca.objects.order_by('-nombre')
        mensaje = ""

        context = {
            'mensaje': mensaje,
            'form':form,
            'puedeEditar': puedeEditar,
            'marcas':marcas
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        mensaje = ""
        Query = Main.objects.all().order_by('-fecha_inicio')
        total = Query.count()
        paginator = Paginator(Query, 50)
        page = request.GET.get('page')
        mensaje = ""
        try:
            entities = paginator.page(page)
        except PageNotAnInteger:
            entities = paginator.page(1)
        except EmptyPage:
            entities = paginator.page(paginator.num_pages)

        if total == 0:
            mensaje = "No tienes informacion registrada"

        user = request.user
        pedimento = request.POST.get('pedimento')
        numProyecto = request.POST.get('numProyecto')
        localizacion = request.POST.get('localizacion')
        ordenCompra = request.POST.get('ordenCompra')
        marcaSeleccionada = request.POST.get('marca')
        marca = Marca.objects.filter(nombre=marcaSeleccionada).first()
        modelo = request.POST.get('modelo')
        serie = request.POST.get('serie')
        origen = request.POST.get('origen')
        precio = request.POST.get('precio')
        tipoCambio = request.POST.get('tipoCambio')
        fecha_ingreso = request.POST.get('fecha_ingreso')
        fecha_pedimento = request.POST.get('fecha_pedimento')
        descripcion = request.POST.get('descripcion')
        jssID = request.POST.get('jssID')
        
        print "checando si tengo datos"
        print marcaSeleccionada
        print user
        print pedimento
        print numProyecto
        print localizacion
        print ordenCompra
        print marca
        print modelo
        print serie
        print origen
        print precio
        print tipoCambio
        print fecha_ingreso
        print fecha_pedimento
        print descripcion
        print jssID

        try:
            if pedimento == "":
                return render(self.request, self.template_name)
            else:
                Main.objects.create(
                    user=user,
                    pedimento=pedimento,
                    numProyecto=numProyecto,
                    localizacion=localizacion,
                    ordenCompra=ordenCompra,
                    marca=marca,
                    modelo=modelo,
                    serie=serie,
                    origen=origen,
                    precio=precio,
                    tipoCambio=tipoCambio,
                    fecha_ingreso=fecha_ingreso,
                    fecha_pedimento=fecha_pedimento,
                    descripcion=descripcion,
                    jssID=jssID                    
                )
        except Exception as e:
            mensaje = "Error al crear registro " + str(e)
            print str(e)
        context = {
            'entities': entities,
            'total': total,
            'mensaje': mensaje
        }

        return HttpResponseRedirect('/Main')


class UpdateMainFormView(ListView):
    template_name = "formulario.html"

    def get(self, request, pk, *args, **kwargs):
        user_logged = request.user
        entity = Main.objects.get(id=pk)
        marcas = Marca.objects.order_by('-nombre')
        form = RegistrarMain()
        puedeEditar = False
        if request.user.groups.filter(name="aduanas").exists():
            puedeEditar = True

        mensaje = ""
        context = {
            'entity':entity,
            'puedeEditar':puedeEditar,
            'mensaje':mensaje,
            'marcas':marcas,
            'form':form,
        }

        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        mensaje = ""
        entities = Main.objects.filter(user=request.user).order_by('-fecha_inicio')
        total = entities.count()
        user = request.user
        pedimento = request.POST.get('pedimento')
        numProyecto = request.POST.get('numProyecto')
        localizacion = request.POST.get('localizacion')
        ordenCompra = request.POST.get('ordenCompra')
        marcaSeleccionada = request.POST.get('marca')
        marca = Marca.objects.filter(nombre=marcaSeleccionada).first()
        modelo = request.POST.get('modelo')
        serie = request.POST.get('serie')
        origen = request.POST.get('origen')
        precio = request.POST.get('precio')
        tipoCambio = request.POST.get('tipoCambio')
        fecha_ingreso = request.POST.get('fecha_ingreso')
        fecha_pedimento = request.POST.get('fecha_pedimento')
        descripcion = request.POST.get('descripcion')
        jssID = request.POST.get('jssID')
        imagen = request.POST.get('imagen')

        print "checando si tengo datos EDITAR"
        print "User " + str(user)
        print "Pedimento " + str(pedimento)
        print "Num Proyecto " + str(numProyecto)
        print "Localizacion " + str(localizacion)
        print "Orden compra " + str(ordenCompra)
        print "Marca " + str(marca)
        print "Modelo " + str(modelo)
        print "Serie " + str(serie)
        print "Origen " + str(origen)
        print "Precio " + str(precio)
        print "Tipo Cambio  " + str(tipoCambio)
        print "fecha ingreso " + str(fecha_ingreso)
        print "fecha pedimento " + str(fecha_pedimento)
        print "descripcion " + str(descripcion)
        print "ID " + str(jssID)
        print "Imagen " + str(imagen)

        try:
            main = Main.objects.get(id=pk)
            main.pedimento = pedimento
            main.numProyecto = numProyecto
            main.localizacion = localizacion
            main.ordenCompra = ordenCompra
            main.marca = marca
            main.modelo = modelo
            main.serie = serie
            main.origen = origen
            main.precio = precio
            main.tipoCambio = tipoCambio
            main.fecha_ingreso = fecha_ingreso
            main.fecha_pedimento = fecha_pedimento
            main.descripcion = descripcion
            main.jssID = jssID
            main.imagen = imagen
            main.save()
        except Exception as e:
            print "ALGO SALIO MAL EDITAR " + str(e)
            mensaje = "Error al editar fomulario " + str(e)

        context = {
                    'entities': entities,
                    'total': total,
                    'mensaje': mensaje
                   }

        return HttpResponseRedirect('/Main')


class DeleteMainView(ListView):
    def get(self, request, pk, **kwargs):
        Main.objects.filter(id=pk, user=request.user).delete()
        return render(self.request, 'lista.html')


class SerializerMain(APIView):
    def get(self, request, format=None):
        snippets = Main.objects.all()
        serializer = MainSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MainSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"Response": "Pedimento agregado correctamente"},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_302_FOUND)


class SerializerSingleMain(APIView):
    def get(self, request, pk, format=None):
        snippets = Main.objects.get(id=pk)
        serializer = MainSerializer(snippets, many=False)
        return Response(serializer.data)
