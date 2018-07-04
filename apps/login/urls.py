from django.conf.urls import url,include
from apps.login.views import *

urlpatterns = [
url(r'^$',login, name='log'),
url(r'^registrar$',registrar,name='registro'),
url(r'^logout$',logout,name='logout'),
]