from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$|^index/$', views.index, name='index'),
    url(r'^faqs/$', views.faqs, name='faqs'),
    url(r'^about/$', views.about, name='about'),
    url(r'^login/$', views.login, name='login'),
    url(r'^pricing/$', views.pricing, name='pricing'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^moreinfo/$', views.moreinfo, name='moreinfo'),
    ]
