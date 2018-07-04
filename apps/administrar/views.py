from django.shortcuts import render,redirect
from apps.administrar.models import *
from django.views.decorators.csrf import csrf_exempt, csrf_protect


def index(request):
	return render(request,'simular/inicioAdmin.html')

@csrf_protect
def tipoU(request):
	if request.method == 'POST':
		tUsuario = tipoUsuario()
		tUsuario.descripcion = request.POST['descripcion']
		tUsuario.estado = 1
		tUsuario.save()
		return redirect('admi:tipoUsuario')
	tipo = tipoUsuario.objects.order_by('id')
	contexto =  {'tipo':tipo}
	return render(request,'administrar/tipoUsuario.html',contexto)

def eliminar(request,idTipo):
	tipo = tipoUsuario.objects.get(id=idTipo)
	tipo.estado = 0
	tipo.save()
	return redirect('admi:tipoUsuario')

def habilitar(request,idTipo):
	tipo = tipoUsuario.objects.get(id=idTipo)
	tipo.estado = 1
	tipo.save()
	return redirect('admi:tipoUsuario')

def faseLista(request):
	fase = faseCultivo.objects.all().order_by('id')
	return render(request,'administrar/faseCultivo.html',{'fase':fase})

def faseListaSiembra(request,idSiembra):
	fase = faseCultivo.objects.filter(siembra=idSiembra)
	return render(request,'administrar/faseCultivo.html',{'fase':fase})


def siembras(request):
	if request.method == 'POST':
		sm = siembra()
		sm.nombre = request.POST['nombre']
		sm.descripcion = request.POST['descripcion']
		sm.estado = 1
		sm.save()
		return redirect('admi:siembra')
	sm2 =  siembra.objects.all().order_by('id')
	return render(request,'administrar/siembra.html',{'siembra':sm2})

def listaUsuarios(request):
	usua = usuario.objects.filter(estado=1).order_by('id')

	return render(request,'administrar/listaUsuario.html',{'usuario':usua})

def bloquearUsuario(request,idusuario):
	usua = usuario.objects.get(id=idusuario)
	usua.estado = 0
	usua.save()
	return redirect('admi:listaUsuarios')

def usuariosBloqueados(request):
	usua = usuario.objects.filter(estado=0).order_by('-id')

	return render(request,'administrar/listaUsuario.html',{'usuario':usua})

def habilitarUsuario(request,idusuario):
	usua = usuario.objects.get(id=idusuario)
	usua.estado = 1
	usua.save()
	return redirect('admi:usuariosBloqueados')

def verUsuario(request,idusuario):
	usua = usuario.objects.get(id=idusuario)
	return render(request,'administrar/verUsuario.html',{'usuario':usua})
# Create your views here.
