from primerComponente.views import primerTablaList
from django.urls import path, re_path
from django.conf.urls import include
urlpatterns = [
    re_path(r'^primer_componente/$', primerTablaList.as_view())


]