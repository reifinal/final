from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.lista_estudiantes),
    url(r'^estudiante/(?P<pk>[0-9]+)/$', views.detalle_estudiante),
    ]