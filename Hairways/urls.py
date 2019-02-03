from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pricing/', views.pricing, name='pricing'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('Salon/<int:id>/', views.moreinfo, name='moreinfo'),
    path('user/', views.user, name='user'),
    path('productsServices/', views.productsServices, name='productsServices'),
    path('staffClients/', views.staffClients, name='staffClients'),
    path('map/', views.map, name='map'),
    path('calendar/', views.calendar, name='calendar'),
    path('upgrade/', views.upgrade, name='upgrade'),
    path('upload/', views.upload, name='upload'),
    path('faqs/', views.faqs, name='faqs'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name="signup"),
    path('blog/', views.blog, name="blog"),
    path('locations/', views.locations, name="locations"),
    # url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),

    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
