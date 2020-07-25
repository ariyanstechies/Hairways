from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import (LoginView, LogoutView,
                                       PasswordChangeView,
                                       PasswordResetCompleteView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView,
                                       PasswordResetView)
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView

from home.forms import (ProfileUpdateForm, UserPasswordChangeForm,
                        UserSignUpForm, UserSetPasswordForm,
                        UserUpdateForm)
from home.models import Profile, User


class Login(LoginView):
    template_name = "accounts/login.html"

    def get_success_url(self):
        if self.request.user.is_vendor:
            return reverse_lazy('vendor_dashboard')
        return reverse_lazy('customer_dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class Logout(LogoutView):
    next_page = reverse_lazy('home')


class UserSignUpView(CreateView):
    model = User
    form_class = UserSignUpForm
    template_name = "accounts/register.html"

    def form_valid(self, form):
        user = form.save()

        messages.success(self.request, f'Your account has been created!')

        login(self.request, user)

        return redirect('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Set appropriate user_type
        context['user_type'] = 'Customer'
        return context


@method_decorator(login_required, name='dispatch')
class PasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    template_name = 'accounts/password_change_form.html'

    def get_success_url(self):
        messages.success(self.request, 'Password Changed Successfully.')
        if self.request.user.is_vendor:
            return reverse_lazy('vendor_dashboard')
        return reverse_lazy('customer_dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PasswordReset(PasswordResetView):
    template_name = 'accounts/password_reset_form.html'
    email_template_name = 'accounts/password_reset_email.html'
    subject_template_name = 'accounts/password_reset_subject.txt'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PasswordResetDone(PasswordResetDoneView):
    template_name = "accounts/password_reset_done.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PasswordResetConfirm(PasswordResetConfirmView):
    form_class = UserSetPasswordForm
    template_name = "accounts/password_reset_confirm.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PasswordResetComplete(PasswordResetCompleteView):
    template_name = "accounts/password_reset_complete.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


@login_required
def profile_edit(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,
                                         request.FILES,
                                         instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            messages.success(request,
                             f'Your account details have been updated!')
            if request.user.is_vendor:
                return redirect('vendor_dashboard')
            return redirect('customer_dashboard')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': user_form,
        'p_form': profile_form
    }
    return render(request, 'accounts/profile.html', context)
