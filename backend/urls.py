from django.conf.urls import url, include
import backend.views

urlpatterns = [url(r'test$', backend.views.test, )]