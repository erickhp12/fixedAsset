from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .serializers import MarcaSerializer
from rest_framework.views import APIView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework import status
from .models import Marca
from .forms import RegistrarMarca
from django.http import HttpResponseRedirect


class MarcaListView(ListView):
    template_name = "listaMarcas.html"

    @method_decorator(login_required(login_url='login.view.url'))
    def get(self, request, *args, **kwargs):
        Query = Marca.objects.order_by('-fecha_inicio')
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


class MarcaFormView(CreateView):
    template_name = "formularioMarcas.html"

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
        Query = Marca.objects.filter(user=request.user).order_by('-fecha_inicio')
        total = Query.count()
        paginator = Paginator(Query, 50)
        page = request.GET.get('page')
        mensaje = "sin mensaje"

        try:
            entities = paginator.page(page)
        except PageNotAnInteger:
            entities = paginator.page(1)
        except EmptyPage:
            entities = paginator.page(paginator.num_pages)

        if total == 0:
            mensaje = "No tienes informacion registrada"

        user = request.user
        nombre = request.POST.get('nombre')
        observaciones = request.POST.get('observaciones')
        jssID = request.POST.get('jssID')
        
        print "checando si tengo datos"
        print user
        print nombre
        print observaciones

        try:
            if nombre == "":
                print  "1"
                return render(self.request, self.template_name)
            else:
                Marca.objects.create(
                    user=user,
                    nombre=nombre,
                    observaciones=observaciones              
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

        return HttpResponseRedirect('/Marca')


class UpdateMarcaFormView(ListView):
    template_name = "formulario.html"
    template_Marca = "lista.html"

    def get(self, request, pk, *args, **kwargs):
        loger_user = request.user
        entity = Marca.objects.get(user=request.user, id=pk)
        form = RegistrarMarca()

        mensaje = ""
        context = {
            'entity': entity,
            'mensaje': mensaje,
            'form': form
        }

        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        mensaje = ""
        entities = Marca.objects.filter(user=request.user).order_by('-fecha_inicio')
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
            marca = Marca.objects.get(user=request.user, id=pk)
            marca.pedimento = pedimento
            marca.numProyecto = numProyecto
            marca.localizacion = localizacion
            marca.ordenCompra = ordenCompra
            marca.marca = marca
            marca.modelo = modelo
            marca.serie = serie
            marca.origen = origen
            marca.precio = precio
            marca.tipoCambio = tipoCambio
            marca.fecha_ingreso = fecha_ingreso
            marca.fecha_pedimento = fecha_pedimento
            marca.descripcion = descripcion
            marca.jssID = jssID
            marca.save()
        except Exception as e:
            print "ALGO SALIO MAL EDITAR" + str(e)
            mensaje = "Error al editar gasto " + str(e)

        context = {
                    'entities': entities,
                    'total': total,
                    'mensaje': mensaje
                   }

        return HttpResponseRedirect('/Marca')


class DeleteMarcaView(ListView):
    def get(self, request, pk, **kwargs):
        Marca.objects.filter(id=pk, user=request.user).delete()
        return render(self.request, 'lista.html')


class SerializerMarca(APIView):
    def get(self, request, format=None):
        snippets = Marca.objects.all()
        serializer = MarcaSerializer(snippets, many=True)
        print "JSON RESPUESTA "
        print serializer.data
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MarcaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"Response": "Pedimento agregado correctamente"},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_302_FOUND)


class SerializerSingleMarca(APIView):
    def get(self, request, pk, format=None):
        snippets = Marca.objects.get(id=pk)
        serializer = MarcaSerializer(snippets, many=False)
        print "JSON RESPUESTA "
        print serializer.data
        return Response(serializer.data)
