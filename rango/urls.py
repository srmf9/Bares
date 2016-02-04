from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^new_tapa/$', views.add_tapa, name='add_tapa'),
    	url(r'^about/$', views.about, name='about'),
    	url(r'^reclama_datos/', views.reclama_datos, name='reclama_datos'),
    	url(r'^(?P<bares_name_slug>[\w\-]+)/$', views.bares, name='bares'),
    	)