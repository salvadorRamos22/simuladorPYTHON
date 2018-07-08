from django.shortcuts import render,redirect
from apps.administrar.models import *


def index(request):
	return render(request,'simular/inicioSimular.html')


def nuevaSimulacion(request):

	smb = siembra.objects.filter(estado=1)
	return render(request,'simular/nuevaSimulacion.html',{'siembras':smb})
