from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="main"),
    url(r'^add/$', views.add, name="add"),
    url(r'(?P<number>\d+)/destroy/$', views.destroy, name="destroy"),
    url(r'(?P<number>\d+)/delete/$', views.delete, name="delete"),


]