from django.conf.urls import url
from main.views import *

urlpatterns = [
    url(r'^Main/$', MainListView.as_view()),
    url(r'^Main/Form/$', MainFormView.as_view()),
    url(r'^Main/API/$', SerializerMain.as_view()),
    url(r'^Main/API/(?P<pk>\d+)/$', SerializerSingleMain.as_view())
]
