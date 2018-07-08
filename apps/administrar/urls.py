from django.conf.urls import url,include
from apps.administrar.views import *

urlpatterns = [
url(r'^inicio$',index,name='inicio'),
url(r'^tipoU$',tipoU,name='tipoUsuario'),
url(r'^eliminarTipo/(?P<idTipo>\d+)/$',eliminar,name='eliminarTipo'),
url(r'^habilitarTipo/(?P<idTipo>\d+)/$',habilitar,name='habilitarTipo'),

url(r'^faseCultivo$',faseLista,name='faseCultivo'),
url(r'^faseCultivoSiembra/(?P<idSiembra>\d+)/$',faseListaSiembra,name='faseCultivoSiembra'),
url(r'^siembra$',siembras,name='siembra'),

url(r'^listaUsuarios$',listaUsuarios,name='listaUsuarios'),
url(r'^bloquearUsuario/(?P<idusuario>\d+)/$',bloquearUsuario,name='bloquearUsuario'),

url(r'^listaUsuarioBloqueados$',usuariosBloqueados,name='usuariosBloqueados'),
url(r'^habilitarUsuario/(?P<idusuario>\d+)/$',habilitarUsuario,name='habilitarUsuario'),
url(r'^verUsuario/(?P<idusuario>\d+)/$',verUsuario,name='verusuario'),

url(r'^nuevaFase$',nuevaFase,name="nuevaFase"),

]