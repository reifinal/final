from django.conf.urls import include, url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.lista_estudiantes, name='lista_estudiante'),
    url(r'^estudiante/(?P<pk>[0-9]+)/$', views.detalle_estudiante, name='detalle_estudiante'),
    url(r'^estudiante/nuevo/$', views.nuevo_estudiante, name='nuevo_estudiante'),
    url(r'^estudiante/(?P<pk>[0-9]+)/editar/$', views.editar_estudiante, name='editar_estudiante'),
    url(r'^curso/$', views.lista_cursos, name='lista_cursos'),
    url(r'^curso/(?P<pk>[0-9]+)/$', views.detalle_curso, name='detalle_curso'),
    url(r'^curso/nuevo/$', views.nuevo_curso, name='nuevo_curso'),
    url(r'^curso/(?P<pk>[0-9]+)/editar/$', views.editar_curso, name='editar_curso'),
    url(r'^curso/(?P<pk>[0-9]+)/borrar/$', views.borrar_curso, name='borrar_curso'),
    url(r'^matricula/nuevo/$', views.nuevo_matricula, name='nuevo_matricula'),
    url(r'^login/$', views.authentication, name='authentication'),
    url(r'^logout/$', auth_views.logout, {'next_page':'/'}, name="logout"),
    ]