from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from home.models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from bootstrap_datepicker_plus import DatePickerInput


class ClientSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'username',
            'password1',
            'password2',
            'image',
        )

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_client = True
        user.save()
        client = Client.objects.create(user=user)
        return user


class StaffSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'username',
        )


class OwnerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'username',
            'password1',
            'password2',
            'image',
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_owner = True
        if commit:
            user.save()
        return user


class OwnerAddInfoForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ('ownerName', 'email', 'phone', 'location', 'gender')


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ('message', )
        widgets = {
            'message':
            forms.Textarea(
                attrs={
                    'rows': 3,
                    'placeholder': 'Share your feedback about this salon'
                })
        }


class TempUserForm(forms.ModelForm):
    class Meta:
        model = tempuser
        fields = (
            'name',
            'phone_no',
            'email',
        )


class addSalonForm(forms.ModelForm):
    class Meta:
        model = Salon
        fields = ('name', 'description', 'paybill', 'town',
                  'location_description')


class SalonSubscriptionForm(forms.ModelForm):
    class Meta:
        model = SalonSubscription
        fields = ('package', 'amount', 'payment_method')


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = (
            'firstname',
            'lastname',
            'job_description',
            'phone',
            'email',
            'date_started',
            'salary',
        )
        widgets = {
            'date_started': DatePickerInput(),
        }


class addClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('user', 'Full_Name', 'email', 'phone')


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = ('name', 'cost', 'duration', 'availability')


class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ('name', 'price', 'brand')


class clientAppointment(forms.ModelForm):
    class Meta:
        model = Appointments
        fields = ['appointment_date', ]
        labels = {
            'appointment_date': ''
        }
        widgets = {
            'appointment_date': DatePickerInput()
        }


class SalonAppointment(forms.ModelForm):
    class Meta:
        model = Appointments
        fields = ['services', 'appointment_date', 'products', 'clientphoneNo']
        widgets = {
            'services': forms.CheckboxSelectMultiple,
            'appointment_date': DatePickerInput(),
            'products': forms.CheckboxSelectMultiple,
        }


class AppointmentUpdateForm(forms.ModelForm):
    class Meta:
        model = Appointments
        fields = ['services']
        widgets = {
            'services': forms.CheckboxSelectMultiple,
        }


class ImageForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ('image', 'image_position')


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ('ownerName', 'email', 'phone', 'location')


class PpicUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('image',)
