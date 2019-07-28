from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from home.decorators import client_required
from home.forms import ClientSignUpForm
from home.models import User, Client, Appointments, Comments
from django.views import generic
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from django.views.generic.edit import UpdateView
from django.shortcuts import get_list_or_404, get_object_or_404


class ClientSignUpView(CreateView):
    model = User
    form_class = ClientSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Client'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


@method_decorator([login_required, client_required], name='dispatch')
class ClientUpdate(UpdateView):
    model = Client
    fields = ['nickname', 'email']
    template_name = 'clients/client_update_form.html'

    def get_object(self):
        return get_object_or_404(Ticket, pk=self.pk)
        # TODO: add redirect url or succes_url


@method_decorator([login_required, client_required], name='dispatch')
class AppointmentListView(ListView):
    model = Appointments
    context_object_name = 'my_appointments'
    template_name = 'clients/dashboard.html'

    def get_queryset(self):
        queryset = self.request.user.my_appointments \
            .select_related('client')
        return queryset


@method_decorator([login_required, client_required], name='dispatch')
class AppointmentCreateView(CreateView):
    model = Appointments
    fields = ('services', 'salons', 'AppointmentsStatus',
              'date_time', 'totalCost')
    template_name = 'clients/order_add_form.html'

    def form_valid(self, form):
        appointment = form.save(commit=False)
        appointment.client = self.request.user
        appointment.save()
        messages.success(
            self.request, 'The appointment was created succesfully.')
        return redirect('client_dashboard')


@method_decorator([login_required, client_required], name='dispatch')
class CommentsListView(ListView):
    model = Comments
    context_object_name = 'my_comments'
    template_name = 'clients/dashboard2.html'

    def get_queryset(self):
        queryset = self.request.user.my_comments \
            .select_related('author')
        return queryset
