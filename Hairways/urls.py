from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path, include
from .views import owners, clients, home_views


urlpatterns = [
    path('', home_views.home, name='home'),
    path('about/', home_views.about, name='about'),
    path('pricing/', home_views.pricing, name='pricing'),
    # path('dashboard/', home_views.dashboard, name='dashboard'),
    path('Salon/<int:id>/', home_views.moreinfo, name='moreinfo'),
    path('user/<int:id>/', home_views.user, name='user'),
    path('productsServices/', home_views.productsServices, name='productsServices'),
    path('staffClients/', home_views.staffClients, name='staffClients'),
    path('map/', home_views.map, name='map'),
    path('calendar/', home_views.calendar, name='calendar'),
    path('upgrade/', home_views.upgrade, name='upgrade'),
    path('upload/', home_views.upload, name='upload'),
    path('faqs/', home_views.faqs, name='faqs'),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('signup/', views.signup, name="signup"),
    path('blog/', home_views.blog, name="blog"),
    path('locations/', home_views.locations, name="locations"),
    path('dashboard/', home_views.AppointmentListView.as_view(), name='dashboard'),

    # url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    # path('auth/', include('social_django.urls', namespace='social')),      # GOOGLE & FACEBOOK OAUTH


    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
