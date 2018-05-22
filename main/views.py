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
from .forms import RegistrarMain
from django.http import HttpResponseRedirect


class MainListView(ListView):
    template_name = "lista.html"

    @method_decorator(login_required(login_url='login.view.url'))
    def get(self, request, *args, **kwargs):
        Query = Main.objects.filter(user=request.user).order_by('-fecha_inicio')
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


class MainFormView(CreateView):
    template_name = "formulario.html"

    @method_decorator(login_required(login_url='login.view.url'))
    def get(self, request, *args, **kwargs):
        user_logged = request.user
        mensaje = ""

        context = {
            'mensaje': mensaje
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        mensaje = ""
        Query = Main.objects.filter(user=request.user).order_by('-fecha_inicio')
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
        marca = request.POST.get('marca')
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
                print  "1"
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
                print "2"
        except Exception as e:
            mensaje = "Error al crear registro " + str(e)
            print "3"
            print str(e)
        context = {
            'entities': entities,
            'total': total,
            'mensaje': mensaje
        }

        return HttpResponseRedirect('/Main')


class UpdateMainFormView(ListView):
    template_name = "formulario.html"
    template_main = "lista.html"

    def get(self, request, pk, *args, **kwargs):
        loger_user = request.user
        entity = Main.objects.get(user=request.user, id=pk)
        form = RegistrarMain()

        mensaje = ""
        context = {
            'entity': entity,
            'mensaje': mensaje,
            'form': form
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
        marca = request.POST.get('marca')
        modelo = request.POST.get('modelo')
        serie = request.POST.get('serie')
        origen = request.POST.get('origen')
        precio = request.POST.get('precio')
        tipoCambio = request.POST.get('tipoCambio')
        fecha_ingreso = request.POST.get('fecha_ingreso')
        fecha_pedimento = request.POST.get('fecha_pedimento')
        descripcion = request.POST.get('descripcion')
        jssID = request.POST.get('jssID')

        print "checando si tengo datos EDITAR"
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
            main = Main.objects.get(user=request.user, id=pk)
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
            main.save()
        except Exception as e:
            print "ALGO SALIO MAL EDITAR" + str(e)
            mensaje = "Error al editar gasto " + str(e)

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
        print "JSON RESPUESTA "
        print serializer.data
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
        print "JSON RESPUESTA "
        print serializer.data
        return Response(serializer.data)
