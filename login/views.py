# coding=utf-8
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from login.forms import LoginForm
from marca.models import Marca
from main.models import Main
from django.contrib.auth.models import User
class LoginView(TemplateView):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        mensaje = "0"
        if request.user.is_authenticated():
            return HttpResponseRedirect('/')
        else:
            if request.session.get("login"):
                return HttpResponseRedirect('/')

            ctx = { 'mensaje':mensaje }

            return render(request, self.template_name, ctx)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect('/')
        else:
            mensaje = "0"
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password"]
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return HttpResponseRedirect('/')
                    else:
                        mensaje = "Usuario inactivo, contacta al administrador"
                else:
                    mensaje = "Usuario y/o contraseña incorrectos"

            ctx = {
                    'mensaje': mensaje
                    }
            return render(request, self.template_name, ctx)


class IndexView(TemplateView):
    template_name = 'index.html'

    @method_decorator(login_required(login_url='login.view.url'))
    def get(self, request, *args, **kwargs):
        marcas = Marca.objects.all().count()
        pedimentos = Main.objects.count()
        usuarios = User.objects.count()
        cdJuarez = Main.objects.filter(origen='Ciudad Juarez').count()
        valleHermoso = Main.objects.filter(origen='Valle Hermoso').count()
        terminados = Main.objects.filter(terminado=True).count()
        pendientes = Main.objects.filter(terminado=False).count()
        print "ciudad juarez"
        print cdJuarez

        context = {
            'marcas':marcas,
            'pedimentos':pedimentos,
            'usuarios':usuarios,
            'cdJuarez':cdJuarez,
            'terminados': terminados,
            'pendientes':pendientes,
            'valleHermoso':valleHermoso,
        }

        return render(request, self.template_name, context)


class MisionView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, "mision.html")


class VisionView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, "vision.html")


class HistoryView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, "historia.html")


class AccountView(TemplateView):
    template_name = 'cuenta.html'

    @method_decorator(login_required(login_url='login.view.url'))
    def get(self, request, *args, **kwargs):
        entities = Main.objects.filter(user=request.user).order_by('-fecha_inicio')[:10]
        
        mensaje = ""
        
        context = {
                    'entities': entities,
                    'mensaje': mensaje,  
                    }
        return render(request,self.template_name, context)


class LogoutView(TemplateView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect('/')

