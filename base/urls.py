from django.contrib import admin
from django.urls import include, path
from home.views import owners, clients, home_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home.urls")),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', home_views.SignUpView.as_view(), name='signup'),
    path('accounts/signup/client/', clients.ClientSignUpView.as_view(), name='client_signup'),
    path('accounts/signup/Owner/', owners.OwnerSignUpView.as_view(), name='owner_signup'),
]
