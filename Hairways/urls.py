from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path, include
from .views import owners, clients, home_views


urlpatterns = [
    path('', home_views.home, name='home'),
    path('about/', home_views.about, name='about'),
    path('client/update/', clients.ClientUpdate.as_view(), name = 'client_update'),
    path('pricing/', home_views.pricing, name='pricing'),
    # path('dashboard/', home_views.dashboard, name='dashboard'),
    path('Salon/<int:id>/', home_views.moreinfo, name='moreinfo'),
    path('user/<int:id>/', home_views.user, name='user'),
    #path('appointment/list/', clients.Appointment, name='dashboard2'),
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
    path('appointment/add/', clients.AppointmentCreateView.as_view(), name='appointment_add'),
    path('client/dashboard', clients.AppointmentListView.as_view(), name='client_dashboard'),
    path('dashboard/', home_views.AppointmentListView.as_view(), name='dashboard'),
    path('client/dashboard2', clients.CommentsListView.as_view(), name='client_dashboard2'),

    # url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    # path('auth/', include('social_django.urls', namespace='social')),      # GOOGLE & FACEBOOK OAUTH
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
