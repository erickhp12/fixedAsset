from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from fixedAsset import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include("login.urls")),
    url(r'^', include("main.urls")),
    url(r'^', include("marca.urls")),
    url(r'^', include("usuarios.urls")),
] + static( settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
