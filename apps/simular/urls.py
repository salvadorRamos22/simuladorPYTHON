from django.conf.urls import url,include
from apps.simular.views import *

urlpatterns = [
url(r'^inicio',index,name='index'),
url(r'^nuevaSimulacion',nuevaSimulacion,name='nuevaSimulacion'),
]