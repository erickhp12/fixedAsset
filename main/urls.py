from django.conf.urls import url
from main.views import *

urlpatterns = [
    url(r'^Main/$', SerializerMain.as_view()),
    url(r'^Main/(?P<pk>\d+)/$', SerializerSingleMain.as_view())
]
