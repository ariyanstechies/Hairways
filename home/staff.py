from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from home.decorators import client_required
from home.forms import StaffSignUpForm
from django.db import transaction

from home.models import User, Client, Appointments, Reviews, Staff
from django.views import generic
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from django.views.generic.edit import UpdateView
from django.shortcuts import get_list_or_404, get_object_or_404
from django.urls import reverse_lazy


class StaffSignUpView(CreateView):
    model = User
    form_class = StaffSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Staff'
        return super().get_context_data(**kwargs)

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.password = 'hairways001'
        user.is_staff = True
        user.save()
        staff = Staff.objects.create(
            user=user, salon=self.request.user.owner.my_salons)
        staff.save()
        return user

    def form_valid(self, form):
        user = form.save()
        # login(self.request, user)
        return redirect('home')


# @method_decorator([login_required, client_required], name='dispatch')
# class ClientUpdate(UpdateView):
#     model = Client
#     fields = ['Full_Name', 'phone', 'email']
#     template_name = 'clients/client_update_form.html'
#     success_url = reverse_lazy('mini_dashboard')

#     def get_object(self):
#         return get_object_or_404(Client, pk=self.request.user.id)
#         messages.success(
#             self.request, 'The appointment was created succesfully.')
