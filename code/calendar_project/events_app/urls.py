from django.conf.urls import url
from events_app import views

urlpatterns = [
    url(r'^hello/$', views.hola_mundo, name='hola_mundo'),
]
