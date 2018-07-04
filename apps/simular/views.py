from django.shortcuts import render,redirect
from apps.simular.models import *


def index(request):
	return render(request,'simular/inicioSimular.html')
