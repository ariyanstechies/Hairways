from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from home.decorators import customer_required
from home.models import User, Customer, Appointment, Review
from django.views import generic
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from django.views.generic.edit import UpdateView
from django.shortcuts import get_list_or_404, get_object_or_404
from django.urls import reverse_lazy


@ method_decorator([login_required, customer_required], name='dispatch')
class CustomerUpdateView(UpdateView):
    model = Customer
    fields = ['full_name', 'phone_number', 'email']
    template_name = 'customer/client_update_form.html'
    success_url = reverse_lazy('mini_dashboard')

    def get_object(self):
        return get_object_or_404(Customer, pk=self.request.user.id)
        messages.success(
            self.request, 'The appointment was created succesfully.')


@method_decorator([login_required, customer_required], name='dispatch')
class AppointmentListView(ListView):
    model = Appointment
    context_object_name = 'my_appointments'
    template_name = 'customer/dashboard.html'

    def get_queryset(self):
        queryset = self.request.user.my_appointments \
            .select_related('client')
        return queryset


@method_decorator([login_required, customer_required], name='dispatch')
class AppointmentCreateView(CreateView):
    model = Appointment
    fields = ('services', 'salons',
              'date_time', 'totalCost')
    template_name = 'customer/order_add_form.html'

    def form_valid(self, form):
        appointment = form.save(commit=False)
        appointment.client = self.request.user
        appointment.save()
        messages.success(
            self.request, 'The appointment was created succesfully.')
        return redirect('client_dashboard')


@method_decorator([login_required, customer_required], name='dispatch')
class ReviewListView(ListView):
    model = Review
    context_object_name = 'my_reviews'
    template_name = 'customer/dashboard2.html'

    def get_queryset(self):
        queryset = self.request.user.my_reviews \
            .select_related('author')
        return queryset


@method_decorator([login_required, customer_required], name='dispatch')
class MiniDashboard(ListView):
    model = Appointment
    context_object_name = 'my_appointments'
    template_name = 'customer/mini_dashboard.html'


@method_decorator([login_required, customer_required], name='dispatch')
class MyAppointment(ListView):
    model = Appointment
    context_object_name = 'my_appointments'
    template_name = 'customer/client_appointment.html'

    def get_queryset(self):
        queryset = self.request.user.my_appointments \
            .select_related('client')
        return queryset


@method_decorator([login_required, customer_required], name='dispatch')
class MyReview(ListView):
    model = Review
    context_object_name = 'my_reviews'
    template_name = 'customer/client_reviews.html'

    def get_queryset(self):
        queryset = self.request.user.my_reviews \
            .select_related('author')
        return queryset
