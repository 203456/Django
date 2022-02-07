from django.urls import path, re_path
from django.conf.urls import include
#View import
from loadImageComponente.views import ImageTableDetail, imageView

urlpatterns = [
    re_path(r'^table/$', imageView.as_view()),
    re_path(r'^table/(?P<pk>\d+)$', ImageTableDetail.as_view())
]
