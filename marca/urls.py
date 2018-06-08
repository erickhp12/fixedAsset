from django.conf.urls import url
from marca.views import *

urlpatterns = [
    url(r'^Marca/$', MarcaListView.as_view()),
    url(r'^Marca/Form/$', MarcaFormView.as_view()),
    url(r'^Marca/Form/editar/(?P<pk>\d+)/$',UpdateMarcaFormView.as_view(), name='formulario'),
    url(r'^Marca/API/$', SerializerMarca.as_view()),
    url(r'^Marca/API/(?P<pk>\d+)/$', SerializerSingleMarca.as_view()),
    url(r'^deleteMarca/(?P<pk>\d+)/$', DeleteMarcaView.as_view()),
]
