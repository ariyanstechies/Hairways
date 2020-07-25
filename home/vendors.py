from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic import CreateView
from home.forms import AppointmentUpdateForm
from home.models import User, Vendor, Appointment, Salon
from home.decorators import vendor_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import get_list_or_404, get_object_or_404
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from django.template.defaultfilters import slugify


@method_decorator([login_required, vendor_required], name='dispatch')
class VendorUpdate(UpdateView):
    model = Vendor
    fields = ['email', 'name', 'phone', 'location', 'gender']
    template_name = 'owners/owner_update_form.html'

    def get_object(self):

        return get_object_or_404(Vendor, pk=self.request.user.id)
        # TODO: add redirect url or succes_url



# special appointment adds
@method_decorator([login_required, vendor_required], name='dispatch')
class Appointment2CreateView(CreateView):
    model = Appointment
    fields = ('salons', 'date_time', 'totalCost')
    template_name = 'customer/order_add_form.html'

    def form_valid(self, form):
        self.appointment = form.save(commit=False)
        self.appointment.Vendor = self.request.user.owner
        self.appointment.save()
        messages.success(
            self.request, 'The appointment was created succesfully.')
        return redirect('a_update', pk=self.appointment.pk)


@method_decorator([login_required, vendor_required], name='dispatch')
class AppointmentUpdate(UpdateView):
    model = Appointment
    form_class = AppointmentUpdateForm
    template_name = 'appointments_update_form.html'
