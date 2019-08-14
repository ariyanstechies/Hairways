from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from home.models import *


class ClientSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'password1', 'password2','image', )
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_client = True
        user.save()
        client = Client.objects.create(user=user)
        return user


class OwnerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_owner = True
        if commit:
            user.save()
        return user


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ('comment', )


class addEmployeeForm(forms.ModelForm):

    class Meta:
        model = Staff
        fields = ('firstname', 'lastname', 'phone',
                  'email', 'salary', 'date_started',)


class addClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ('user', 'Full_Name', 'email', 'phone')


class addServiceForm(forms.ModelForm):

    class Meta:
        model = Services
        fields = ('serviceName', 'serviceCost', 'serviceDuration',
                  'serviceBookings', 'availability', 'salons')


class addProductForm(forms.ModelForm):

    class Meta:
        model = Products
        fields = ('product_name', 'price', 'product_brand', 'salons')


class clientAppointment(forms.ModelForm):

    class Meta:
        model = Appointments
        fields = ('client', 'clientphoneNo',
                  'salons', 'totalCost', 'date_time')


class AppointmentUpdateForm(forms.ModelForm):
    class Meta:
        model = Appointments
        fields = ['services']
        widgets = {
            'services': forms.CheckboxSelectMultiple,
        }
