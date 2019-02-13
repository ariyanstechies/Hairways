from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView
from ..forms import OwnerSignUpForm
from ..models import User

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
        return redirect('home')
