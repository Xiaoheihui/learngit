from django.conf.urls import url, include
import backend.views

urlpatterns = [
    url(r'register$', backend.views.register),
    url(r'login$', backend.views.login),
    url(r'test$', backend.views.test),
    url(r'getMessage$', backend.views.getMessage),
    url(r'alterMessage$', backend.views.alterMessage),
    url(r'getCompInfoByClassId$', backend.views.getCompInfoByClassId),
]