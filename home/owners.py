from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic import CreateView
from home.forms import OwnerSignUpForm, AppointmentUpdateForm
from home.models import User, Owner, Appointments, Salon
from home.decorators import owner_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import get_list_or_404, get_object_or_404
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from django.template.defaultfilters import slugify


class OwnerSignUpView(CreateView):
    model = User
    form_class = OwnerSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'owner'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('add_salon')


@method_decorator([login_required, owner_required], name='dispatch')
class OwnerUpdate(UpdateView):
    model = Owner
    fields = ['email', 'ownerName', 'phone', 'location', 'gender']
    template_name = 'owners/owner_update_form.html'

    def get_object(self):

        return get_object_or_404(Owner, pk=self.request.user.id)
        # TODO: add redirect url or succes_url


@method_decorator([login_required, owner_required], name='dispatch')
class SalonCreateView(CreateView):
    model = Salon
    fields = ('name', 'description', 'paybill', 'location')
    template_name = 'owners/salon_add_form.html'

    def form_valid(self, form):
        salon = form.save(commit=False)
        salon.Owner = self.request.user.owner
        salon.url = slugify(salon.name)
        salon.save()
        messages.success(self.request, 'The Salon was created succesfully.')
        return redirect('dashboard_appointments')

        # special appointment adds


@method_decorator([login_required, owner_required], name='dispatch')
class Appointment2CreateView(CreateView):
    model = Appointments
    fields = ('salons', 'date_time', 'totalCost')
    template_name = 'clients/order_add_form.html'

    def form_valid(self, form):
        self.appointment = form.save(commit=False)
        self.appointment.Owner = self.request.user.owner
        self.appointment.save()
        messages.success(
            self.request, 'The appointment was created succesfully.')
        return redirect('a_update', pk=self.appointment.pk)


@method_decorator([login_required, owner_required], name='dispatch')
class AppointmentUpdate(UpdateView):
    model = Appointments
    form_class = AppointmentUpdateForm
    template_name = 'appointments_update_form.html'
