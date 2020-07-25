from django.contrib import admin
from django.urls import include, path
from home import accounts, views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home.urls")),

    # Accounts
    path('accounts/login/', accounts.Login.as_view(), name='login'),
    path('accounts/logout/', accounts.Logout.as_view(), name='logout'),
    path('accounts/register/', accounts.UserSignUpView.as_view(),
         name='register'),
    path('accounts/password_change/',
         accounts.PasswordChange.as_view(), name='password_change'),
    path('accounts/password_reset/',
         accounts.PasswordReset.as_view(), name='password_reset'),
    path('accounts/password_reset/done/',
         accounts.PasswordResetDone.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/',
         accounts.PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', accounts.PasswordResetComplete.as_view(),
         name='password_reset_complete'),
    path('accounts/profile/', accounts.profile_edit, name='profile_edit'),
]
