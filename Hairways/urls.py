from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path

urlpatterns = [
    url(r'^$|^home/$', views.home, name='home'),
    url(r'^faqs/$', views.faqs, name='faqs'),
    url(r'^about/$', views.about, name='about'),
    # url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    # url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^pricing/$', views.pricing, name='pricing'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    # url(r'^moreinfo/$', views.moreinfo, name='moreinfo'),
    path('Salon/<int:id>/', views.moreinfo, name='moreinfo'),
    path('Salon/<int:id>/', views.services, name='moreinfo'),
    url(r'^user/$', views.user, name='user'),
    url(r'^productsServices/$', views.productsServices, name='productsServices'),
    url(r'^staffClients/$', views.staffClients, name='staffClients'),
    url(r'^map/$', views.map, name='map'),
    url(r'^calendar/$', views.calendar, name='calendar'),
    url(r'^upgrade/$', views.upgrade, name='upgrade'),
    url(r'^upload/$', views.upload, name='upload'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
