from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .serializers import UserSerializer
from rest_framework.views import APIView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework import status
from marca.models import Marca
from .forms import RegisterUser
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


class UsuariosListView(ListView):
    template_name = "listaUsuarios.html"

    @method_decorator(login_required(login_url='login.view.url'))
    def get(self, request, *args, **kwargs):
        entities = User.objects.all().order_by('-date_joined')
        total = entities.count()
        mensaje = ""

        if total == 0:
            mensaje = "No tienes informacion registrada"

        context = {
            'entities': entities,
            'total': total,
            'mensaje': mensaje
        }

        return render(request, self.template_name, context)
