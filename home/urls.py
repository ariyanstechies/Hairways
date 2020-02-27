from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from home import views, owners
from home.owners import AppointmentUpdate, Appointment2CreateView
from home.clients import ClientUpdate, AppointmentCreateView
from home.clients import AppointmentListView, MiniDashboard
from home.clients import CommentsListView, MyAppointments, MyComments


urlpatterns = [
    path('', views.comingsoon, name='comingsoon'),
    path('current/registerd/salons',views.crs, name = 'crs'),
    path('home', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('faqs/', views.faqs, name='faqs'),
    path('salon/<slug:name>/',views.salon_details, name = 'salon_details'),
    path('add_salon', views.signup_steps, name='add_salon'),
    path('client/update/', ClientUpdate.as_view(), name='client_update'),
    path('owner/update/', owners.OwnerUpdate.as_view(), name='owner_update'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('salon/add/', owners.SalonCreateView.as_view(), name='salon_add'),
    path('preference/', views.preference, name='preference'),
    path('visits/', views.visits, name="visits"),
    path('Salon/payment/', views.clientPayment, name='clientPayment'),
    path('dashboard/profile/', views.profile, name='profile'),
    path('dashboard/reviews/', views.reviews, name='reviews'),
    path('dashboard/services/', views.services, name='services'),
    path('dashboard/services-add/', views.services_add, name='services_add'),
    path('dashboard/staffs/', views.staffs, name='staffs'),
    path('dashboard/staffs/new/', views.staff_new, name='staffs_new'),
    path('dashboard/staffs/<int:pk>', views.staffs_edit, name='staffs_edit'),
    path('dashboard/appointments-add/', views.dashboard_appointments_add, name='dashboard_appointments_add'),
    path('dashboard/products/', views.products, name='products'),
    path('dashboard/products-add/', views.products_add, name='products_add'),
    path('dashboard/customers/', views.customers, name='customers'),
    path('upload/', views.upload, name='upload'),
    path('appointment/add/', AppointmentCreateView.as_view(),
         name='appointment_add'),
    path('special/appointment/add/',
         Appointment2CreateView.as_view(), name='appointment2_add'),
    path('client/dashboard', AppointmentListView.as_view(),
         name='client_dashboard'),
    path('dashboard/appointments', views.AppointmentListView.as_view(), name='dashboard_appointments'),
    path('client/dashboard2', CommentsListView.as_view(),
         name='client_dashboard2'),
    path('update/<int:pk>/', AppointmentUpdate.as_view(), name='a_update'),

    #     client dashboard A.K.A Mini dashboard
    path('user/profile/', MiniDashboard.as_view(), name='mini_dashboard'),
    path('my/appointments', MyAppointments.as_view(), name='my_appointments'),
    path('my/comments', MyComments.as_view(), name='my_comments'),
    #     end of client dashboard


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
