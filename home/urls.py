from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from home import views, vendors
from home.vendors import AppointmentUpdate, Appointment2CreateView
from home.customers import AppointmentCreateView, AppointmentListView, MiniDashboard
from home.salons import SalonCreateView, salon_details

urlpatterns = [
    # Pages
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('faqs/', views.faqs, name='faqs'),

    # Salons
    path('salon/new/', SalonCreateView.as_view(), name='new_salon'),
    path('salon/<slug:name>/', salon_details, name='show_salon'),
    path('salon/payment/', views.clientPayment, name='clientPayment'),
    path('add_salon', views.signup_steps, name='add_salon'),


    # API
    path('api/v1/confirmation', views.confirmation, name='confirmation'),
    path('mpesa', views.mpesa, name='mpesa'),
    path('api/v1/validation', views.validation, name='validation'),


    path('transaction/inprogress', views.transaction_progress,
         name='transaction_progress'),
    path('owner/update/', vendors.VendorUpdate.as_view(), name='owner_update'),

    # Vendor Dashboard
    path('dashboard/', views.dashboard, name='vendor_dashboard'),
    path('dashboard/profile/', views.profile, name='profile'),
    path('dashboard/reviews/', views.reviews, name='reviews'),
    path('dashboard/customers/', views.customers, name='customers'),
    path('dashboard/services', views.services, name='services'),
    path('dashboard/services/new', views.service_new, name='service_new'),
    path('dashboard/service/<int:id>/edit',
         views.service_edit,
         name='service_edit'),
    path('dashboard/service/<int:id>/remove/',
         views.service_delete,
         name='service_delete'),
    # Products
    path('dashboard/products', views.products, name='products'),
    path('dashboard/products/new', views.product_new, name='product_new'),
    path('dashboard/products/<int:id>/edit',
         views.product_edit, name='product_edit'),
    path('dashboard/product/<int:id>/remove/',
         views.product_delete, name='product_delete'),

    # Appointments
    path('dashboard/appointments',
         views.appointments, name='dashboard_appointments'),
    path('appointment/update/<int:pk>/',
         AppointmentUpdate.as_view(), name='a_update'),
    path('dashboard/appointments/new/',
         views.dashboard_appointments_new, name='dashboard_appointments_new'),
    path('appointments/complete/<int:pk>/',
         views.appointment_complete,  name='appointment_complete'),

    # salon images starts here
    path('dashboard/salon/images<slug:slug>',
         views.salon_images,
         name='salon_images'),
    path('dashboard/salon/select/images<slug:slug>/<int:id>',
         views.select_image,
         name='select_images'),
    path('user/profile', views.user_profile, name='user_profile'),

    path('upload/', views.upload, name='upload'),
    path('about/client/<int:pk>/',
         views.client_profile_for_salons,
         name='client_profile_for_salons'),

    # Customer dashboard A.K.A Mini dashboard
    path('customer/dashboard',
         AppointmentListView.as_view(),
         name='customer_dashboard'),
    path('user/profile/', MiniDashboard.as_view(), name='mini_dashboard'),
    path('preference/', views.preference, name='preference'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
