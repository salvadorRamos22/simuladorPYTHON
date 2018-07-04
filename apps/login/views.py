from django.shortcuts import render,redirect
from django.http import *
from django.contrib.auth import *
from django.contrib.auth.models import *
from django.template import loader
from django.views.defaults import page_not_found
from apps.administrar.models import *
from django.contrib.auth.hashers import make_password,check_password

def login(request):
	if request.user.is_active:
		return redirect('admi:inicio')
	error=' '
	if request.method == 'POST':
		email2 = request.POST.get('email',None)
		con = request.POST.get('password',None)
		#con2 = make_password(con,hasher='pbkdf2_sha256')
		us = usuario.objects.filter(email=email2).exists()
		if us == True:
			us = usuario.objects.get(email=email2)
			nombre = us.nombre
			con2 = us.password
			tiusu = us.tipoU 
			con3 = check_password(con,con2,setter=None,preferred='default')
			if con3 == True:
				usn=""
				usn+=nombre
				usn+=email2
				user=auth.authenticate(username=usn,email=email2,password=con)
				if user:
					auth.login(request,user)
					if tiusu == 1:
						return redirect('admi:inicio')
					else:
						return redirect('simular:index')
				else:
					error="Error de autentificacion"
					return render(request,'administrar/login.html',{'error':error})
			else:
				error="Password incorrecto"
				return render(request,'administrar/login.html',{'error':error})
		else:
			error = "Email no valido o mal digitado"
			return render(request,'administrar/login.html',{'error':error})
	else:
		error=" "
		template = loader.get_template('administrar/login.html')
		contexto = {'error':error}
		return render(request,'administrar/login.html',contexto)
		#return HttpResponse(template.render(context,request))

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect("/")


def registrar(request):
	error = ''
	year=('1930','1931','1932','1933','1934','1935','1936','1937','1938','1939',
	'1940','1941','1942','1943','1944','1945','1946','1947','1948','1949',
	'1950','1951','1952','1953','1954','1955','1956',
	'1957','1958','1959','1961','1962','1963','1964','1965',
	'1966','1967','1968','1969','1970','1971','1972','1973','1974','1975',
	'1976','1977','1978','1979',
	'1980','1981','1982','1969','1983','1984','1985','1986','1987','1988','1989',
	'1990','1991','1992','1993','1994','1995','1996','1997','1998','1999',
	'2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010',
	)
	mes = ('Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre')
	dia = ('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31')
	sexos = (('Masculino','Masculino'),('Femenino','Femenino'))
	tipou = tipoUsuario.objects.filter(estado=1).order_by('id')
	if request.method == 'POST':
		email2 = request.POST.get('email',None)

		if User.objects.filter(email=email2).exists() == False:
			usua = usuario()
			nom = request.POST['nombre']
			usua.nombre = nom
			usua.apellido = request.POST['apellido']
			passw = request.POST['password']
			usua.password = make_password(passw,hasher='pbkdf2_sha256')
			anio = request.POST['anio']
			mes2 = request.POST['mes']
			mesNum = mesNumerico(mes2)
			dia2 = request.POST['dia']
			fecha=anio
			fecha+= "-"
			fecha+=mesNum
			fecha+="-"
			fecha+=dia2
			usua.fechaNacimiento = fecha
			sexo2 = request.POST['sexo']
			if sexo2 == "0":
				usua.sexo = "Masculino"
			else:
				usua.sexo = "Femenino"
			email2 = request.POST['email']
			usua.email = email2
			idTipoU = request.POST['tipou']
			usua.tipoU = tipoUsuario.objects.get(id=idTipoU)
			usua.estado = 1
			usua.save()
			nom2=''
			nom2+=nom
			nom2+=email2
			user = User.objects.create_user(username=nom2,email=email2,password=passw)
			user=authenticate(email=email2,password=passw)
			login(request)
			return redirect('admi:inicio')	
		else:
			error="El correo ya existe"
			return render(request,'administrar/registrar.html',{'error':error,'tipo':tipou,'year':year,'mes':mes,'dia':dia,'sexo':sexos})
	else:
		error=' '
		return render(request,'administrar/registrar.html',{'error':error,'tipo':tipou,'year':year,'mes':mes,'dia':dia,'sexo':sexos})


def mesNumerico(dato):
	mm = ''
	if dato == 'Enero':
		mm = '1'
	if dato == 'Febrero':
		mm = '2'
	if dato == 'Marzo':
		mm = '3'
	if dato == 'Abril':
		mm = '4'
	if dato =='Mayo':
		mm = '5'
	if dato == 'Junio':
		mm = '6'
	if dato == 'Julio':
		mm = '7'
	if dato == 'Agosto':
		mm = '8'
	if dato == 'Septiembre':
		mm = '9'
	if dato == 'Octubre':
		mm = '10'
	if dato == 'Noviembre':
		mm = '11'
	if dato == 'Diciembre':
		mm = '12'
	return mm 
		#return redirec('login:registro')