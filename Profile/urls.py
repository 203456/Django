from django.urls import path, re_path
from django.conf.urls import include


from Profile.views import UserDetail, UserProfile,  UserView

urlpatterns = [
    re_path(r'^users/$', UserView.as_view()),
    re_path(r'^user/(?P<pk>\d+)$', UserDetail.as_view()),
    re_path(r'^data/(?P<pk>\d+)/$',UserProfile.as_view()),
]