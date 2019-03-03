from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView
from ..forms import OwnerSignUpForm
from ..models import User, Owner, Appointments, Comments
from ..decorators import owner_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import get_list_or_404, get_object_or_404
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)


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


@method_decorator([login_required, owner_required], name='dispatch')
class OwnerUpdate(UpdateView):
    model = Owner
    fields = ['email', 'ownerName','phone','location','gender']
    template_name =  'owners/owner_update_form.html'

    def get_object(self):

        return get_object_or_404(Owner, pk=self.request.user.id)
        # TODO: add redirect url or succes_url
