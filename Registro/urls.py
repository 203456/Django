from django.urls import path, re_path
from django.conf.urls import include
#View import
from Registro.views import RegistroView

urlpatterns = [
    re_path(r'^crear_user/$', RegistroView.as_view())
]
