from django.conf.urls import url, include
import backend.views

urlpatterns = [
    url(r'register$', backend.views.register),
    url(r'login$', backend.views.login),
    url(r'test$', backend.views.test),
    url(r'getMessage$', backend.views.getMessage),
    url(r'alterMessage$', backend.views.alterMessage),
    url(r'getCompInfoByClassId$', backend.views.getCompInfoByClassId),
    url(r'getCompInfoByCompId$', backend.views.getCompInfoByCompId),
    url(r'getCompInfoBySelect$', backend.views.getCompInfoBySelect),
    url(r'sendBBS$', backend.views.sendBBS),
    url(r'getBBSByClassId$', backend.views.getBBSByClassId),
    url(r'getBBSByUserId$', backend.views.getBBSByUserId),
    url(r'deleteBBS$', backend.views.deleteBBS),
    url(r'getMarkMessage$', backend.views.getMarkMessage),
    url(r'DeleteMarkMessage$', backend.views.DeleteMarkMessage),
    url(r'markComp$', backend.views.markComp),
    url(r'upLoadImage$', backend.views.upLoadImage),
    url(r'getNewestComp$', backend.views.getNewestComp),
    url(r'getHotestComp$', backend.views.getHotestComp),
    url(r'uploadCompInfo$', backend.views.upLoadCompInfo),
]