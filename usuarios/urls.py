from django.conf.urls import url
from usuarios.views import *

urlpatterns = [
    url(r'^Usuarios/$', UsuariosListView.as_view()),
    # url(r'^usuarios/Form/$', UsuariosFormView.as_view()),
    # url(r'^usuarios/Form/editar/(?P<pk>\d+)/$',
    #     UpdateusuariosFormView.as_view(), name='formulario'),
    # url(r'^usuarios/API/$', Serializerusuarios.as_view()),
    # url(r'^usuarios/API/(?P<pk>\d+)/$', SerializerSingleusuarios.as_view()),
    # url(r'^deleteusuarios/(?P<pk>\d+)/$', DeleteusuariosView.as_view()),
]
