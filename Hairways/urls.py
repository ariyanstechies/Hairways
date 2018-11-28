from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$|^home/$', views.home, name='home'),
    url(r'^faqs/$', views.faqs, name='faqs'),
    url(r'^about/$', views.about, name='about'),


    url(r'^signup/$', views.signup, name='signup'),
    url(r'^pricing/$', views.pricing, name='pricing'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^user/$', views.user, name='user'),
    url(r'^productsServices/$', views.productsServices, name='productsServices'),
    url(r'^staffClients/$', views.staffClients, name='staffClients'),
    url(r'^map/$', views.map, name='map'),
    url(r'^calendar/$', views.calendar, name='calendar'),
    url(r'^upgrade/$', views.upgrade, name='upgrade'),
    url(r'^moreinfo/$', views.moreinfo, name='moreinfo'),

    

    ]
