from django.conf.urls import url

from login.views import IndexView, LoginView, LogoutView, AccountView, MisionView, VisionView, HistoryView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index.view.url'),
    url(r'^mision/$', MisionView.as_view(), name='mision'),
    url(r'^vision/$', VisionView.as_view(), name='vision'),
    url(r'^historia/$', HistoryView.as_view(), name='historia'),
    url(r'^login/$', LoginView.as_view(), name='login.view.url'),
    url(r'^logout/$', LogoutView.as_view(), name='logout.view.url'),
    url(r'^cuenta/$', AccountView.as_view(), name='account.view.url'),
]
