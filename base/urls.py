from django.contrib import admin
from django.urls import include, path
from home import accounts as account, views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home.urls")),

    # Accounts
    path('accounts/login/', account.Login.as_view(), name='login'),
    path('accounts/logout/', account.Logout.as_view(), name='logout'),
    path('accounts/register/', account.UserSignUpView.as_view(),
         name='register'),
    path('accounts/password_change/',
         account.PasswordChange.as_view(), name='password_change'),
    path('accounts/password_reset/',
         account.PasswordReset.as_view(), name='password_reset'),
    path('accounts/password_reset/done/',
         account.PasswordResetDone.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/',
         account.PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', account.PasswordResetComplete.as_view(),
         name='password_reset_complete'),
    path('accounts/profile/', account.profile_edit, name='profile_edit'),
]
