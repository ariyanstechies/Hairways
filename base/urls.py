from django.contrib import admin
from django.urls import include, path
from home import owners, clients, views, staff

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home.urls")),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.SignUpView.as_view(), name='signup'),
    path('accounts/signup/client/',
         clients.ClientSignUpView.as_view(), name='client_signup'),
    path('accounts/signup/Owner/',
         owners.OwnerSignUpView.as_view(), name='owner_signup'),

    path('accounts/signup/staff/',
         staff.StaffSignUpView.as_view(), name='staff_signup'),
]
